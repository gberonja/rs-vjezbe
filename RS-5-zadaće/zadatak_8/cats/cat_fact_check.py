from aiohttp import web

async def handle_cat_fact_check(request):
    data = await request.json()
    filtered_facts = [fact for fact in data["facts"] if "cat" in fact.lower()]
    return web.json_response({"filtered_facts": filtered_facts})
    
app = web.Application()
app.router.add_post("/facts", handle_cat_fact_check)

if __name__ == "__main__":
    web.run_app(app,port=8087)