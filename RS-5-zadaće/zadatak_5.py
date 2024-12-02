import aiohttp, asyncio
from aiohttp import web
from aiohttp.web import AppRunner

proizvodi = [
    {"id": 1, "naziv": "Laptop", "cijena": 5000},
    {"id": 2, "naziv": "Miš", "cijena": 100},
    {"id": 3, "naziv": "Tipkovnica", "cijena": 200},
    {"id": 4, "naziv": "Monitor", "cijena": 1000},
    {"id": 5, "naziv": "Slušalice", "cijena": 50}
]

lista_narudzbi = []


async def get_proizvodi(request):
    proizvod_id = request.match_info.get('id')

    if proizvod_id is None:
        return web.json_response(proizvodi, status=200)
    
    for proizvod in proizvodi:
        if proizvod['id'] == int(proizvod_id):
            return web.json_response(proizvod, status=200)
        
    return web.json_response({'error': 'Proizvod s traženim ID-em ne postoji'}, status=404)

async def add_narudzba(request):
    data = await request.json()
    proizvod_id = data.get('proizvod_id')
    kolicina = data.get('kolicina', 1)

    p = None
    for proizvod in proizvodi:
        if proizvod['id'] == int(proizvod_id):
            p = proizvod
            break
    if not p:
        return web.json_response({'error': 'Proizvod s traženim ID-em ne postoji'}, status=404)

    for narudzba in lista_narudzbi:
        if narudzba['proizvod_id'] == int(proizvod_id):
            narudzba['kolicina'] += int(kolicina)
            break
    else:
        nova_narudzba = {
            'proizvod_id': int(proizvod_id),
            'kolicina': int(kolicina)
        }
        lista_narudzbi.append(nova_narudzba)

    return web.json_response({'lista_narudzbi': lista_narudzbi}, status=200)

    

app = web.Application()
app.router.add_routes([
    web.get('/proizvodi', get_proizvodi),
    web.get('/proizvodi/{id}', get_proizvodi),
    web.post('/narudzbe', add_narudzba)
])

async def start_server():
    runner = AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8080)
    await site.start()
    print("Poslužitelj sluša na http://localhost:8080")

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

        print("\nTestiranje POST /narudzbe (proizvod 2, količina 3)")
        rezultat_4 = await session.post("http://localhost:8080/narudzbe", json={"proizvod_id": 2, "kolicina": 3})
        rezultat_4_dict = await rezultat_4.json()
        print(rezultat_4_dict)

        print("\nTestiranje POST /narudzbe (proizvod 10, nepostojeći ID)")
        rezultat_5 = await session.post("http://localhost:8080/narudzbe", json={"proizvod_id": 10, "kolicina": 1})
        rezultat_5_dict = await rezultat_5.json()
        print(rezultat_5_dict)

        print("\nTestiranje POST /narudzbe (ažuriranje kolicine: proizvod 2, dodavanje količine 2)")
        rezultat_6 = await session.post("http://localhost:8080/narudzbe", json={"proizvod_id": 2, "kolicina": 2})
        rezultat_6_dict = await rezultat_6.json()
        print(rezultat_6_dict)

if __name__ == '__main__':
    asyncio.run(main())