import asyncio
from SP110E.Controller import Controller


async def main():
    device = Controller()
    await device.connect('AF:00:10:01:C8:AF')
    await device.switch_on()
    await device.set_brightness(255)
    await device.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
