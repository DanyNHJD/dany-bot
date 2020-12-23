import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

# Load token from .env file and set as variable
load_dotenv()
Token = os.getenv('DANYBOT_TOKEN')
OwnerID = int(os.getenv('DANY_ID'))

# Sets prefix for bot
danybot = commands.Bot(command_prefix = commands.when_mentioned_or('d!'))

# Other Variables
cogs_path = './cogs'
CogsToString = ' '.join([str(elem) for elem in os.listdir(cogs_path)])
NoCogError = 'You need to give me a cog! Current cogs avalable are: ' + CogsToString.strip('__pycache__')

# Loads up cogs (allow putting commands on other files)
@danybot.command(hidden=True)
async def load(ctx, extension=None):
    if extension == None:
        return await ctx.send(NoCogError)
    danybot.load_extension(f'cogs.{extension}')
    await ctx.send(f'Loaded {extension}.')

@danybot.command(hidden=True)
async def unload(ctx, extension=None):
    if extension == None:
        return await ctx.send(NoCogError)
    danybot.unload_extension(f'cogs.{extension}')
    await ctx.send(f'Unloaded {extension}.')

@danybot.command(hidden=True)
async def reload(ctx, extension=None):
    if extension == None:
        return await ctx.send(NoCogError)
    danybot.unload_extension(f'cogs.{extension}')
    danybot.load_extension(f'cogs.{extension}')
    await ctx.send(f'Reloaded {extension}.')

# Looks up cogs on the cogs directory, then loads them.
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        danybot.load_extension(f'cogs.{filename[:-3]}')

# Prints if ready
@danybot.event
async def on_ready():
    await danybot.change_presence(status=discord.Status.online,
    activity=discord.Activity(type=discord.ActivityType.playing,
    name="with nekos | d!help"))
    print("DanyBot is now ready.")

#Ping test command
@danybot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(danybot.latency * 1000)}ms')

danybot.run(Token)
