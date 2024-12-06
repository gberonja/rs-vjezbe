import aiohttp
import asyncio

async def main():
    async with aiohttp.ClientSession() as session:
        # Sekvencijalno
        microservice_1 = await session.get('http://localhost:8081/pozdrav')
        microservice_1_json = await microservice_1.json()
        print(microservice_1_json['message'])
        
        microservice_2 = await session.get('http://localhost:8082/pozdrav')
        microservice_2_json = await microservice_2.json()
        print(microservice_2_json['message'])
        
        # Konkurentsko
        tasks = [
            session.get('http://localhost:8081/pozdrav'),
            session.get('http://localhost:8082/pozdrav')
        ]
        
        results = await asyncio.gather(*tasks)
        responses_json = [await result.json() for result in results]
        
        for response in responses_json:
            print(response['message'])
        

asyncio.run(main())