import aiohttp
import asyncio

async def get_dog_fact(session):
    url = "https://dogapi.dog/api/v2/facts"
    response = await session.get(url)
    data = await response.json()
    return data['data'][0]["attributes"]['body']
    
async def get_cat_fact(session):
    url = "https://catfact.ninja/fact"
    response = await session.get(url)
    data = await response.json()
    return data['fact']

async def mix_facts(dog_facts, cat_facts):
    nova_lista = [dog_fact if len(dog_fact)>len(cat_fact) else cat_fact for dog_fact, cat_fact in zip(dog_facts,cat_facts)]
    return nova_lista
    
async def main():
    async with aiohttp.ClientSession() as session:
        dog_facts_tasks = [get_dog_fact(session) for _ in range(5)]
        cat_facts_tasks = [get_cat_fact(session) for _ in range(5)]
        
        all_facts = await asyncio.gather(*dog_facts_tasks, *cat_facts_tasks)
        
        dog_facts = all_facts[:5]
        cat_facts = all_facts[5:]
        
        rezultat = await mix_facts(dog_facts,cat_facts)
        print("Mixane činjenice o psima i mačkama:")
        for fact in rezultat:
            print(fact)
    
asyncio.run(main())