import discord
from discord.ext import commands

class Admin(commands.Cog):

    def __init__(self, danybot):
        self.danybot = danybot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Admin.py is loaded.')

    @commands.command()
    async def clear(self, ctx, amount=5):
        clear_messages = int(amount)
        await ctx.channel.purge(limit=clear_messages+1)

    #@commands.command()
    #async def status(self, ctx, status=None):
        #status_str = str(status)
        #if status_str != 'online' or 'idle' or 'offline' or 'dnd':
            #return await ctx.send(f'Please set a status to change! [online, idle, dnd, offline]')
        #await danybot.change_presence(f'status=discord.Status.{status_str}')

    @commands.command()
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'Kicked {member.mention}')

    @commands.command()
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention}')

    @commands.command()
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
                return

def setup(danybot):
    danybot.add_cog(Admin(danybot))
