import asyncio
from bleak import BleakClient, BleakScanner, discover as BleakDiscover
from bleak.exc import BleakError


class Driver:
    """Low-level SP110E asynchronous BLE driver based on bleak library."""
    Client = None
    Parameters = None
    __ICModels = (
        'SM16703', 'TM1804', 'UCS1903', 'WS2811', 'WS2801', 'SK6812', 'LPD6803', 'LPD8806', 'APA102', 'APA105',
        'DMX512', 'TM1914', 'TM1913', 'P9813', 'INK1003', 'P943S', 'P9411', 'P9413', 'TX1812', 'TX1813', 'GS8206',
        'GS8208', 'SK9822', 'TM1814', 'SK6812_RGBW', 'P9414', 'PG412')
    __Sequences = ('RGB', 'RBG', 'GRB', 'GBR', 'BRG', 'BGR')
    __Characteristic = '0000ffe1-0000-1000-8000-00805f9b34fb'
    __Modes = tuple(range(0, 122))
    __Flag = None

    def __init__(self):
        """Initialize object."""
        self.__handle_parameters(bytearray([0] * 12))

    async def connect(self, mac_address: str, timeout: float = 3.0):
        """Establish BLE connection to device."""
        device = await BleakScanner.find_device_by_address(mac_address, timeout=timeout)
        if not device:
            raise BleakError(f"A device with address {mac_address} could not be found.")
        self.Client = BleakClient(device)
        await self.Client.connect()
        await self.Client.start_notify(self.__Characteristic, self.__callback_handler)
        await self.read_parameters()

    async def disconnect(self) -> None:
        """Close connection to device."""
        await self.Client.disconnect()

    def is_connected(self) -> bool:
        """Check connection to device."""
        if self.Client:
            return self.Client.is_connected
        else:
            return False

    async def send_command(self, command_byte: hex, data_bytes: [hex, hex, hex] = (0x00, 0x00, 0x00)):
        """Send command with data."""
        if type(data_bytes) not in [list, tuple]:
            data_bytes = (data_bytes, 0, 0)
        data_to_write = tuple(data_bytes) + tuple([command_byte])
        await self.Client.write_gatt_char(self.__Characteristic, bytearray(data_to_write))

    async def read_parameters(self) -> dict:
        """Read parameters information from device."""
        self.__Flag = asyncio.Event()
        await self.send_command(0x10)
        # Wait for callback with data from device
        await asyncio.wait_for(self.__Flag.wait(), 5)
        return self.Parameters

    async def write_parameters(self, parameters: dict) -> dict:
        """Write device parameters to device in batch mode."""
        for param, value in parameters.items():
            if param == 'state':
                if value:
                    await self.send_command(0xAA)  # Switch on
                else:
                    await self.send_command(0xAB)  # Switch off
            elif param == 'mode':
                if value not in self.__Modes:
                    raise ValueError(f'Mode is not supported: {value}')
                if value == 0:
                    await self.send_command(0x06)
                else:
                    await self.send_command(0x2C, value)
            elif param == 'speed':
                await self.send_command(0x03, value)
            elif param == 'brightness':
                await self.send_command(0x2A, value)
            elif param == 'ic_model':
                if value not in self.__ICModels:
                    raise ValueError(f'IC Model is not supported: {value}')
                idx = self.__ICModels.index(value)
                await self.send_command(0x1C, idx)
            elif param == 'sequence':
                if value not in self.__Sequences:
                    raise ValueError(f'Sequence is not supported: {value}')
                idx = self.__Sequences.index(value)
                await self.send_command(0x3C, idx)
            elif param == 'pixels':
                pixels_bytes = value.to_bytes(2, byteorder='big')
                await self.send_command(0x2D, [pixels_bytes[0], pixels_bytes[1], 0])
            elif param == 'color':
                await self.send_command(0x1E, value)
            elif param == 'white':
                await self.send_command(0x69, value)
        return await self.read_parameters()

    def get_parameters(self) -> dict:
        """Get read parameters."""
        return self.Parameters

    def get_sequences(self) -> tuple:
        """Get list of supported RGB sequence types."""
        return self.__Sequences

    def get_ic_models(self) -> tuple:
        """Get list of supported IC models."""
        return self.__ICModels

    def get_modes(self) -> tuple:
        """Get list of supported modes."""
        return self.__Modes

    def print_info(self):
        """Print device info."""
        for key in self.Parameters:
            print(key, ':', self.Parameters[key])

    def __callback_handler(self, sender, data: bytearray):
        """Handle callback with data from device."""
        if sender == 12:
            self.__handle_parameters(data)
        if self.__Flag:
            # Let get_info() method to go further
            self.__Flag.set()

    def __handle_parameters(self, data: bytearray):
        """Handle read parameters."""
        self.Parameters = {
            'state': data[0] == 1,
            'mode': data[1],
            'speed': data[2],
            'brightness': data[3],
            'ic_model': self.__ICModels[data[4]],
            'sequence': self.__Sequences[data[5]],
            'pixels': int.from_bytes(data[6:8], byteorder='big'),
            'color': [data[8], data[9], data[10]],
            'white': data[11]
        }


async def discover() -> list:
    """Discover BLE devices."""
    devices = await BleakDiscover()
    if devices:
        devices_list = [{d.name: d.address} for d in devices]
    else:
        devices_list = None
    return devices_list
