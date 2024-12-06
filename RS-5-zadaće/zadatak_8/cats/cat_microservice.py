from aiohttp import web
import aiohttp
import asyncio

async def handle_cat_facts(request):
    async with aiohttp.ClientSession() as session:
        response = await session.get('https://catfact.ninja/facts')
        data = await response.json()
        facts = [item["fact"] for item in data.get("data", [])]
        return web.json_response({"facts": facts})

async def handle_cat_fact(request):
    fact_amount = int(request.match_info.get('amount', 1))
    facts = []
    
    async with aiohttp.ClientSession() as session:
        for _ in range(fact_amount):
            response = await session.get("https://catfact.ninja/fact")
            data = await response.json()
            facts.append(data["fact"])
    
    return web.json_response({"facts": facts})

app = web.Application()
app.router.add_get('/cats', handle_cat_facts)
app.router.add_get('/cat/{amount}', handle_cat_fact)

if __name__ == "__main__":
    web.run_app(app, port=8086)
        

