# Logan's first bot

import discord
import random
import time 
import sys
import re
import os
from discord.ext import commands
from discord.ext.commands import Bot
from discord.ext.commands import CommandNotFound
from discord import User
import asyncio

bot = commands.Bot(command_prefix="+")

#Black listed words
Swearing = open(r"C:\Users\Admin\Desktop\Swearingwords.txt")
SwearingWords = Swearing
Badwords = (SwearingWords.read())
#Badwords = (Badwords.split(","))
print (Badwords)
BW = ("fuck","shit","bitch","ass","fucking")
print (BW)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error

@bot.event
async def on_ready():
    print ("Hi, welcome back!")
    print ("It is currently bla bla clock")
    print ("I am running on " + bot.user.name)
    print ("With the id: " + bot.user.id)
    await bot.change_presence(game=discord.Game(name="Fuck my brain is small"))

@bot.event
async def on_message(message):
    if BW in message.content.lower():
        await bot.send_message(message.channel, 'Do you kiss your mother with that mouth?')
    await bot.process_commands(message)

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: pong!! XSSS")
    print ("user have pinged")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    await bot.say("The users name is : {}".format(user.name))
    await bot.say("The users ID is: {}".format(user.id))
    await bot.say("The users status is: {}".format(user.status))
    await bot.say("The users highest role is: {}".format(user.top_role))
    await bot.say("The user joined at: {}".format(user.joined_at))

@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    await bot.say(":boot:   {}.       Ya Loser!".format(user.name))
    await bot.kick(user)
    
@bot.command(pass_context=True)
async def flower(ctx, user: discord.Member):
    await bot.say(":sunflower: For {}!".format(user.name))
    print ("user have flowered")

@bot.command(pass_context=True)
async def fish(ctx):
    
    FishType = (random.randint(1,10))
    Bfish = int("6")
    Nfish = int("9")
    await bot.say("You've casted your :fishing_pole_and_fish: ")
    time.sleep(1)
    await bot.say("Please wait patiently...wait, do you even have patience?")
    Delay = (random.randint(0,6))
    time.sleep(Delay)

    if FishType <= Bfish:
        await bot.say("You've caught a   :blowfish:  YIKES!!!! EWWWW!!!")
    
    elif FishType <= Nfish:
        await bot.say("You've caught a   :fish:  I mean...It's not that bad?")
    
    else:
        await bot.say("You've caught a   :tropical_fish:   BRUH! INSANE LUCK!")
    

    print ("An user has fished")
