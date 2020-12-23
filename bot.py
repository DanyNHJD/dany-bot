import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

#Load token from .env file and set as variable
load_dotenv()
TOKEN = os.getenv('DANYBOT_TOKEN')

#Sets prefix for bot
danybot = commands.Bot(command_prefix = 'd!')

#Loads up cogs (allow putting commands on other files)
@danybot.command()
async def load(ctx, extension):
    danybot.load_extension(f'cogs.{extension}')
    await ctx.send(f'Loaded {extension}.')

@danybot.command()
async def unload(ctx, extension):
    danybot.unload_extension(f'cogs.{extension}')
    await ctx.send(f'Unloaded {extension}.')

@danybot.command()
async def reload(ctx, extension):
    danybot.unload_extension(f'cogs.{extension}')
    danybot.load_extension(f'cogs.{extension}')
    await ctx.send(f'Reloaded {extension}.')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        danybot.load_extension(f'cogs.{filename[:-3]}')

@danybot.event
async def on_ready():
    print("DanyBot is now ready.")

#Ping test command
@danybot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(danybot.latency * 1000)}ms')

danybot.run(TOKEN)
