from SP110E.Driver import Driver, discover as driver_discover


class Controller:
    """High-level SP110E asynchronous controller."""
    Driver = None
    MACAddress: str = None
    Connected: bool = False

    def __init__(self, mac_address: str = None):
        """On object creation."""
        self.Driver = Driver()
        self.MACAddress = mac_address

    @staticmethod
    async def discover() -> list:
        """Discover BLE devices."""
        return await driver_discover()

    async def connect(self, mac_address: str = None):
        """Establish BLE connection to device."""
        if mac_address:
            self.MACAddress = mac_address
        await self.Driver.connect(self.MACAddress)
        self.Connected = True

    async def disconnect(self) -> None:
        """Close connection to device."""
        await self.Driver.disconnect()
        self.Connected = False

    def is_connected(self):
        """check device is connected."""
        return self.Connected

    async def configure(self, ic_model: str, sequence: str, pixels: int) -> None:
        await self.Driver.write_parameters({
            'ic_model': ic_model,
            'sequence': sequence,
            'pixels': pixels
        })

    async def switch_on(self) -> dict:
        """Switch device on."""
        return await self.__write_parameter('state', True)

    async def switch_off(self) -> dict:
        """Switch device off."""
        return await self.__write_parameter('state', False)

    async def toggle(self) -> bool:
        """Toggle device state between on/off."""
        if self.__get_parameter('state'):
            await self.__write_parameter('state', False)
        else:
            await self.__write_parameter('state', True)
        return self.__get_parameter('state')

    async def set_mode(self, mode: int) -> None:
        """Set work mode (0-121). 0 - auto mode (demo)."""
        await self.__write_parameter('mode', mode)

    async def set_speed(self, speed: int) -> None:
        """Set speed of automatic modes (0-255)."""
        await self.__write_parameter('speed', speed)

    async def set_brightness(self, brightness: int) -> None:
        """Set LED brightness (0-255)."""
        await self.__write_parameter('brightness', brightness)

    async def set_color(self, color: [int, int, int]) -> None:
        """Set static color in RGB format (0-255)."""
        await self.__write_parameter('color', color)

    async def set_white(self, white: int) -> None:
        """Set brightness of white LED (0-255)."""
        await self.__write_parameter('white', white)

    def is_on(self) -> bool:
        """Check device is On."""
        return self.__get_parameter('state')

    def get_mode(self) -> int:
        """Get work mode (0-121). 0 - auto mode (demo)."""
        return self.__get_parameter('mode')

    def get_speed(self) -> int:
        """Get speed of automatic modes (0-255)."""
        return self.__get_parameter('speed')

    def get_brightness(self) -> int:
        """Get LED brightness (0-255)."""
        return self.__get_parameter('brightness')

    def get_color(self) -> [int, int, int]:
        """Get static color in RGB format (0-255)."""
        return self.__get_parameter('color')

    def get_white(self) -> int:
        """Get brightness of white LED (0-255)."""
        return self.__get_parameter('white')

    def get_sequences(self) -> tuple:
        """Get list of supported RGB sequence types."""
        return self.Driver.get_sequences()

    def get_ic_models(self) -> tuple:
        """Get list of supported IC models."""
        return self.Driver.get_ic_models()

    def get_modes(self) -> tuple:
        """Get list of supported modes."""
        return self.Driver.get_modes()

    def __get_parameter(self, parameter: str):
        return self.Driver.get_parameters()[parameter]

    async def __write_parameter(self, parameter: str, value):
        return await self.Driver.write_parameters({parameter: value})
