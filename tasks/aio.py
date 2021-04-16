import aiohttp
import asyncio


async def fetch(url: str, session: aiohttp.ClientSession):
    return await session.get(url)


async def page_exists(url: str, session: aiohttp.ClientSession):
    resp = await fetch(url, session)
    return resp.status in range(200, 300)
