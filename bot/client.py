import discord
from discord.ext import commands
from bot.commands import setup_commands

def get_discord_client():
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    intents.presences = True
    client = commands.Bot(command_prefix='!', intents=intents)
    
    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!')
    
    setup_commands(client)
    return client
