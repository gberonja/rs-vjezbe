from aiohttp import web
from asyncio import sleep

async def handle_service1(request):
    await sleep(3)
    return web.json_response({"message": "Pozdrav nakon 3 sekunde"})

app = web.Application()
app.router.add_get('/pozdrav', handle_service1)

if __name__ == '__main__':
    web.run_app(app, port=8081)