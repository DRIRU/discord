import discord 
from discord.ext import commands
from discord import app_commands

class Manage(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Manage Loaded")
    @commands.command()
    async def shutdown(self, ctx):
        await ctx.send("Shutting Down")
        await self.client.close()
    @commands.command()
    async def load(self, ctx, cogName: str):
        try:
            await self.client.load_extension(f"cogs.{cogName}")
        except Exception as e:
            await ctx.send("Loading cog failed")
            return
        await ctx.send("Cog loaded")
    @commands.command()
    async def reload(self, ctx, cogName: str):
        try:
            await self.client.reload_extension(f"cogs.{cogName}")
        except Exception as e:
            await ctx.send("Reoading cog failed")
            return
        await ctx.send("Cog Reloaded")
    @commands.command()
    async def unload(self, ctx, cogName: str):
        try:
            await self.client.unload_extension(f"cogs.{cogName}")
        except Exception as e:
            await ctx.send("Coudld not unload the cog")
            return
        await ctx.send("Cog Unloaded")
    

async def setup(client: commands.Bot):
    await client.add_cog(Manage(client))