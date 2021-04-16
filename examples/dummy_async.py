import asyncio
from util import timecount


async def dummy(i: int):
    print('Begin:', i)
    # Simulate a non-blocking IO task
    await asyncio.sleep(i)
    print('End:', i)


@timecount.exectime
async def call():
    await asyncio.gather(
        dummy(1),
        dummy(2),
        dummy(3)
    )


asyncio.run(call())
