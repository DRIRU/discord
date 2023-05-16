import discord 
from discord.ext import commands
from discord import app_commands
class ping(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Ping Loaded")
        
    @app_commands.command(name = "welcome", description="Says hi")
    async def welcome(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Hi {interaction.user.mention}", ephemeral=True)
    @app_commands.command(name = "ping", description="Shows ping")
    async def ping(self, interaction: discord.Interaction):
        latency = round(self.client.latency * 1000)
        await interaction.response.send_message(f"Pongss! {latency}ms", ephemeral = True)
    
    @app_commands.command(name="fun", description="arg")
    async def fun(self, interaction: discord.Interaction):
        arg = "helo"
        await interaction.response.send_message(f"{interaction.user.name} said {arg}", ephemeral = True)

async def setup(client: commands.Bot):
    await client.add_cog(ping(client))