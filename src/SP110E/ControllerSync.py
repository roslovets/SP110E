from syncer import sync
from SP110E.Controller import Controller


class ControllerSync:
    """Synchronous adapter for high-level SP110E asynchronous controller."""
    Controller = None

    def __init__(self):
        """On object creation."""
        self.Controller = Controller()

    @sync
    async def discover(self) -> list:
        """Discover BLE devices."""
        return await self.Controller.discover()

    @sync
    async def connect(self, mac_address: str):
        """Establish BLE connection to device."""
        await self.Controller.connect(mac_address)

    @sync
    async def disconnect(self) -> None:
        """Close connection to device."""
        try:
            await self.Controller.disconnect()
        except:
            pass

    @sync
    async def update(self) -> None:
        """Update device state."""
        await self.Controller.update()

    @sync
    async def configure(self, ic_model: str, sequence: str, pixels: int) -> None:
        await self.Controller.configure(ic_model, sequence, pixels)

    @sync
    async def switch_on(self) -> None:
        """Switch device on."""
        await self.Controller.switch_on()

    @sync
    async def switch_off(self) -> None:
        """Switch device off."""
        await self.Controller.switch_off()

    @sync
    async def toggle(self) -> bool:
        """Toggle device state between on/off."""
        return await self.Controller.toggle()

    @sync
    async def set_mode(self, mode: int) -> None:
        """Set work mode (0-121). 0 - auto mode (demo)."""
        await self.Controller.set_mode(mode)

    @sync
    async def set_speed(self, speed: int) -> None:
        """Set speed of automatic modes (0-255)."""
        await self.Controller.set_speed(speed)

    @sync
    async def set_brightness(self, brightness: int) -> None:
        """Set LED brightness (0-255)."""
        await self.Controller.set_brightness(brightness)

    @sync
    async def set_color(self, color: [int, int, int]) -> None:
        """Set static color in RGB format (0-255)."""
        await self.Controller.set_color(color)

    @sync
    async def set_white(self, white: int) -> None:
        """Set brightness of white LED (0-255)."""
        await self.Controller.set_white(white)

    def is_on(self) -> bool:
        """Check device is On."""
        return self.Controller.is_on()

    def get_mode(self) -> int:
        """Get work mode (0-121). 0 - auto mode (demo)."""
        return self.Controller.get_mode()

    def get_speed(self) -> int:
        """Get speed of automatic modes (0-255)."""
        return self.Controller.get_speed()

    def get_brightness(self) -> int:
        """Get LED brightness (0-255)."""
        return self.Controller.get_brightness()

    def get_color(self) -> [int, int, int]:
        """Get static color in RGB format (0-255)."""
        return self.Controller.get_color()

    def get_white(self) -> int:
        """Get brightness of white LED (0-255)."""
        return self.Controller.get_white()

    def print_info(self):
        """Print device info."""
        self.Controller.print_info()

    def __del__(self) -> None:
        """On object destruction."""
        self.disconnect()
