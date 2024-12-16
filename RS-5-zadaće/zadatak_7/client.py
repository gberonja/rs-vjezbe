import aiohttp
import asyncio

async def fetch_sum_data(session, data_json):
    response = await session.post('http://localhost:8083/zbroj', json=data_json)
    return await response.json()

async def fetch_product_data(session, data_json):
    response = await session.post('http://localhost:8084/umnozak', json=data_json)
    return await response.json()

async def fetch_kolicnik_data(session, data_json):
    response = await session.post('http://localhost:8085/kolicnik', json=data_json)
    return await response.json()

async def main():
    data = [i for i in range(1,15)]
    data_json = {'brojevi': data}
    
    async with aiohttp.ClientSession() as session:
        # Konkuretno prva dva microservice-a
        sum_task = fetch_sum_data(session, data_json)
        product_task = fetch_product_data(session, data_json)
        microservice_sum_data, microservice_product_data = await asyncio.gather(sum_task, product_task)
    
        combined_data =  {
            "zbroj": microservice_sum_data.get('zbroj'),
            "umnozak": microservice_product_data.get('umnozak')
        }
            
            # Sekvencijalno treći microservice
        microservice_quotient_data = await fetch_kolicnik_data(session, combined_data)
        quotient = microservice_quotient_data.get('kolicnik')
        
        print(f"Zbroj brojeva: {combined_data["zbroj"]}")
        print(f"Umnožak brojeva: {combined_data["umnozak"]}")
        print(f"Količnik umnoška i zbroja: {quotient}")
    
asyncio.run(main())
        
