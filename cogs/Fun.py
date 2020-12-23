import discord
import random
import nekos
from discord.ext import commands

class Fun(commands.Cog):
    def __init__(self, danybot):
        self.danybot = danybot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Fun.py is loaded.')


    @commands.command(aliases=['8ball'])
    async def eightball(self, ctx, *, question):
        responses = [
        "It is certain",
        "Without a doubt",
        "You may rely on it",
        "Yes definitely",
        "It is decidedly so",
        "As I see it, yes",
        "Most likely",
        "Yes",
        "Outlook good",
        "Signs point to yes",
        "Reply hazy try again",
        "Better not tell you now",
        "Ask again later",
        "Cannot predict now",
        "Concentrate and ask again",
        "Don't count on it",
        "Outlook not so good",
        "My sources say no",
        "Very doubtful",
        "My reply is no"]
        await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")

    @commands.command()
    async def cat(self, ctx):
        await ctx.send(nekos.cat())


def setup(danybot):
    danybot.add_cog(Fun(danybot))
