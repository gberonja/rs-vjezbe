from aiohttp import web

async def handle_sum(request):
    data = await request.json()
    if not isinstance(data.get("brojevi"),list):
        return web.json_response({"error": "Ulazni podatak mora biti lista s brojevima"}, status=400)
    zbroj = sum(data["brojevi"]) 
    return web.json_response({"zbroj": zbroj})

app = web.Application()
app.router.add_post('/zbroj', handle_sum)

if __name__ == '__main__':
    web.run_app(app, port=8083)