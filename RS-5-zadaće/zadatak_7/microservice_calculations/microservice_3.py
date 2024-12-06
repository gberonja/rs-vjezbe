from aiohttp import web

async def handle_quotient(request):
    data = await request.json()
    
    zbroj = data["zbroj"]
    umnozak = float(data["umnozak"])
    
    if zbroj == 0:
        return web.json_response({"greška": "Ne može se dijeliti s nulom"}, status=400)
    print(zbroj, type(zbroj))
    print(umnozak, type(umnozak))
    
    
    kolicnik = umnozak / zbroj
    return web.json_response({"kolicnik": kolicnik})
    
app = web.Application()
app.router.add_post("/kolicnik", handle_quotient)

if __name__ == "__main__":
    web.run_app(app, port=8085)