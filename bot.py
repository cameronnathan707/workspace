
import discord
file=open('token.txt','r')
TOKEN = file.readline()
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

    if message.content.startswith('/'):
        if message.content.startswith('/help'):
           await message.channel.send('help')

client.run(TOKEN)