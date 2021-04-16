import aiohttp
import asyncio
from tasks import aio
from util import timecount


@timecount.exectime
async def call():
    print('Index,Exists')
    page = 'https://en.wikipedia.org/wiki/{}'
    coro = []
    async with aiohttp.ClientSession() as session:
        for i in range(100):
            coro.append(aio.page_exists(page.format(i), session))

        results = await asyncio.gather(*coro)

    for i, res in enumerate(results):
        print(f'{i},{res}')


asyncio.run(call())
