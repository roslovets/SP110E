from typing import Union
from sp110e.driver import Driver, discover as driver_discover


class Controller:
    """High-level sp110e asynchronous controller.

    Use it only in asynchronous environment (with `asyncio`).

    Author: Pavel Roslovets
    https://roslovets.github.io
    """

    def __init__(self, mac: str, timeout: float = 3.0, retries: int = 0):
        """On object creation."""
        self._mac = mac
        self._timeout = timeout
        self._retries = retries
        self._driver = Driver()
        self._presets = []

    @staticmethod
    async def discover() -> list:
        """Discover BLE devices."""
        return await driver_discover()

    async def connect(self):
        """Establish BLE connection to device."""
        await self._connect_with_retries()

    async def disconnect(self) -> None:
        """Close connection to device."""
        if self._driver.is_connected():
            await self._driver.disconnect()

    def is_connected(self):
        """Check device is connected."""
        return self._driver.is_connected()

    def is_rgbw(self) -> bool:
        """Check IC model supports RGBW mode."""
        return self._driver.is_ic_model_rgbw()

    async def switch_on(self, force: bool = False) -> None:
        """Switch device on."""
        await self.set_state(True, force=force)

    async def switch_off(self, force: bool = False) -> None:
        """Switch device off."""
        await self.set_state(False, force=force)

    async def toggle(self) -> bool:
        """Toggle device state between on/off."""
        new_state = not self.get_state()
        await self.set_state(new_state)
        return new_state

    async def update(self) -> dict:
        """Read device parameters."""
        await self._connect_with_retries()
        return await self._driver.read_parameters()

    async def set_ic_model(self, ic_model: str, force: bool = False) -> None:
        """Set device IC model."""
        await self._connect_and_write_parameters({'ic_model': ic_model}, force=force)

    async def set_sequence(self, sequence: str, force: bool = False) -> None:
        """Set device color sequence."""
        await self._connect_and_write_parameters({'sequence': sequence}, force=force)

    async def set_pixels(self, pixels: int, force: bool = False) -> None:
        """Set number of pixels in LED strip."""
        await self._connect_and_write_parameters({'pixels': pixels}, force=force)

    async def set_state(self, state: bool, force: bool = False) -> None:
        """Set device state: on/off."""
        await self._connect_and_write_parameters({'state': state}, force=force)

    async def set_mode(self, mode: int, force: bool = False) -> None:
        """Set work mode (0-121). 0 - auto mode (demo)."""
        await self._connect_and_write_parameters({'mode': mode}, force=force)

    async def set_speed(self, speed: int, force: bool = False) -> None:
        """Set speed of automatic modes (0-255)."""
        await self._connect_and_write_parameters({'speed': speed}, force=force)

    async def set_brightness(self, brightness: int, force: bool = False) -> None:
        """Set LED brightness (0-255)."""
        await self._connect_and_write_parameters({'brightness': brightness}, force=force)

    async def set_color(self, color: [int, int, int], force: bool = False) -> None:
        """Set static color in RGB format (0-255)."""
        await self._connect_and_write_parameters({'color': list(color)}, force=force)

    async def set_white(self, white: int, force: bool = False) -> None:
        """Set brightness of white LED (0-255)."""
        await self._connect_and_write_parameters({'white': white}, force=force)

    async def set_preset(self, name: str, force: bool = False):
        """Select defined preset."""
        preset, _ = self._find_preset(name)
        parameters = {
            'state': preset.get('state', None),
            'mode': preset.get('mode', None),
            'speed': preset.get('speed', None),
            'brightness': preset.get('brightness', None),
            'color': preset.get('color', None),
            'white': preset.get('white', None)
        }
        await self._connect_and_write_parameters(parameters, force=force)

    def add_preset(self, preset: dict):
        """Add preset to control device parameters."""
        name = preset['name']
        _, index = self._find_preset(name)
        if index is not None:
            self._presets[index] = preset
        else:
            self._presets.append(preset)

    def set_mac_address(self, mac_address: str) -> None:
        """Set device MAC address."""
        self._mac = mac_address

    def get_presets(self) -> list:
        """Get all defined presets."""
        return self._presets

    def get_preset(self, name: str) -> Union[dict, None]:
        """Get defined preset by name."""
        preset, _ = self._find_preset(name)
        return preset

    def get_mac_address(self) -> str:
        """Get device MAC address."""
        return self._mac

    def is_on(self) -> bool:
        """Check device is On."""
        return self.get_state()

    def get_ic_model(self) -> str:
        """Get device IC model."""
        return self._driver.get_parameter('ic_model')

    def get_sequence(self) -> str:
        """Set device color sequence."""
        return self._driver.get_parameter('sequence')

    def get_pixels(self) -> int:
        """Set number of pixels in LED strip."""
        return self._driver.get_parameter('pixels')

    def get_state(self) -> bool:
        """Get device state: on/off."""
        return self._driver.get_parameter('state')

    def get_mode(self) -> int:
        """Get work mode (0-121). 0 - auto mode (demo)."""
        return self._driver.get_parameter('mode')

    def get_speed(self) -> int:
        """Get speed of automatic modes (0-255)."""
        return self._driver.get_parameter('speed')

    def get_brightness(self) -> int:
        """Get LED brightness (0-255)."""
        return self._driver.get_parameter('brightness')

    def get_color(self) -> [int, int, int]:
        """Get static color in RGB format (0-255)."""
        return self._driver.get_parameter('color')

    def get_white(self) -> int:
        """Get brightness of white LED (0-255)."""
        return self._driver.get_parameter('white')

    def get_sequences(self) -> tuple:
        """Get list of supported RGB sequence types."""
        return self._driver.get_sequences()

    def get_ic_models(self) -> tuple:
        """Get list of supported IC models."""
        return self._driver.get_ic_models()

    def get_modes(self) -> tuple:
        """Get list of supported modes."""
        return self._driver.get_modes()

    def print_parameters(self):
        """Print device info."""
        self._driver.print_parameters()

    async def __aenter__(self):
        """Enter context callback."""
        await self.connect()
        return self

    async def __aexit__(self, *excinfo):
        """Exit context callback."""
        await self.disconnect()

    async def _connect_with_retries(self):
        """Establish BLE connection to device with retries."""
        for i in range(0, self._retries + 1):
            try:
                if not self._driver.is_connected():
                    await self._driver.connect(self._mac, timeout=self._timeout)
            except Exception:
                if i == self._retries:
                    raise Exception

    async def _connect_and_write_parameters(self, parameters: dict, force: bool = False) -> None:
        """Write parameter to device with auto connect."""
        parameters_to_write = parameters
        for parameter in list(parameters):
            value = parameters[parameter]
            if (value is None) or (not force and (value == self._driver.get_parameter(parameter))):
                del parameters_to_write[parameter]
        if parameters_to_write:
            await self._connect_with_retries()
            await self._driver.write_parameters(parameters_to_write)

    def _find_preset(self, name: str) -> (dict, int):
        """Find defined preset by name."""
        index = next((index for (index, d) in enumerate(self._presets) if d['name'] == name), None)
        if index is not None:
            preset = self._presets[index]
        else:
            preset = None
        return preset, index
