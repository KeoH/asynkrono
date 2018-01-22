
import aiohttp, asyncio, async_timeout, signal, sys

from process_html import process_page

POP_URL = 'http://www.raccoongames.es/es/productos/figuras-estatuas/funko'

LAST_PAGE = 190  # en la web pone q hay 205 paginas pero es mentira

loop = asyncio.get_event_loop()  
client = aiohttp.ClientSession(loop=loop)

async def fetch(session, page):
    print("Capturando pagina {}".format(page))

    async with session.get('{}/{}'.format(POP_URL, page)) as response:
        print("Terminado pagina {}".format(page))    
        return await process_page(await response.text())


for page in range(1, LAST_PAGE+1):
    asyncio.ensure_future(fetch(client, page))

loop.run_forever()