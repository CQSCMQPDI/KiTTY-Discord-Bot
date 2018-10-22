from discord.ext import commands
from cogs.utils.chat_formatting import box

try:
    from pyfiglet import figlet_format
except:
    figlet_format = None


class Ascii(object):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ascii")
    async def _ascii(self, *, text):
        try:
            msg = str(figlet_format(text, font='cybermedium'))
            if msg[0] == " ":
                msg = "." + msg[1:]
            error = figlet_format("Too long !",
                                  font='cybermedium')
            if len(msg) > 2000:
                await self.bot.say(box(error))
            else:
                await self.bot.say(box(msg))
        except Exception as e:
            await self.bot.say("Don't use emojis :cat:, and/or accents")


def setup(bot):
    n = Ascii(bot)
    bot.add_cog(n)