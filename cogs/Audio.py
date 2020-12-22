import discord
from discord.ext import commands
from discord.utils import get
import urllib.parse, urllib.request, re

class Audio(commands.Cog):

    def __init__(self, danybot):
        self.danybot = danybot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Audio.py is loaded.')

    @commands.command(aliases=['play'])
    async def yt(self, ctx, *, search):

        query_string = urllib.parse.urlencode({'search_query': search})
        htm_content = urllib.request.urlopen(
            'http://www.youtube.com/results?' + query_string)
        search_results = re.findall(r'/watch\?v=(.{11})',
                                    htm_content.read().decode())
        await ctx.send('http://www.youtube.com/watch?v=' + search_results[0])
        await ctx.send('Currently setting up the ability to play music in voice chat, hang tight!')

def setup(danybot):
    danybot.add_cog(Audio(danybot))
