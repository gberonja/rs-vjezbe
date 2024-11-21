import asyncio

async def dohvati_korisnike():
    print("Dohvaćam podatke o korisnicima...")
    await asyncio.sleep(3)
    korisnici = [
        {'ime': 'Ante', 'dob': 31},
        {'ime': 'Luka', 'dob': 23},
        {'ime': 'Marko', 'dob': 19}
    ]
    print("Podaci o korisnicima dohvaćeni.")
    return korisnici

async def dohvati_proizvode():
    print("Dohvaćam podatke o korisnicima...")
    await asyncio.sleep(5)
    proizvodi = [
        {'naziv': 'Lampa', 'cijena': 20},
        {'naziv': 'Laptop', 'cijena': 700},
        {'naziv': 'Zvučnici', 'cijena': 100}
    ]
    print("Podaci o proizvodima dohvaćeni.")
    return proizvodi

async def main():
    korisnici, proizvodi = await asyncio.gather(dohvati_korisnike(),dohvati_proizvode())
    print(f"Podaci o korisnicima: {korisnici}")
    print(f"Podaci o proizvodima: {proizvodi}")
    
asyncio.run(main())