import discord # Documentation at https://discordpy.readthedocs.io
from discord.ext import commands

# Prefix to use bot commands. Can be anything including words
command_prefix = "!"

# Bot will receive all events (e.g., when a message gets sent, when someone joins the server)
intents = discord.Intents().all()

# Creates bot instance. This is the actual "bot"
bot = commands.Bot(command_prefix=command_prefix, intents=intents)


# Use @bot.event to create an event the bot will listen to
@bot.event
async def on_ready(): # on_ready is one of the events used by the bot
    # Get channel id by right clicking on channel and clicking copy id
    channel_id = 964774357920530444 # Go to Discord settings -> Advanced -> Turn on Developer Mode

    # Gets the channel instance
    channel = bot.get_channel(channel_id)

    # Send message in channel
    await channel.send("kd") # Must use "await" because .send() method is asynchronous (Do some research if you wanna know more)


# Runs discord bot
bot.run("TOKEN") # Input Discord bot token there
