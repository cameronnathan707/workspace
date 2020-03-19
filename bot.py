
import discord

TOKEN = 'Njg5OTg5MjQ0NjYzNjI4MDMx.XnLG2w.VloRYkz0Zx7C9Mc5yZlLZ9-kC7s'
GUILD = 'test server'

client = discord.Client()

@client.event
async def on_ready():
    print("The bot is ready!")
    await client.change_presence(activity=discord.Game(name="Music"))

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(  f'Hi {member.name}, welcome to Nathan\'s Discord server!')
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello World!')
client.run(TOKEN)