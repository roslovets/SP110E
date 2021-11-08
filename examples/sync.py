from sp110e.controller_sync import ControllerSync

device = ControllerSync('AF:00:10:01:C8:AF', timeout=2, retries=1)
device.connect()  # Optional
device.print_parameters()
device.switch_on()
device.set_brightness(255)
device.switch_off()
device.disconnect()  # Optional
