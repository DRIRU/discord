3]}")
async def main():
    async with client:
        await load()
        await client.start(TOKEN)