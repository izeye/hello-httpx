import asyncio
import httpx

from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.routing import Route


async def hello(request):
    print(request)
    return HTMLResponse("Hello World!")


app = Starlette(routes=[Route("/", hello)])


async def main():
    async with httpx.AsyncClient(app=app, base_url="http://testserver") as client:
        r = await client.get("/")
        print(r)
        print(r.text)
        assert r.status_code == 200
        assert r.text == "Hello World!"


asyncio.run(main())
