
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2021.11.03
#
# title: How to get data with websocket in a class and instantiate variable
# url: https://stackoverflow.com/questions/69817003/how-to-get-data-with-websocket-in-a-class-and-instantiate-variable/69824728#69824728

# [How to get data with websocket in a class and instantiate variable](https://stackoverflow.com/questions/69817003/how-to-get-data-with-websocket-in-a-class-and-instantiate-variable/69824728#69824728)

import asyncio
import websockets
import json

async def handler():
    async with websockets.connect('wss://ftx.com/ws/') as ws:
        
        # subscribe
        data = {'op': 'subscribe', 'channel': 'ticker', 'market': 'ETH-PERP'}
        await ws.send(json.dumps(data))

        # get all messages (not only with `update`)
        async for message in ws:
            #print(message)

            data = json.loads(message)
            
            if data['type'] == 'update':
                print(data['data']['last'])

# --- main ---
     
asyncio.get_event_loop().run_until_complete(handler())
