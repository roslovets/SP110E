from typing import Any, Union
import asyncio
from bleak import BleakClient, BleakScanner, discover as bleak_discover
from bleak.exc import BleakError


async def discover() -> list:
    """Discover BLE devices."""
    devices = await bleak_discover()
    if devices:
        devices_list = [{d.name: d.address} for d in devices]
    else:
        devices_list = None
    return devices_list


class Driver:
    """Low-level sp110e asynchronous BLE driver based on bleak library.

    Use it only if you know why.

    Author: Pavel Roslovets
    https://roslovets.github.io
    """
    IC_MODELS = (
        'SM16703', 'TM1804', 'UCS1903', 'WS2811', 'WS2801', 'SK6812', 'LPD6803', 'LPD8806', 'APA102', 'APA105',
        'DMX512', 'TM1914', 'TM1913', 'P9813', 'INK1003', 'P943S', 'P9411', 'P9413', 'TX1812', 'TX1813',
        'GS8206', 'GS8208', 'SK9822', 'TM1814', 'SK6812_RGBW', 'P9414', 'PG412')
    SEQUENCES = ('RGB', 'RBG', 'GRB', 'GBR', 'BRG', 'BGR')
    CHARACTERISTIC = '0000ffe1-0000-1000-8000-00805f9b34fb'
    MODES = tuple(range(0, 122))
    _client = None
    _parameters = None
    _flag = None

    def __init__(self):
        """Initialize object."""
        self._handle_parameters(bytearray([0] * 12))

    async def connect(self, mac_address: str, timeout: float = 3.0, auto_read: bool = True) -> Union[dict, None]:
        """Establish BLE connection to device."""
        device = await BleakScanner.find_device_by_address(mac_address, timeout=timeout)
        if not device:
            raise BleakError(f'A device with address {mac_address} could not be found')
        self._client = BleakClient(device)
        await self._client.connect()
        await self._client.start_notify(self.CHARACTERISTIC, self._callback_handler)
        if auto_read:
            return await self.read_parameters()
        else:
            return None

    async def disconnect(self) -> None:
        """Close connection to device."""
        await self._client.disconnect()

    def is_connected(self) -> bool:
        """Check connection to device."""
        if self._client:
            return self._client.is_connected
        else:
            return False

    async def send_command(self, command_byte: hex, data_bytes: [hex, hex, hex] = (0x00, 0x00, 0x00)):
        """Send command with data."""
        if type(data_bytes) not in [list, tuple]:
            data_bytes = (data_bytes, 0, 0)
        data_to_write = tuple(data_bytes) + tuple([command_byte])
        await self._client.write_gatt_char(self.CHARACTERISTIC, bytearray(data_to_write))

    async def read_parameters(self) -> dict:
        """Read parameters information from device."""
        self._flag = asyncio.Event()
        await self.send_command(0x10)
        # Wait for callback with data from device
        try:
            await asyncio.wait_for(self._flag.wait(), 1)
        except Exception:
            pass
        return self._parameters

    async def write_parameters(self, parameters: dict, auto_read: bool = True) -> Union[dict, None]:
        """Write device parameters to device in batch mode."""
        for parameter, value in parameters.items():
            await self._write_parameter(parameter, value, auto_read=False)
        if auto_read:
            return await self.read_parameters()
        else:
            return None

    async def write_parameter(self, parameter: str, value: Any, auto_read: bool = True) -> Union[dict, None]:
        """Write device parameter to device."""
        return await self._write_parameter(parameter, value, auto_read)

    def get_parameter(self, parameter: str) -> Any:
        """Get read parameter by name."""
        return self._parameters[parameter]

    def get_parameters(self) -> dict:
        """Get read parameters."""
        return self._parameters

    def get_sequences(self) -> tuple:
        """Get list of supported RGB sequence types."""
        return self.SEQUENCES

    def get_ic_models(self) -> tuple:
        """Get list of supported IC models."""
        return self.IC_MODELS

    def is_ic_model_rgbw(self, ic_model: str = None) -> bool:
        """Check IC model supports RGBW mode."""
        if not ic_model:
            ic_model = self.get_parameter('ic_model')
        idx = self.IC_MODELS.index(ic_model)
        return idx > 22

    def get_modes(self) -> tuple:
        """Get list of supported modes."""
        return self.MODES

    def print_parameters(self):
        """Print device info."""
        for key in self._parameters:
            print(key, ':', self._parameters[key])

    async def _write_parameter(self, parameter: str, value: Any, auto_read: bool = True) -> Union[dict, None]:
        """Write device parameter to device."""
        if parameter == 'state':
            if value:
                await self.send_command(0xAA)  # Switch on
            else:
                await self.send_command(0xAB)  # Switch off
        elif parameter == 'mode':
            if value not in self.MODES:
                raise ValueError(f'Mode is not supported: {value}')
            if value == 0:
                await self.send_command(0x06)
            else:
                await self.send_command(0x2C, value)
        elif parameter == 'speed':
            await self.send_command(0x03, value)
        elif parameter == 'brightness':
            await self.send_command(0x2A, value)
        elif parameter == 'ic_model':
            if value not in self.IC_MODELS:
                raise ValueError(f'IC Model is not supported: {value}')
            idx = self.IC_MODELS.index(value)
            await self.send_command(0x1C, idx)
        elif parameter == 'sequence':
            if value not in self.SEQUENCES:
                raise ValueError(f'Sequence is not supported: {value}')
            idx = self.SEQUENCES.index(value)
            await self.send_command(0x3C, idx)
        elif parameter == 'pixels':
            pixels_bytes = value.to_bytes(2, byteorder='big')
            await self.send_command(0x2D, [pixels_bytes[0], pixels_bytes[1], 0])
        elif parameter == 'color':
            await self.send_command(0x1E, value)
        elif parameter == 'white':
            await self.send_command(0x69, value)
        if auto_read:
            return await self.read_parameters()
        else:
            return None

    def _callback_handler(self, sender, data: bytearray):
        """Handle callback with data from device."""
        if sender == 12:
            self._handle_parameters(data)
        if self._flag:
            # Let get_info() method to go further
            self._flag.set()

    def _handle_parameters(self, data: bytearray):
        """Handle read parameters."""
        self._parameters = {
            'state': data[0] == 1,
            'mode': data[1],
            'speed': data[2],
            'brightness': data[3],
            'ic_model': self.IC_MODELS[data[4]],
            'sequence': self.SEQUENCES[data[5]],
            'pixels': int.from_bytes(data[6:8], byteorder='big'),
            'color': [data[8], data[9], data[10]],
            'white': data[11]
        }
