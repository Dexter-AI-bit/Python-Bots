import discord
from discord.ext import commands

class Greetings(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        await ctx.send('Hello, I am BMO')

    @commands.command()
    async def goodbye(self, ctx):
        await ctx.send('Goodbye, See you later!')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = discord.utils.get(member.guild.text_channels, name='general')
        if channel:
            await channel.send(f'Welcome to the server, {member.mention}!')

def setup(bot):
    bot.add_cog(Greetings(bot))