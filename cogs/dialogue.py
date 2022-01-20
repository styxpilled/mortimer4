from discord.ext import commands
from lib.env import CONFIG
from lib.log import logConsole

from fuzzywuzzy import fuzz

log = logConsole()

class Dialogue(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        if str(message.channel) in CONFIG['CHANNELS']:
            ratio = fuzz.partial_ratio(message.content.lower(), self.bot.user.name.lower())
            log.info(ratio)
            if len(message.content) > 4 and (self.bot.user.mentioned_in(message) or ratio > 75):
                log.info(f'Mentioned in #{message.channel}')
                await message.channel.send(ratio)

def process_message():
    pass

def setup(bot):
    bot.add_cog(Dialogue(bot))