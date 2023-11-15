# bot.py
from discord.ext import commands
import discord
import time
import os
InstallDeps = input("Install dependencies? (y|n)")
CustomTokenyn = input("Custom Token? (y|n)")

if CustomTokenyn == "y":
    CustomToken = input("Enter your custom token: ")
    TOKEN = CustomToken
else:
    TOKEN = "Your own token goes here!"
    if TOKEN == "Your own token goes here!":
        print("Error: No standard Token defined")
        exit()
if InstallDeps == "y":
    print("Now Installing Deps")
    os.system("pip install discord")
    
os.system("cls")

print("Going for main start")

GUILD = 'Test'

bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())

print("Initiated Bot")

@bot.command(name="dm", pass_context=True)
async def dm(context, user: discord.User, message):
    message = message or "Test"
    await user.send(message)
    
@bot.command(name="normaldm", pass_context=True)
async def dm(context, user: discord.User):
    message = "Hello, this is Mee6.2, we are developing a Bot named "+ bot.user.name + " , you may use this bot in your server"
    await user.send(message)

@bot.command(name="boot", pass_context=False)
async def boot(context):
    await context.reply("Boot COMMAND not supported anymore")
    
    
@bot.event # could be client instead of bot for you
async def on_message(message):
    await bot.process_commands(message)
    if message.author == bot.user:
        return
    
    if "/dm" in message.content:
        print("COMMAND")
        return
    
    if isinstance(message.channel,discord.DMChannel):
        channel = bot.get_channel(1173945781468811274)
        await channel.send(message.author.name + ": " + message.content)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name="/helpme"))
    print("\033[32mAuth is a go, press Ctrl/Strg + C to stop")
    print("\033[0m")
    print("=================================================================================")
    print("|State: \033[32mOnline\033[0m                                                                  |")
    print("|Token: " + TOKEN + "|")
    print("|User: " + bot.user.name + "                                                                   |")
    print("=================================================================================")
    
@bot.command(name="helpme", pass_context=False)
async def helpme(context):
    await context.reply("Bot in Development (BiD) \n /helpme: Shows this dialoug \n More comming soon...")
    
print("Commands initiated \nAuth is now starting")

bot.run(TOKEN)
