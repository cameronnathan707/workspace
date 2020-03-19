import discord
TOKEN = 'Your Secret Token'

client = discord.Client()

@client.event
async def on_ready():
    print("The bot is ready!")
    await client.change_presence(activity=discord.Game(name="Music"))

client.run(TOKEN)