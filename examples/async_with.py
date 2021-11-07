import asyncio
import random
from sp110e.сontroller import Controller


async def main():
    async with Controller('AF:00:10:01:C8:AF', timeout=2, retries=1) as device:
        await device.switch_on()
        await device.set_brightness(255)
        for i in range(0, 10):
            color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
            await device.set_color(color)
        await device.switch_off()

if __name__ == "__main__":
    asyncio.run(main())
