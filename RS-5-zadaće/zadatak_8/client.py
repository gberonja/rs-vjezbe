import aiohttp
import asyncio

async def fetch_cat_fact(session, amount):
    url = f"http://localhost:8086/cat/{amount}"
    response = await session.get(url)
    return await response.json()

async def filter_cat_facts(session, facts):
    url = "http://localhost:8087/facts"
    response = await session.post(url, json={"facts": facts})
    return await response.json()

async def main():
    amount = 5
    
    async with aiohttp.ClientSession() as session:
        data = await fetch_cat_fact(session, amount)
        filtered_data = await filter_cat_facts(session, data['facts'])
        print(filtered_data['filtered_facts'])
        
if __name__ == '__main__':
    asyncio.run(main())