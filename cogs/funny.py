import discord
import pyfiglet
import requests
import random
from discord.ext import commands
from cogs.utils import checks
from random import randint
from random import choice
from cogs.utils.chat_formatting import box
from bs4 import BeautifulSoup

class Fun:
	"""docstring for fun"""
	def __init__(self, bot):
		self.bot = bot
		self.nsword = 0

	@commands.command(pass_context=True)
	async def swordbattle(self, ctx, *, user: discord.Member):
		"""Sword Duel!"""
		author = ctx.message.author
		self.nsword += 1
		n = self.nsword
		if user.id == self.bot.user.id:
			await self.bot.say("I'm a cat ! Not a fighting guy !")
		else:
			await self.bot.say(author.mention + " and " + user.mention + " dueled for " + str(randint(1, 120)) +
								" hours! It was a long, heated battle, but " +
								choice([author.mention, user.mention]) + " is victorious !")

	@commands.command(pass_context=True)
	async def cookie(self, ctx, *, user: discord.Member):
		"""Give some cookie to a people!"""
		author = ctx.message.author
		if user.id == self.bot.user.id:
			await self.bot.say("Thank you :3 !")
		else:
			await self.bot.say(author.mention + " gave a :cookie: to " + user.mention + " :cat:")

	@commands.command(pass_context=True)
	async def heart(self, ctx, *, user: discord.Member):
		"""<3"""
		author = ctx.message.author
		user.id == self.bot.user.id
		await self.bot.say(":heart: " + user.mention)

	@commands.command(pass_context=True)
	async def arduino(self):
		"""We're loving arduino"""
		source = requests.Session().get("https://www.hackster.io/arduino/projects", headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"}).content
		soup = BeautifulSoup(source, "html.parser")
		lst = soup.find_all("div", class_="project_card__body__S0LrW cards__body__3yUOQ")
		print(lst)
		arduino = "https://www.hackster.io/" + random.choice(lst).string
		await self.bot.say(arduino)

def setup(bot):
    bot.add_cog(Fun(bot))
