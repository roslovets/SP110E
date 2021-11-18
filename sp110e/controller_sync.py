from syncer import sync
from sp110e.controller import Controller


class ControllerSync(Controller):
    """Synchronous adapter for high-level sp110e asynchronous controller."""
    Controller = None

    def __init__(self, mac_address: str = None, timeout: float = 3.0, retries: int = 0):
        """On object creation."""
        super().__init__(mac_address, timeout, retries)

    @sync
    async def discover(self) -> list:
        """Discover BLE devices."""
        return await super().discover()

    @sync
    async def connect(self):
        """Establish BLE connection to device."""
        await super().connect()

    @sync
    async def disconnect(self) -> None:
        """Close connection to device."""
        try:
            await super().disconnect()
        except:
            pass

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
    async def update(self) -> dict:
        """Read device parameters."""
        return await super().update()

    @sync
    async def set_ic_model(self, ic_model: str, force: bool = False) -> None:
        """Set device IC model."""
        await super().set_ic_model(ic_model, force)

    @sync
    async def set_sequence(self, sequence: str, force: bool = False) -> None:
        """Set device color sequence."""
        await super().set_sequence(sequence, force)

    @sync
    async def set_pixels(self, pixels: int, force: bool = False) -> None:
        await super().set_pixels(pixels, force)

    @sync
    async def set_mode(self, mode: int, force: bool = False) -> None:
        """Set work mode (0-121). 0 - auto mode (demo)."""
        await super().set_mode(mode, force)

    @sync
    async def set_speed(self, speed: int, force: bool = False) -> None:
        """Set speed of automatic modes (0-255)."""
        await super().set_speed(speed, force)

    @sync
    async def set_brightness(self, brightness: int, force: bool = False) -> None:
        """Set LED brightness (0-255)."""
        await super().set_brightness(brightness, force)

    @sync
    async def set_color(self, color: [int, int, int], force: bool = False) -> None:
        """Set static color in RGB format (0-255)."""
        await super().set_color(color, force)

    @sync
    async def set_white(self, white: int, force: bool = False) -> None:
        """Set brightness of white LED (0-255)."""
        await super().set_white(white, force)

    def __del__(self) -> None:
        """On object destruction."""
        self.disconnect()
