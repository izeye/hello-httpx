import asyncio
import httpx


async def get():
    async with httpx.AsyncClient() as client:
        async_result = client.get('https://www.example.com/')
        print(async_result)
        print(type(async_result))
        result = await async_result
        print(result)
        print(type(result))
        print(result.text)


asyncio.run(get())
