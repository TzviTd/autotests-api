import asyncio

import websockets

async def client():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        message = "Hi Server! Nice to see you"
        print(f"Sending: {message}")
        await websocket.send(message) #sending message to the server

        #getting response from the server (all 5)
        for _ in range(5):
            response = await websocket.recv()
            print(response)

asyncio.run(client())