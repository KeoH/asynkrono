
import aiohttp, asyncio, async_timeout

POP_URL = 'http://www.raccoongames.es/es/productos/figuras-estatuas/funko'

LAST_PAGE = 190  # en la web pone q hay 205 paginas pero es mentira

async def fetch(session, page):
    print("Capturando pagina {}".format(page))
    with async_timeout.timeout(10):
        async with session.get('{}/{}'.format(POP_URL, page)) as response:
            print("Terminado pagina {}".format(page)) 
            return await response.text()


async def main():
    async with aiohttp.ClientSession() as session:
        for page in range(1, LAST_PAGE+1):
            await fetch(session, page)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())