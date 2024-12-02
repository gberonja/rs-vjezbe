import aiohttp
import asyncio
from aiohttp import web
from aiohttp.web import AppRunner

async def get_proizvodi(request):
    proizvod_id = request.match_info.get('id')
    
    proizvodi = [
        {"id": 1, "naziv": "Laptop", "cijena": 5000},
        {"id": 2, "naziv": "Miš", "cijena": 100},
        {"id": 3, "naziv": "Tipkovnica", "cijena": 200},
        {"id": 4, "naziv": "Monitor", "cijena": 1000},
        {"id": 5, "naziv": "Slušalice", "cijena": 50}
    ]
    
    if proizvod_id is None:
        return web.json_response(proizvodi, status=200)
    
    for proizvod in proizvodi:
        if proizvod['id'] == int(proizvod_id):
            return web.json_response(proizvod, status=200)
        
    return web.json_response({'error': 'Proizvod s traženim ID-em ne postoji'}, status=404)

app = web.Application()
app.router.add_get("/proizvodi", get_proizvodi)
app.router.add_get("/proizvodi/{id}", get_proizvodi)

async def start_server():
    runner = AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8080)
    await site.start()

async def main():
    await start_server()
    
    async with aiohttp.ClientSession() as session:
        print('Klijentska sesija otvorena')
        
        print("\nTestiranje GET /proizvodi")
        rezultat_1 = await session.get("http://localhost:8080/proizvodi")
        rezultat_1_dict = await rezultat_1.json()
        print(rezultat_1_dict)

        print("\nTestiranje GET /proizvodi/2")
        rezultat_2 = await session.get("http://localhost:8080/proizvodi/2")
        rezultat_2_dict = await rezultat_2.json()
        print(rezultat_2_dict)

        print("\nTestiranje GET /proizvodi/10")
        rezultat_3 = await session.get("http://localhost:8080/proizvodi/10")
        rezultat_3_dict = await rezultat_3.json()
        print(rezultat_3_dict)

if __name__ == '__main__':
    asyncio.run(main())
