from aioconsole import get_standard_streams
import asyncio

async def main():
    reader, writer = await get_standard_streams()
    while True:
        res = await reader.readline()
        if not res:
            break
        writer.write(res)

if __name__ == "__main__":
    asyncio.run(main())