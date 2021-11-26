from sp110e.controller_sync import ControllerSync
from time import sleep

device = ControllerSync('AF:00:10:01:C8:AF', timeout=2, retries=1)
device.add_preset('red', {'color': [255, 0, 0], 'brightness': 100})
device.add_preset('new_year', {'mode': 1, 'speed': 100})
device.add_preset('demo', {'mode': 0, 'speed': 255, 'brightness': 10})
device.add_preset('off', {'state': False})
device.switch_on()
sleep(3)
device.set_preset('red')
sleep(3)
device.set_preset('new_year')
sleep(3)
device.set_preset('demo')
sleep(3)
device.set_preset('off')
device.disconnect()
