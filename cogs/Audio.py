import discord
import youtube_dl
import os
import asyncio
from discord.ext import commands
from discord.utils import get
from discord.voice_client import VoiceClient
from discord.ext.commands import Bot
import urllib.parse, urllib.request, re
from discord import FFmpegPCMAudio
from os import system

# Configure settings for youtube-dl
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

def endSong(guild, path):
    os.remove(path)


class Audio(commands.Cog):

    def __init__(self, danybot):
        self.danybot = danybot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Audio.py is loaded.')

    @commands.command(aliases=['yt'], brief="Play music from youtube in a voice channel.")
    async def play(self, ctx, *, search=None):
        if not ctx.message.author.voice:
            return await ctx.send(f'You need to join a voice chat {ctx.author.mention}!')
        if search == None:
            return await ctx.send(f'{ctx.author.mention}, Please type in a video name / URL.')

        channel = ctx.message.author.voice.channel
        voice_client = await channel.connect()
        guild = ctx.message.guild
        # Look for song then save it to the url variable
        query_string = urllib.parse.urlencode({'search_query': search})
        htm_content = urllib.request.urlopen(
            'http://www.youtube.com/results?' + query_string)
        search_results = re.findall(r'/watch\?v=(.{11})',
                                    htm_content.read().decode())
        url = 'http://www.youtube.com/watch?v=' + search_results[0]

        print(url)
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            file = ydl.extract_info(url, download=True)
            path = str(file['title']) + "-" + str(file['id'] + ".mp3")

        voice_client.play(discord.FFmpegPCMAudio(path), after=lambda x: endSong(guild, path))
        voice_client.source = discord.PCMVolumeTransformer(voice_client.source, 1)

        await ctx.send(f'**Music: **{url}')

        while voice_client.is_playing():
            await asyncio.sleep(1)
        else:
            await voice_client.disconnect()
            print(f'Disconnected from {ctx.guild.name}')


def setup(danybot):
    danybot.add_cog(Audio(danybot))
