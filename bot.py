import discord
import responses
async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)
def run_bot():
    TOKEN = 'OTM0NTE1NDMyNDQwODg5MzU0.GOdpM4.KYDlBZPSRgfHR3bfK84UGVMIvvJL8Z1WY4edQw'
    client = discord.Client(intents=discord.Intents.default())
    @client.event
    async def on_ready():
        print(f'{client.user} is running')
    @client.event
    async def on_message(message):
        
    client.run(TOKEN)