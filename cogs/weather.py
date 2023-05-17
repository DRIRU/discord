import discord 
from discord.ext import commands
from discord import app_commands
import aiohttp
import datetime
class Weather(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print("Weather cog Loaded")
    
    @app_commands.command(name="weather", description="shows weather")
    async def weather(self, interaction: discord.Interaction, city: str):
        url = "http://api.weatherapi.com/v1/current.json"
        API_KEY = ""
        params = {
            "key":API_KEY,
            "q": city,
        }
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as response:
                data = await response.json()
                location = data["location"]["name"]
                temp_c, temp_f = data["current"]["temp_c"], data["current"]["temp_f"]
                feelslike_c, feelslike_f =  data["current"]["feelslike_c"], data["current"]["feelslike_f"]
                condition = data["current"]["condition"]["text"]
                wind_mph, wind_kph = data["current"]["wind_mph"], data["current"]["wind_kph"]
                vis_km, vis_miles = data["current"]["vis_km"], data["current"]["vis_miles"]
                humidity =  data["current"]["humidity"]
                precip_mm, precip_in = data["current"]["precip_mm"], data["current"]["precip_in"]
                time = datetime.datetime.strptime(data["current"]["last_updated"], "%Y-%m-%d %H:%M")
                img_url = "http:"+data["current"]["condition"]["icon"]
                embed = discord.Embed(title=f"Weather for {location}", description=f"{location} is {condition} today", timestamp = time)
                embed.add_field(name="Temperature", value = f"C: {temp_c} | F:{temp_f}")
                embed.add_field(name="Feels Like", value = f"C: {feelslike_c} | F:{feelslike_f}")
                embed.add_field(name="Wind Speed", value=f"{wind_kph} Km/h | {wind_mph} M/h")
                embed.add_field(name="Visibility", value=f"{vis_km} Km | {vis_miles} Miles")
                embed.add_field(name="Precipitation", value=f"{precip_in} in | {precip_mm} mm")
                embed.add_field(name="Humidity", value=f"{humidity}%")
                embed.set_thumbnail(url=img_url)
                await interaction.response.send_message(embed=embed)
async def setup(client: commands.Bot):
    await client.add_cog(Weather(client))
