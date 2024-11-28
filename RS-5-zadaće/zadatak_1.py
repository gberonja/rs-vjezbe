from aiohttp import web

proizvodi = [
    {"naziv": "Krumpir", "cijena": 1.3, "količina": 30},
    {"naziv": "Banana", "cijena": 2.2, "količina": 10},
    {"naziv": "Jabuka", "cijena": 1.6, "količina": 97},
]

async def get_products(request):
    return web.json_response(proizvodi) 


app = web.Application()
app.router.add_get('/proizvodi', get_products)

web.run_app(app, port=8080)