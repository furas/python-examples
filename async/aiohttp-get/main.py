import aiohttp
import asyncio
import json

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main(urls):
    tasks = []
    results = []
    async with aiohttp.ClientSession() as session:
        for url in urls:
            tasks.append(fetch(session, url))
        results = await asyncio.gather(*tasks)
    return results

def parallel(urls):
    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(main(urls))
    return results

# --- main ---

urls = [
    #('https://stackoverflow.com/', 1), # wrong 
    'https://stackoverflow.com/', # wrong 
    'https://httpbin.org/',
    'http://toscrape.com/',
]

result = parallel(urls)

for item in result:
    print(item[:300])
    print('-----')


