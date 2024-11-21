import asyncio

async def dohvati_podatke():
    print("Dohvaćam podatke...")
    await asyncio.sleep(3)
    data = [x for x in range(1,11)]
    print("Podaci dohvaćeni.")
    return data

async def main():
    data = await dohvati_podatke()
    print(f"Podaci: {data}")
    
asyncio.run(main())