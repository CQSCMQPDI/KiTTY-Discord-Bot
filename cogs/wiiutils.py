import asyncio
import requests
import discord
from __main__ import send_cmd_help
from discord.ext import commands
import aiohttp
import json

class wiiutils:

    def __init__(self, bot):
        self.bot = bot
        self.session = self.bot.http.session

    @commands.group(pass_context=True)
    async def wii(self, ctx):
    	if ctx.invoked_subcommand is None:
    		await send_cmd_help(ctx)

    @commands.command(pass_context=True)
    async def wiimmfi(self, ctx):
    	"""Does Wiimmfi servers are down ?"""
    	query = ("https://wiimmfi.glitch.me/mkw/amount")
    	page = requests.get(query).json()
    	user = page["available"]
    	numberuser = user["players"]
    	status = page["status"]
    	#Saying if Wiimmfi is online or no !
    	if status == 200:
    		online = "Yes"
    	else:
    		online = "No"

    	embed=discord.Embed(title="wiimmfi server status", color=0xff0000)
    	embed.set_thumbnail(url="https://i.imgur.com/SVcS7lE.png")
    	embed.add_field(name="Players :", value=numberuser, inline=True)
    	embed.add_field(name="Online ?", value=online, inline=True)
    	await self.bot.say(embed=embed)

    @wii.command(pass_context=True)
    async def homebrew(self, ctx):
        """You want to homebrew your Wii ?"""
        homebrewfr = "https://katolo.gy/2018/10/03/softmod-sa-wii/"
        homebrewen = "https://sites.google.com/site/completesg/"
        await self.bot.say(homebrewfr + "\n" + homebrewen)

def setup(bot):
    bot.add_cog(wiiutils(bot))

