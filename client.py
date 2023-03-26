import asyncio, telnetlib, sys
from aioconsole import get_standard_streams


async def tcp_echo_client():
    tcp_reader, tcp_writer = await asyncio.open_connection(
        'localhost', telnetlib.TELNET_PORT)

    std_reader, std_writer = await get_standard_streams()
    print("all connected")
    message = ""
    while message!= "exit\n".encode():
        message = await std_reader.readline()

        tcp_writer.write(message)
        await tcp_writer.drain()

        data = await tcp_reader.read(100)
        print(f'Received: {data.decode()!r}')
        std_writer.write(data)

    print('Close the connection')
    tcp_writer.close()
    await tcp_writer.wait_closed()
    std_writer.close() 
    await std_writer.wait_closed()

asyncio.run(tcp_echo_client())