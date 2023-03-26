import asyncio, telnetlib

async def handle_echo(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    while True:
        data = await reader.readline()
        message = data.decode()
        addr = writer.get_extra_info('peername')

        if message == "exit\n":
            message = "Goodbye!"
            print(f"Send: {message!r}")
            writer.write(data)
            await writer.drain()
            print("Close the connection")
            writer.close()
            await writer.wait_closed()
            break
        else:
            print(f"Received {message!r} from {addr!r}")

            print(f"Send: {message!r}")
            writer.write(data)
            await writer.drain()
    

async def main():
    server = await asyncio.start_server(
        handle_echo, 'localhost', telnetlib.TELNET_PORT)

    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addrs}')

    async with server:
        await server.serve_forever()

asyncio.run(main())