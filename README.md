# SP110E Python Library

Control SP110E BLE RGB LED device from computer

## Install

```bash
pip install sp110e
```

## Tools

- Controller: High-level SP110E asynchronous controller. Use it only in asynchronous environment (with `asyncio`)
- ControllerSync: Synchronous adapter for high-level SP110E asynchronous controller. Handy tool to use from Python shell or synchronous (normal) environment
- Driver: Low-level SP110E asynchronous BLE driver based on bleak library. Use it only if you know why

## Documentation

[Full API Reference](./docs)

## Examples

Quick start:

```python
from sp110e.controller_sync import ControllerSync

device = ControllerSync('AF:00:10:01:C8:AF')
device.switch_on()
device.set_color([255, 0, 0])
device.set_brightness(255)
```

[More examples](examples)

## Development

### Create new release

Push changes to 'main' branch following [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/).

### Update documentation

`docs` folder is being updated automatically by GitHub Actions when source files are changed.

## Integrations

- [SP110E Home Assistant Integration](https://github.com/roslovets/SP110E-HASS)

## Useful links

- [SP110E API Reference](https://gist.github.com/mbullington/37957501a07ad065b67d4e8d39bfe012)
- [Vox](https://github.com/nguyenthuongvo/Vox)
- [bleak library](https://github.com/hbldh/bleak)
- [Reverse engineering simple BLE](http://nilhcem.com/iot/reverse-engineering-simple-bluetooth-devices)
