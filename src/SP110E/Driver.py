import asyncio
from bleak import BleakClient, BleakScanner, discover as BleakDiscover
from bleak.exc import BleakError


class Driver:
    """Low-level SP110E asynchronous BLE driver based on bleak library."""
    Client = None
    Info = None
    State: bool = True
    Mode: int = None
    Speed: int = None
    Brightness: int = None
    ICModel: str = None
    Sequence: str = None
    Pixels: int = None
    Color: [int, int, int] = None
    White: int = None
    __ICModels = (
        'SM16703', 'TM1804', 'UCS1903', 'WS2811', 'WS2801', 'SK6812', 'LPD6803', 'LPD8806', 'APA102', 'APA105',
        'DMX512', 'TM1914', 'TM1913', 'P9813', 'INK1003', 'P943S', 'P9411', 'P9413', 'TX1812', 'TX1813', 'GS8206',
        'GS8208', 'SK9822', 'TM1814', 'SK6812_RGBW', 'P9414', 'PG412')
    __Sequences = ('RGB', 'RBG', 'GRB', 'GBR', 'BRG', 'BGR')
    __Characteristic = '0000ffe1-0000-1000-8000-00805f9b34fb'
    __Flag = None

    async def connect(self, mac_address: str):
        """Establish BLE connection to device."""
        device = await BleakScanner.find_device_by_address(mac_address, timeout=5.0)
        if not device:
            raise BleakError(f"A device with address {mac_address} could not be found.")
        self.Client = BleakClient(device)
        await self.Client.connect()
        await self.Client.start_notify(self.__Characteristic, self.callback_handler)
        await self.get_info()

    async def write(self, bytes_to_write: [hex]):
        """Write bytes to device."""
        await self.Client.write_gatt_char(self.__Characteristic, bytearray(bytes_to_write))

    async def command(self, command_byte: hex, data_bytes: [hex, hex, hex] = (0x00, 0x00, 0x00)):
        """Send command with data."""
        if type(data_bytes) not in [list, tuple]:
            data_bytes = (data_bytes, 0, 0)
        await self.write(tuple(data_bytes) + tuple([command_byte]))

    def callback_handler(self, sender, data):
        """Handle callback with data from device."""
        if sender == 12:
            self.Info = data
            self.State = self.Info[0] == 1
            self.Mode = self.Info[1]
            self.Speed = self.Info[2]
            self.Brightness = self.Info[3]
            self.ICModel = self.get_ic_models()[self.Info[4]]
            self.Sequence = self.get_sequences()[self.Info[5]]
            self.Pixels = int.from_bytes(self.Info[6:8], byteorder='big')
            self.Color = [self.Info[8], self.Info[9], self.Info[10]]
            self.White = self.Info[11]
        if self.__Flag:
            # Let get_info() method to go further
            self.__Flag.set()

    async def get_info(self) -> bytearray:
        """Get information from device."""
        self.__Flag = asyncio.Event()
        await self.command(0x10)
        # Wait for callback with data from device
        await self.__Flag.wait()
        return self.Info

    async def disconnect(self) -> None:
        """Close connection to device."""
        await self.Client.disconnect()

    async def set_state(self, state: bool) -> None:
        """Set device state (True - on, False - off)."""
        if state:
            # Switch on
            await self.command(0xAA)
        else:
            # Switch off
            await self.command(0xAB)
        self.State = state

    async def set_mode(self, mode: int) -> None:
        """Set work mode (1-121)."""
        await self.command(0x2C, mode)
        self.Mode = mode

    async def set_speed(self, speed: int) -> None:
        """Set speed of automatic modes (0-255)."""
        await self.command(0x03, speed)
        self.Speed = speed

    async def set_brightness(self, brightness: int) -> None:
        """Set LED brightness (0-255)."""
        await self.command(0x2A, brightness)
        self.Brightness = brightness

    async def set_ic_model(self, ic_model: str) -> None:
        """Set name of LED strip IC model."""
        idx = self.get_ic_models().index(ic_model)
        await self.command(0x1C, idx)
        self.ICModel = ic_model

    async def set_sequence(self, sequence: str) -> None:
        """Set RGB sequence type."""
        idx = self.get_sequences().index(sequence)
        await self.command(0x3C, idx)
        self.Sequence = sequence

    async def set_pixels(self, pixels: int) -> None:
        """Set number of LED strip pixels (1-1024)."""
        pixels_bytes = pixels.to_bytes(2, byteorder='big')
        await self.command(0x2D, [pixels_bytes[0], pixels_bytes[1], 0])
        self.Pixels = pixels

    async def set_color(self, color: [int, int, int]) -> None:
        """Set static color in RGB format (0-255)."""
        await self.command(0x1E, color)
        self.Color = color
        self.Mode = 121

    async def set_white(self, white: int) -> None:
        """Set brightness of white LED (0-255)."""
        await self.command(0x69, white)
        self.White = white

    async def auto_mode(self) -> None:
        """Enable auto mode (demo)."""
        await self.command(0x06)
        self.Mode = 0

    def get_state(self) -> bool:
        """Get device state (True - on, False - off)."""
        return self.State

    def get_mode(self) -> int:
        """Get work mode (0-121). 0 - auto mode (demo)."""
        return self.Mode

    def get_speed(self) -> int:
        """Get speed of automatic modes (0-255)."""
        return self.Speed

    def get_brightness(self) -> int:
        """Get LED brightness (0-255)."""
        return self.Brightness

    def get_ic_model(self) -> str:
        """Get name of LED strip IC model."""
        return self.ICModel

    def get_sequence(self) -> str:
        """Get RGB sequence type."""
        return self.Sequence

    def get_pixels(self) -> int:
        """Get number of LED strip pixels (1-1024)."""
        return self.Pixels

    def get_color(self) -> [int, int, int]:
        """Get static color in RGB format (0-255)."""
        return self.Color

    def get_white(self) -> int:
        """Get brightness of white LED (0-255)."""
        return self.White

    def get_sequences(self) -> tuple:
        """Get list of supported RGB sequence types."""
        return self.__Sequences

    def get_ic_models(self) -> tuple:
        """Get list of supported IC models."""
        return self.__ICModels

    def print_info(self):
        """Print device info."""
        print('State:', self.get_state())
        print('Mode:', self.get_mode())
        print('Speed:', self.get_speed())
        print('Brightness:', self.get_brightness())
        print('IC Model:', self.get_ic_model())
        print('Sequence:', self.get_sequence())
        print('Pixels:', self.get_pixels())
        print('Color:', self.get_color())
        print('White:', self.get_white())


async def discover() -> list:
    """Discover BLE devices."""
    devices = await BleakDiscover()
    if devices:
        devices_list = [{d.name: d.address} for d in devices]
    else:
        devices_list = None
    return devices_list
