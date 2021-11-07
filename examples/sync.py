from SP110E.ControllerSync import ControllerSync

device = ControllerSync('AF:00:10:01:C8:AF', timeout=2, retries=1)
device.switch_on()
device.set_brightness(255)
device.switch_off()
