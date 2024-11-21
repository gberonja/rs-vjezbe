import asyncio
import random

async def provjeri_parnost(broj):
    await asyncio.sleep(2)
    return f"Broj {broj} je paran." if broj % 2 == 0 else f"Broj {broj} je neparan."

async def main():
    lista_brojeva = [random.randint(1,100) for _ in range(10)]
    zadaci = [provjeri_parnost(broj) for broj in lista_brojeva]
    rezultati = await asyncio.gather(*zadaci)
    print(rezultati)

asyncio.run(main())