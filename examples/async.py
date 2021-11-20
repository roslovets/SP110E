import asyncio
from sp110e.controller import Controller


async def main():
    device = Controller('AF:00:10:01:C8:AF', timeout=2, retries=1)
    await device.switch_on()
    await device.set_brightness(255)
    await device.set_color([0, 255, 0])
    await device.set_white(0)
    await device.set_speed(10)
    await device.set_mode(1)
    await device.switch_off()
    await device.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
