import aiohttp
import asyncio

async def get_cat_fact(session):
    url = "https://catfact.ninja/fact"
    response = await session.get(url)
    data = await response.json()
    return data['fact']

async def filter_cat_facts(cat_list):
    filtered_facts = [fact for fact in cat_list if "cat" in fact.lower() or "cats" in fact.lower()]
    return filtered_facts

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [get_cat_fact(session) for _ in range(20)]
        cat_facts = await asyncio.gather(*tasks)
        
        filtered_facts = await filter_cat_facts(cat_facts)
        
        print("Filtirane činjenice o mačkama:")
        for fact in filtered_facts:
            print(f"- {fact}")

    
asyncio.run(main())