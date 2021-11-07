from typing import Any, Union
from SP110E.Driver import Driver, discover as driver_discover


class Controller:
    """High-level SP110E asynchronous controller."""
    Driver = None
    MACAddress: str = None
    Timeout: float = None
    Retries: int = None

    def __init__(self, mac_address: str, timeout: float = 3.0, retries: int = 0):
        """On object creation."""
        self.MACAddress = mac_address
        self.Timeout = timeout
        self.Retries = retries
        self.Driver = Driver()

    @staticmethod
    async def discover() -> list:
        """Discover BLE devices."""
        return await driver_discover()

    async def connect(self):
        """Establish BLE connection to device."""
        await self.__connect_with_retries()

    async def disconnect(self) -> None:
        """Close connection to device."""
        if self.Driver.is_connected():
            await self.Driver.disconnect()

    def is_connected(self):
        """check device is connected."""
        return self.Driver.is_connected()

    async def switch_on(self) -> None:
        """Switch device on."""
        await self.set_state(True)

    async def switch_off(self) -> None:
        """Switch device off."""
        await self.set_state(False)

    async def toggle(self) -> bool:
        """Toggle device state between on/off."""
        new_state = not self.get_state()
        await self.set_state(new_state)
        return new_state

    async def update(self):
        """Read device parameters."""
        await self.__connect_with_retries()
        await self.Driver.read_parameters()

    async def set_ic_model(self, ic_model: str, force: bool = False) -> None:
        """Set device IC model."""
        await self.__connect_and_write_parameter('ic_model', ic_model, force=force)

    async def set_sequence(self, sequence: str, force: bool = False) -> None:
        """Set device color sequence."""
        await self.__connect_and_write_parameter('sequence', sequence, force=force)

    async def set_pixels(self, pixels: int, force: bool = False) -> None:
        """Set number of pixels in LED strip."""
        await self.__connect_and_write_parameter('pixels', pixels, force=force)

    async def set_state(self, state: bool, force: bool = False) -> None:
        """Set device state: on/off."""
        await self.__connect_and_write_parameter('state', state, force=force)

    async def set_mode(self, mode: int, force: bool = False) -> None:
        """Set work mode (0-121). 0 - auto mode (demo)."""
        await self.__connect_and_write_parameter('mode', mode, force=force)

    async def set_speed(self, speed: int, force: bool = False) -> None:
        """Set speed of automatic modes (0-255)."""
        await self.__connect_and_write_parameter('speed', speed, force=force)

    async def set_brightness(self, brightness: int, force: bool = False) -> None:
        """Set LED brightness (0-255)."""
        await self.__connect_and_write_parameter('brightness', brightness, force=force)

    async def set_color(self, color: [int, int, int], force: bool = False) -> None:
        """Set static color in RGB format (0-255)."""
        color = list(color)
        await self.__connect_and_write_parameter('color', color, force=force)

    async def set_white(self, white: int, force: bool = False) -> None:
        """Set brightness of white LED (0-255)."""
        await self.__connect_and_write_parameter('white', white, force=force)

    def set_mac_address(self, mac_address: str) -> None:
        """Set device MAC address."""
        self.MACAddress = mac_address

    def get_mac_address(self) -> str:
        """Get device MAC address."""
        return self.MACAddress

    def is_on(self) -> bool:
        """Check device is On."""
        return self.get_state()

    def get_ic_model(self) -> str:
        """Get device IC model."""
        return self.Driver.get_parameter('ic_model')

    def get_sequence(self) -> str:
        """Set device color sequence."""
        return self.Driver.get_parameter('sequence')

    def get_pixels(self) -> int:
        """Set number of pixels in LED strip."""
        return self.Driver.get_parameter('pixels')

    def get_state(self) -> bool:
        """Get device state: on/off."""
        return self.Driver.get_parameter('state')

    def get_mode(self) -> int:
        """Get work mode (0-121). 0 - auto mode (demo)."""
        return self.Driver.get_parameter('mode')

    def get_speed(self) -> int:
        """Get speed of automatic modes (0-255)."""
        return self.Driver.get_parameter('speed')

    def get_brightness(self) -> int:
        """Get LED brightness (0-255)."""
        return self.Driver.get_parameter('brightness')

    def get_color(self) -> [int, int, int]:
        """Get static color in RGB format (0-255)."""
        return self.Driver.get_parameter('color')

    def get_white(self) -> int:
        """Get brightness of white LED (0-255)."""
        return self.Driver.get_parameter('white')

    def get_sequences(self) -> tuple:
        """Get list of supported RGB sequence types."""
        return self.Driver.get_sequences()

    def get_ic_models(self) -> tuple:
        """Get list of supported IC models."""
        return self.Driver.get_ic_models()

    def get_modes(self) -> tuple:
        """Get list of supported modes."""
        return self.Driver.get_modes()

    async def __aenter__(self):
        """Enter context callback."""
        await self.connect()
        return self

    async def __aexit__(self, *excinfo):
        """Exit context callback."""
        await self.disconnect()

    async def __connect_with_retries(self):
        """Establish BLE connection to device with retries."""
        for i in range(0, self.Retries + 1):
            try:
                if not self.Driver.is_connected():
                    await self.Driver.connect(self.MACAddress, timeout=self.Timeout)
            except Exception:
                if i == self.Retries:
                    raise Exception

    async def __connect_and_write_parameter(self, parameter: str, value: Any, force: bool = False) -> None:
        """Write parameter to device with auto connect."""
        if (value is not None) and (force or value != self.Driver.get_parameter(parameter)):
            await self.__connect_with_retries()
            await self.Driver.write_parameter(parameter, value)
