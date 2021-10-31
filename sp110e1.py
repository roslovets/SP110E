import pygatt
from binascii import hexlify


class SP110E:
    Adapter = None
    Device = None
    Characteristic = '0000ffe1-0000-1000-8000-00805f9b34fb'
    Info = None
    Status: bool = True

    def __init__(self):
        self.Adapter = pygatt.GATTToolBackend()

    def connect(self, mac_address: str):
        self.Adapter.start()
        self.Device = self.Adapter.connect(mac_address)
        self.Device.subscribe(self.Characteristic, callback=self.handle_data)
        self.check()

    def write(
            self,
            bytes: [hex],
            wait: bool = True
    ):
        self.Device.char_write(
            self.Characteristic,
            bytearray(bytes),
            wait_for_response=wait
        )

    def write_command(
            self,
            data_bytes: [hex, hex, hex],
            command_byte: hex,
            wait: bool = True
    ):
        self.write(data_bytes + [command_byte], wait=wait)

    def read(self):
        return self.Device.char_read(self.Characteristic)

    def handle_data(self, handle, value):
        if handle == 13:
            self.Info = value
            self.Status = self.get_status()

    def check(self):
        self.write_command([0x00, 0x00, 0x00], 0x10)

    def disconnect(self):
        self.Adapter.stop()

    def switch_on(self):
        self.write_command([0x00, 0x00, 0x00], 0xAA)
        self.Status = True

    def switch_off(self):
        self.write_command([0x00, 0x00, 0x00], 0xAB)
        self.Status = False

    def toggle(self):
        if self.Status:
            self.switch_off()
        else:
            self.switch_on()

    def set_color(self, color: [int]):
        self.write_command([color[0], color[1], color[2]], 0x1E)

    def auto_mode(self):
        self.write_command([0, 0, 0], 6)

    def get_status(self) -> bool:
        return self.Info[0] == 1

    def get_preset(self) -> int:
        return self.Info[1]

    def get_speed(self) -> int:
        return self.Info[2]

    def get_brightness(self) -> int:
        return self.Info[3]

    def get_ic_model(self) -> int:
        return self.Info[4]

    def get_channel(self) -> int:
        return self.Info[5]

    def get_pixels(self) -> int:
        return int.from_bytes(self.Info[6:8], byteorder='big')

    def get_color(self) -> [int, int, int]:
        return [self.Info[8], self.Info[9], self.Info[10]]

    def get_white(self) -> int:
        return self.Info[11]

    def set_rgb_seq(self, channel):
        self.write_command([channel, 0, 0], 0x3C)
