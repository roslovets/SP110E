import asyncio
from sp110e.driver import Driver


async def main():
    device = Driver()
    await device.connect('AF:00:10:01:C8:AF')
    device.print_parameters()
    await device.write_parameters({
        'ic_model': 'UCS1903',
        'sequence': 'GRB',
        'pixels': 60
    })
    await device.write_parameter('state', True)
    await device.write_parameter('color', [0, 255, 0])
    await device.write_parameter('brightness', 50)
    await device.write_parameter('white', 0)
    await device.write_parameter('speed', 50)
    device.print_parameters()
    await device.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
