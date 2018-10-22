import discord
from discord.ext import commands
from __main__ import send_cmd_help
import wikipedia
import urllib.request, json

class Wikipedia:
    """Wikipedia search for the Red-DiscordBot"""
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, no_pm=True)
    async def wikipedia(self, ctx, *text):
        """Wikipedia search. (Only french results)"""     

        if text == ():
            await send_cmd_help(ctx)
            return
        else:            
            s = "_";
            search = ""
            search = s.join(text)
            user = ctx.message.author
            wikiLang = 'fr'# Define the Wikipedia language / Most of these are supported » https://nl.wikipedia.org/wiki/ISO_3166-1
            ws = None
            wikipedia.set_lang(wikiLang)# Set the Wikipedia language.
            try:
                ws = wikipedia.page(search)
                wikiUrl = (ws.url.encode('ascii', 'xmlcharrefreplace'))
                await self.bot.say(wikiUrl.decode("utf8"))
            except:
                await self.bot.say( "Sorry {}, I've found any results :cat:".format(user))

    @commands.command(pass_context=True)
    async def docubuntu(self, ctx, args):    
        """Ubuntu Doc search, only french"""
        attends = await self.bot.say("I'm searching this for you, {} :cat: !".format(ctx.message.author.mention))
        html = urllib.request.urlopen("https://doc.ubuntu-fr.org/" + args).read()
        if "avez suivi un lien" in str(html):
           await self.bot.say("This page doesn't exist !")
        else:
            await self.bot.say("https://doc.ubuntu-fr.org/" + args)

    @commands.command(pass_context=True)
    async def searchaur(self, ctx, args):
        """Search into the AUR database."""
        attends = await self.bot.say("I'm searching this for you, {} :cat: !".format(ctx.message.author.mention))
        erreur = 0
        try:
            html = urllib.request.urlopen("https://aur.archlinux.org/packages/" + args).read()
        except:
            erreur = 1
        if erreur == 1:
            await self.bot.say("I've made a little search on this : https://aur.archlinux.org/packages/?K=" + args)
        else:
            await self.bot.say("https://aur.archlinux.org/packages/{0} ! \n Use ``pacaur -S {0}`` to install it :cat: !".format(args))

class ModuleNotFound(Exception):
    def __init__(self, m):
        self.message = m
    def __str__(self):
        return self.message
        
def setup(bot):
	bot.add_cog(Wikipedia(bot))