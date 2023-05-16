url = 'https://discord.com/api/oauth2/authorize?client_id=1106998803015417887&permissions=8&scope=bot'
import discord 
from discord import app_commands
import asyncio
from discord.ext import commands
import os
TOKEN = ''
intents = discord.Intents.default() 
intents.message_content = True 
client = commands.Bot(command_prefix="!", intents=intents)

async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith('.py'):
            await client.load_extension(f"cogs.{filename[:-3]}")
async def main():
    async with client:
        await load()
        await client.start(TOKEN)

@client.command()
async def sync(ctx):
    await client.tree.sync()
    await ctx.send("Synced")
@client.event
async def on_ready():
    print("Logged in")
    await client.tree.sync()

asyncio.run(main())
