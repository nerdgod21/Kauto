import discord
from discord.ext import tasks
from discord.ext    import commands
from discord.ext.commands   import Bot
import asyncio

client = discord.Client()

@tasks.loop(minutes=30)
async def test():
    channel = client.get_channel(964774357224292383/964774357920530444)
    channel.send("kd")

@client.event
async def on_ready():
    test.start()




Bot.run("TOKEN")
