import discord
import datetime
from discord.ext import commands
from discord import app_commands
class Info(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print("user cog loaded")
    @commands.command()
    async def userinfo(self, ctx):
        user = ctx.message.author
        embed = discord.Embed(title = "User Information", description = "Information of user", timestamp=datetime.datetime.utcnow())
        embed.set_thumbnail(url=user.avatar)
        embed.add_field(name = "Id", value = user.id)
        embed.add_field(name = "Name", value = f"{user.name}#{user.discriminator}")
        embed.add_field(name = "Nick Name", value = user.display_name)
        await ctx.send(embed = embed)
    @app_commands.command(name = "uinfo", description="shows information")
    async def userInfo(self, interaction: discord.Interaction, user: discord.Member= None):
        if user == None:
            user = interaction.user
        embed = discord.Embed(title = "User Information", description = f"Information of {user.mention}", timestamp=datetime.datetime.now())
        embed.set_thumbnail(url=user.avatar)
        embed.add_field(name = "Id", value = user.id)
        embed.add_field(name = "Name", value = f"{user.name}#{user.discriminator}")
        embed.add_field(name = "Nick Name", value = user.display_name)
        embed.add_field(name = "Created on", value = user.created_at.strftime("%A %d %b %Y, %I:%M %p"))
        embed.add_field(name = "Joined on", value = user.joined_at.strftime("%A %d %b %Y, %I:%M %p"))
        await interaction.response.send_message(embed = embed)

    @app_commands.command(name = "serverinfo", description="shows server information")
    async def serverInfo(self, interaction: discord.Interaction):
        embed = discord.Embed(title = "Server Information", description = f"Information of {interaction.guild.name}", timestamp=datetime.datetime.now())
        embed.set_thumbnail(url = interaction.guild.icon)
        embed.add_field(name = "Id", value = interaction.guild.id)
        embed.add_field(name = "Name", value = interaction.guild.name)
        embed.add_field(name = "Owner", value = interaction.guild.owner.mention)
        embed.add_field(name = "Members", value = len(interaction.guild.members))
        embed.add_field(name = "Channels", value = f"{len(interaction.guild.text_channels)} Text | {len(interaction.guild.voice_channels)} Voice")
        embed.add_field(name = "Created on", value = interaction.guild.created_at.strftime("%A %d %b %Y, %I:%M %p"))
        await interaction.response.send_message(embed = embed)

async def setup(client: commands.Bot):
    await  client.add_cog(Info(client))
