import asyncio
from src.SP110E.Driver import Driver, discover
import random


async def main():
    device = Driver()
    await device.connect('AF:00:10:01:C8:AF')
    await device.set_ic_model('UCS1903')
    await device.set_sequence('GRB')
    device.print_info()
    await device.set_state(True)
    await device.set_color([255, 0, 0])
    # await device.set_pixels(60)
    # await device.set_brightness(1)
    # await device.set_white(0)
    # await device.auto_mode()
    # await device.set_mode(10)
    # await device.set_speed(10)
    # await device.auto_mode()
    # await set_random_color(device)
    # await device.switch_off()
    # await asyncio.sleep(0.5)
    # await device.switch_on()
    # await device.check()
    # print_info(device)
    await device.disconnect()


async def set_random_color(device):
    await device.set_color([random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)])


if __name__ == "__main__":
    asyncio.run(main())
