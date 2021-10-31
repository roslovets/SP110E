import asyncio
from Driver import Driver, discover as driver_discover


class Controller:
    """High-level SP110E asynchronous controller."""
    Driver = None

    def __init__(self):
        self.Driver = Driver()

    @staticmethod
    async def discover() -> list:
        """Discover BLE devices."""
        return await driver_discover()

    async def connect(self, mac_address: str):
        """Establish BLE connection to device."""
        await self.Driver.connect(mac_address)

    async def disconnect(self) -> None:
        """Close connection to device."""
        await self.Driver.disconnect()

    async def update(self) -> None:
        """Update device state."""
        await self.Driver.get_info()

    async def configure(self, ic_model: str, sequence: str, pixels: int) -> None:
        await self.Driver.set_ic_model(ic_model)
        await self.Driver.set_sequence(sequence)
        await self.Driver.set_pixels(pixels)

    async def switch_on(self) -> None:
        """Switch device on."""
        await self.Driver.set_state(True)

    async def switch_off(self) -> None:
        """Switch device off."""
        await self.Driver.set_state(False)

    async def toggle(self) -> bool:
        """Toggle device state between on/off."""
        if self.Driver.get_state():
            # Switch off
            await self.Driver.set_state(False)
        else:
            # Switch on
            await self.Driver.set_state(True)
        return self.Driver.get_state()

    async def set_mode(self, mode: int) -> None:
        """Set work mode (0-121). 0 - auto mode (demo)."""
        if mode == 0:
            await self.Driver.auto_mode()
        else:
            await self.Driver.set_mode(mode)

    async def set_speed(self, speed: int) -> None:
        """Set speed of automatic modes (0-255)."""
        await self.Driver.set_speed(speed)

    async def set_brightness(self, brightness: int) -> None:
        """Set LED brightness (0-255)."""
        await self.Driver.set_brightness(brightness)

    async def set_color(self, color: [int, int, int]) -> None:
        """Set static color in RGB format (0-255)."""
        await self.Driver.set_color(color)

    async def set_white(self, white: int) -> None:
        """Set brightness of white LED (0-255)."""
        await self.Driver.set_white(white)

    def is_on(self) -> bool:
        """Check device is On."""
        return self.Driver.get_state()

    def get_mode(self) -> int:
        """Get work mode (0-121). 0 - auto mode (demo)."""
        return self.Driver.get_mode()

    def get_speed(self) -> int:
        """Get speed of automatic modes (0-255)."""
        return self.Driver.get_speed()

    def get_brightness(self) -> int:
        """Get LED brightness (0-255)."""
        return self.Driver.get_brightness()

    def get_color(self) -> [int, int, int]:
        """Get static color in RGB format (0-255)."""
        return self.Driver.get_color()

    def get_white(self) -> int:
        """Get brightness of white LED (0-255)."""
        return self.Driver.get_white()

    def print_info(self):
        """Print device info."""
        self.Driver.print_info()
