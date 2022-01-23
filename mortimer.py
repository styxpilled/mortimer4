'''
# MORTIMER 4
'''

from discord import Intents
from discord.ext import commands
from lib.env import CONFIG

from lib.log import setup_logging, log_console, log_discord

setup_logging()
log = log_console()
logfile = log_discord()

INTENTS = Intents.default()

bot = commands.Bot(command_prefix='m!', intents=INTENTS)

@bot.event
async def on_ready():
    log.info('Mortimer online!')
    log.info(f'Logged in as [{bot.user.name}] [ID: {bot.user.id}] \n')

bot.load_extension('cogs.commands')
bot.load_extension('cogs.dialogue')

bot.run(CONFIG['TOKEN'])
