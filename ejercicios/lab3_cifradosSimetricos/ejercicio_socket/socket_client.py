import asyncio
import websockets

def get_input():
	return input()

async def hello():
	# Connect to the WebSocket server
	uri = "ws://192.168.56.1:9443"
	async with websockets.connect(uri) as websocket:
		while True:
			# Get input asynchronously by running input() in an executor
			in_val = await asyncio.get_event_loop().run_in_executor(None, get_input)
			await websocket.send(in_val)

			response = await websocket.recv()
			print(f"Received from server: {response}")

if __name__ == "__main__":
	asyncio.run(hello())