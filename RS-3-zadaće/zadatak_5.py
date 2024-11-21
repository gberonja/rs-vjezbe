import asyncio

async def secure_data(podaci_osoba):
    await asyncio.sleep(3)
    return {
        'prezime': podaci_osoba['prezime'],
        'broj_kartice': hash(podaci_osoba['broj_kartice']),
        'CVV': hash(podaci_osoba['CVV'])}

async def main():
    osjetljivi_podaci = [
    {'prezime': 'Ivić', 'broj_kartice': '1234 5678 9101 1121', 'CVV': '123'},
    {'prezime': 'Marković', 'broj_kartice': '2234 6789 0123 4567', 'CVV': '456'},
    {'prezime': 'Jurić', 'broj_kartice': '3234 7890 1234 5678', 'CVV': '789'}
]   
    zadaci = [secure_data(osoba) for osoba in osjetljivi_podaci]
    ispis = await asyncio.gather(*zadaci)
    print(ispis)
    
asyncio.run(main())