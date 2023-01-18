import discord
from discord.ext import commands
#import RPi.GPIO as GPIO
from datetime import datetime
import time

intents = discord.Intents.all()
client = commands.Bot(command_prefix="!", intents=intents)

class Menu(discord.ui.View):
    def _init_(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label = "Ligar caldeira", style=discord.ButtonStyle.green)
    async def menu1(self,interaction: discord.Interaction, button: discord.ui.Button):
        #pega na data
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        
        #compoe o embeded e da lhe as propriedades
        embed = discord.Embed(color=discord.Color.green())
        embed.set_author(name=f"A caldeira foi ligada!")
        embed.add_field(name="Horas",value=f"{current_time}")
        
        #RPGIO script
        SwitchCaldeira()

        #sends embeded
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label = "Desligar caldeira", style=discord.ButtonStyle.red)
    async def menu3(self,interaction: discord.Interaction, button: discord.ui.Button):
        #pega na data
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")

        #compoe o embeded e da lhe as propriedades
        embed = discord.Embed(color=discord.Color.red())
        embed.set_author(name=f"A caldeira foi desligada!")
        embed.add_field(name="Horas",value=f"{current_time}")

        #RPGIO scritp
        SwitchCaldeira()

        #sends embeded
        await interaction.response.edit_message(embed=embed)

@client.command()
async def menu(ctx):
    view = Menu()
    await ctx.reply("Estado da caldeira:", view=view)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


#main runner
client.run('MTA2NDQ3NDAyMjAzMDYxODcyNA.GUNifE.yei61R4QcE2-6-7Iz01gLQ9naLhH2M4YYu7ycM')



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
