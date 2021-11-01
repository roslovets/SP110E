# SP110E Python Library

Control SP110E BLE RGB LED device from computer

## Install

```bash
pip install SP110E
```

## Tools

- Controller: High-level SP110E asynchronous controller. Use it only in asynchronous environment (with `asyncio`) 
- **ControllerSync**: Synchronous adapter for high-level SP110E asynchronous controller. Handy tool to use from Python shell or synchronous (normal) environment
- Driver: Low-level SP110E asynchronous BLE driver based on bleak library. Use it only if you're sure why.

## Examples

```python
from SP110E.ControllerSync import ControllerSync

device = ControllerSync()
device.connect('AF:00:10:01:C8:AF')
device.switch_on()
device.set_color([255, 0, 0])
device.set_brightness(255)
device.disconnect()
```

## Useful links

- [API Reference](https://gist.github.com/mbullington/37957501a07ad065b67d4e8d39bfe012)
- [Vox](https://github.com/nguyenthuongvo/Vox)
- [bleak library](https://github.com/hbldh/bleak)
- [Reverse engineering simple BLE](http://nilhcem.com/iot/reverse-engineering-simple-bluetooth-devices)
