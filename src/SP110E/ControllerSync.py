from syncer import sync
from SP110E.Controller import Controller


class ControllerSync(Controller):
    """Synchronous adapter for high-level SP110E asynchronous controller."""
    Controller = None

    def __init__(self, mac_address: str = None, timeout: float = 3.0, retries: int = 0):
        """On object creation."""
        super().__init__(mac_address, timeout, retries)

    @sync
    async def discover(self) -> list:
        """Discover BLE devices."""
        return await super().discover()

    @sync
    async def connect(self, mac_address: str = None):
        """Establish BLE connection to device."""
        await super().connect(mac_address)

    @sync
    async def disconnect(self) -> None:
        """Close connection to device."""
        try:
            await super().disconnect()
        except:
            pass

    @sync
    async def configure(self, ic_model: str, sequence: str, pixels: int) -> None:
        await super().configure(ic_model, sequence, pixels)

    @sync
    async def switch_on(self) -> None:
        """Switch device on."""
        await super().switch_on()

    @sync
    async def switch_off(self) -> None:
        """Switch device off."""
        await super().switch_off()

    @sync
    async def toggle(self) -> bool:
        """Toggle device state between on/off."""
        return await super().toggle()

    @sync
    async def set_mode(self, mode: int) -> None:
        """Set work mode (0-121). 0 - auto mode (demo)."""
        await super().set_mode(mode)

    @sync
    async def set_speed(self, speed: int) -> None:
        """Set speed of automatic modes (0-255)."""
        await super().set_speed(speed)

    @sync
    async def set_brightness(self, brightness: int) -> None:
        """Set LED brightness (0-255)."""
        await super().set_brightness(brightness)

    @sync
    async def set_color(self, color: [int, int, int]) -> None:
        """Set static color in RGB format (0-255)."""
        await super().set_color(color)

    @sync
    async def set_white(self, white: int) -> None:
        """Set brightness of white LED (0-255)."""
        await super().set_white(white)

    def __del__(self) -> None:
        """On object destruction."""
        self.disconnect()
