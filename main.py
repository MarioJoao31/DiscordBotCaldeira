import discord
from discord.ext import commands
#import RPi.GPIO as GPIO
from datetime import datetime
import time

client = commands.Bot(command_prefix='!',help_command=None,intents = discord.Intents.all())


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    #doesnt read the messages from bot
    if message.author == client.user:
        return
    if message.content.startswith('!ligar'):
        #get date 
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")

        #turns caldeira
        #SwitchCaldeira()

        #meter aqui o tempo a que a caldeira foi ligado 
        await message.channel.send(f'Caldeira ligada, as {current_time}')

@client.command()
async def hello(ctx):
    await ctx.channel.send('funciona fdp')
    



#main runner
client.run('MTA2NDQ3NDAyMjAzMDYxODcyNA.GxMTce.abkTcwk9eum6LhPogCmFW-zqKYrxRSZYm9t72w')



#func to switch caldeira
def SwitchCaldeira():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT)
    p = GPIO.PWM(12,50)
    p.start(7.5)
    p.ChangeDutyCycle(4.2)
    time.sleep(1)
    p.ChangeDutyCycle(2.5)
    time.sleep(1)
    p.stop()
    GPIO.cleanup()
