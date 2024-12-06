from aiohttp import web
from math import prod

async def handle_product(request):
    data = await request.json()
    brojevi = data.get("brojevi")
    if not isinstance(data.get("brojevi"), list):
        return web.json_response({"error": "Ulazni podatak mora biti lista s brojevima"}, status=200)
    
    umnozak = prod(brojevi)
    return web.json_response({"umnozak": umnozak})

app = web.Application()
app.router.add_post('/umnozak', handle_product)

if __name__ == '__main__':
    web.run_app(app, port=8084)