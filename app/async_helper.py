import asyncio
from aiohttp import ClientSession
from . import util, app


async def fetch_image(image_list: list, url: str, lock: asyncio.Lock, session: ClientSession):
    app.logger.info(f"EXECUTING URL: {url}")
    resp = await session.request(method="GET", url=url)
    resp.raise_for_status()

    img = await resp.read()
    async with lock:
        image_list.append(img)


async def execute_async_call(url_list: list):
    async with ClientSession() as session:
        image_list = []
        lock = asyncio.Lock()
        await asyncio.gather(*(fetch_image(image_list, url, lock, session) for url in url_list))

        util.concatenate_and_save_image("img.png", image_list)
