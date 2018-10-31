import asyncio
import discord
from discord.ext import commands
import aiohttp
import asyncio
import random
import os
import speedtest
import requests
from bs4 import BeautifulSoup

class text:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def invite(self):
        """need nekos api for python"""
        embed=discord.Embed(title="Invite a cat !", url='https://bit.ly/2LoyicC', color=0xff0000)
        embed.add_field(name="Hey! Thanks for inviting me over! Click on 'Invite a cat' to start the adventure!", value=":cat:", inline=False)
        await self.bot.say(embed=embed)

    @commands.command()
    async def speedtest(self):
        loader = await self.bot.say("Testing the most efficient server for connection testing !")
        s = speedtest.Speedtest()
        s.get_best_server()
        await self.bot.edit_message(loader, "I measure the download speed ! :cat:")
        s.download()
        await self.bot.edit_message(loader, "I measure the upload speed ! :cat:")
        s.upload()
        await self.bot.edit_message(loader, "Calclulating... :cat:")
        url = s.results.share()
        await self.bot.delete_message(loader)
        await self.bot.say(url)

    @commands.command()
    async def mraw(self):
        """Meow !"""
        mraws = await self.bot.say(':regional_indicator_m: :regional_indicator_r: :regional_indicator_a: :regional_indicator_w:')

    @commands.command()
    async def kop1(self):
        """KOP1 !"""
        await self.bot.say(":regional_indicator_k: :regional_indicator_o: :regional_indicator_p: :one:")

    @commands.command()
    async def vdm(self):
        """The French FML website"""
        source = requests.Session().get("https://www.viedemerde.fr/aleatoire", headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"}).content
        soup = BeautifulSoup(source, "html.parser")
        vdm = list(random.choice(soup.find_all("p", class_="block hidden-xs")).children)[1].string 
        await self.bot.say("```" + vdm + "```")

    @commands.command()
    async def dtc(self):
        source = requests.get("https://www.danstonchat.com/random0.html").content
        soup = BeautifulSoup(source, "html.parser")
        lst = soup.find_all("div", class_="addthis_inline_share_toolbox")
        await self.bot.say("```" + random.choice(lst)["data-description"] + "```")

    @commands.command()
    async def fml(self):
        source = requests.Session().get("http://www.fmylife.com/random", headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"}).content
        soup = BeautifulSoup(source, "html.parser")
        fml = list(random.choice(soup.find_all("p", class_="block hidden-xs")).children)[1].string 
        await self.bot.say("```" + fml + "```")

    @commands.command()
    async def katology(self):
        katology = "Tu connais katology ? Un blog francais traitant de l'actualité technologique, avec un aspect communautaire !"
        await self.bot.say(katology)


def setup(bot):
    bot.add_cog(text(bot))