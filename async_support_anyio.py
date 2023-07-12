import httpx
import anyio


async def main():
    async with httpx.AsyncClient() as client:
        response = await client.get('https://www.example.com/')
        print(response)


anyio.run(main, backend='trio')
