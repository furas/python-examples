
# https://www.blockchain.com/en/api/api_websocket

import asyncio
import websockets

async def main():
    async with websockets.connect("wss://ws.blockchain.info/inv") as client:
        print("[main] Connected to wss://ws.blockchain.info/inv" )
 
        cmd = '{"op":"ping"}'
        print('[main] Send:', cmd)
        await client.send(cmd)
        response = await client.recv()
        print('[main] Recv:', response)
       
        cmd = '{"op":"blocks_sub"}'
        print('[main] Send:', cmd)
        await client.send(cmd)
        while True:
            response = await client.recv()
            print('[main] Recv:', response)
            
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

