import asyncio
import websockets
from websockets import ServerConnection

#request-response
async def echo(websocket: ServerConnection):
    async for message in websocket:
        print(f"Received message: {message}")
        for i in range(5):
            response = f"{i + 1} Server has got a message: {message}"
            await websocket.send(response)

#launching the server
async def main():
    server = await websockets.serve(echo, "localhost", 8765)
    print("The server is launched on ws://localhost:8765")
    await server.wait_closed()

asyncio.run(main())