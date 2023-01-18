from discord.ext import commands
import discord

client = commands.Bot(command_prefix='!',intents = discord.Intents.all())

@client.event
async def on__ready():
    print("Bot online, Ready!")

@client.command()
async def hello(ctx):
    await ctx.channel.send('funciona fdp')

client.run('MTA2NDQ3NDAyMjAzMDYxODcyNA.GxMTce.abkTcwk9eum6LhPogCmFW-zqKYrxRSZYm9t72w')