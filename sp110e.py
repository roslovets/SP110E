import asyncio
from bleak import BleakClient, BleakScanner
from bleak.exc import BleakError


class SP110E:
    Client = None
    Data = None
    State: bool = True
    Mode: int = None
    Speed: int = None
    Brightness: int = None
    ICModel: int = None
    Channel: int = None
    Pixels: int = None
    Color: [int, int, int] = None
    White: int = None
    __Characteristic = '0000ffe1-0000-1000-8000-00805f9b34fb'
    __Flag = None

    def __init__(self):
        pass

    async def connect(self, mac_address: str):
        device = await BleakScanner.find_device_by_address(mac_address, timeout=5.0)
        if not device:
            raise BleakError(f"A device with address {mac_address} could not be found.")
        self.Client = BleakClient(device)
        await self.Client.connect()
        await self.Client.start_notify(self.__Characteristic, self.callback_handler)
        await self.check()

    async def read(self):
        return await self.Client.read_gatt_char(self.__Characteristic)

    async def write(self, bytes_to_write: [hex]):
        await self.Client.write_gatt_char(self.__Characteristic, bytearray(bytes_to_write))

    async def command(self, command_byte: hex, data_bytes: [hex, hex, hex] = (0x00, 0x00, 0x00)):
        if type(data_bytes) not in [list, tuple]:
            data_bytes = (data_bytes, 0, 0)
        await self.write(tuple(data_bytes) + tuple([command_byte]))

    def callback_handler(self, sender, data):
        if sender == 12:
            self.Data = data
            self.State = self.Data[0] == 1
            self.Mode = self.Data[1]
            self.Speed = self.Data[2]
            self.Brightness = self.Data[3]
            self.ICModel = self.Data[4]
            self.Channel = self.Data[5]
            self.Pixels = int.from_bytes(self.Data[6:8], byteorder='big')
            self.Color = [self.Data[8], self.Data[9], self.Data[10]]
            self.White = self.Data[11]
        if self.__Flag:
            self.__Flag.set()

    async def check(self):
        self.__Flag = asyncio.Event()
        await self.command(0x10)
        await self.__Flag.wait()

    async def disconnect(self):
        await self.Client.disconnect()

    async def switch_on(self):
        await self.command(0xAA)
        self.State = True

    async def switch_off(self):
        await self.command(0xAB)
        self.State = False

    async def toggle(self):
        if self.State:
            await self.switch_off()
        else:
            await self.switch_on()

    async def set_pixels(self, pixels: int):
        pixels_bytes = pixels.to_bytes(2, byteorder='big')
        await self.command(0x2D, [pixels_bytes[0], pixels_bytes[1], 0])
        self.Pixels = pixels

    async def set_color(self, color: [int, int, int]):
        await self.command(0x1E, color)
        self.Color = color
        self.Mode = 121

    async def set_brightness(self, brightness: int):
        await self.command(0x2A, brightness)
        self.Brightness = brightness

    async def set_white(self, white: int):
        await self.command(0x69, white)
        self.White = white

    async def set_mode(self, mode: int):
        await self.command(0x2C, mode)
        self.Mode = mode

    async def set_speed(self, speed: int):
        await self.command(0x03, speed)
        self.Speed = speed

    async def auto_mode(self):
        await self.command(0x06)
        self.Mode = 0

    async def set_sequence(self, sequence):
        idx = self.get_sequences().index(sequence)
        await self.command(0x3C, idx)

    def get_state(self) -> bool:
        return self.State

    def get_mode(self) -> int:
        return self.Mode

    def get_speed(self) -> int:
        return self.Speed

    def get_brightness(self) -> int:
        return self.Brightness

    def get_ic_model(self) -> int:
        return self.ICModel

    def get_channel(self) -> int:
        return self.Channel

    def get_pixels(self) -> int:
        return self.Pixels

    def get_color(self) -> (int, int, int):
        return self.Color

    def get_white(self) -> int:
        return self.White

    @staticmethod
    def get_sequences() -> tuple:
        return 'RGB', 'RBG', 'GRB', 'GBR', 'BRG', 'BGR'

    def print_info(self):
        print('State:', self.get_state())
        print('Mode:', self.get_mode())
        print('Speed:', self.get_speed())
        print('Brightness:', self.get_brightness())
        print('IC Model:', self.get_ic_model())
        print('Channel:', self.get_channel())
        print('Pixels:', self.get_pixels())
        print('Color:', self.get_color())
        print('White:', self.get_white())
