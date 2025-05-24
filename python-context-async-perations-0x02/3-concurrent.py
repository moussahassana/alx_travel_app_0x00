import aiosqlite
import asyncio

async def async_fetch_users():
    return await _async_fetch_users()

async def _async_fetch_users(query="SELECT * FROM users", params=None):
    async with aiosqlite.connect("users.db") as conn:
        async with conn.execute(query, params or ()) as cursor:
            results = await cursor.fetchall()
            return results

async def async_fetch_older_users():
    query = "SELECT * FROM users WHERE age > ?"
    params = (40,)
    results = await _async_fetch_users(query, params)
    return results

async def fetch_concurrently():
    users, older_users = await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )
    print("All users:", users)
    print("Users older than 40:", older_users)

asyncio.run(fetch_concurrently())
