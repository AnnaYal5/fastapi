import aiohttp
import asyncio
import aiomysql
import json


async def get_users_from_api():
    url = "https://jsonplaceholder.typicode.com/users"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                users = await response.json()
                return users
            else:
                print(f"Error: {response.status}")
                return []