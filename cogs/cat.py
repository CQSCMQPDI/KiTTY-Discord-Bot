import asyncio
import nekos
import discord
from discord.ext import commands
import aiohttp

class cat:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def cat(self):
        """Send a random cat picture on the channel"""
        cats = nekos.cat()
        await self.bot.say(cats)

    @commands.command()
    async def why(self):
    	"""Why the xbox live is better than psn ?"""
    	why = nekos.why()
    	await self.bot.say(why)

    @commands.command()
    async def fact(self):
    	"""The biggest cat in the world is Maine Coon, this cat weight 25kg"""
    	facts = nekos.fact()
    	embed=discord.Embed(color=0x717171)
    	embed.add_field(name="KiTTY/Deo", value=facts, inline=False)
    	await self.bot.say(embed=embed)

def setup(bot):
    bot.add_cog(cat(bot))