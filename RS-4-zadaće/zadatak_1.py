import aiohttp
import asyncio
import time

async def fetch_users(session):
    url = "https://jsonplaceholder.typicode.com/users"
    response = await session.get(url)
    return await response.json()

async def main():
    start = time.time()
    
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_users(session) for _ in range(5)]
        responses = await asyncio.gather(*tasks)
        
    names = [user['name'] for user in responses[0]]
    emails = [user['email'] for user in responses[0]]
    username = [user['username'] for user in responses[0]]
    
    end = time.time()
    
    print('Imena:', names)
    
    print(f"Potrebno vrijeme: {end- start:.2f} sekundi")
    
asyncio.run(main())