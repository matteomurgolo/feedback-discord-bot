import discord
from discord.ext import commands
from utils.image_generator import generate_message_image

def setup_commands(bot):
    @bot.command(name='convert')
    async def convert(ctx, message_link: str):
        try:
            channel_id, message_id = message_link.split('/')[-2:]
            channel = bot.get_channel(int(channel_id))
            target_message = await channel.fetch_message(int(message_id))
            
            image_path = generate_message_image(target_message)
            
            await ctx.send(file=discord.File(image_path))
        except Exception as e:
            await ctx.send(f"Une erreur s'est produite : {str(e)}")

    @bot.command(name='ping')
    async def ping(ctx):
        await ctx.send('Pong!')
