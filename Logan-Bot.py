# Logan's first bot that does not work at all, because he is dumb

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
    print ("Hi!")
    print ("I am running on" + bot.user.name)
    print ("With the id:" + bot.user.id)

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: ping!! XSSS")
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
    await bot.say(":boot: cya, {}. Ya Loser!".format(user.name))
    await bot.kick(user)

bot.run("NTYxNTkzODAxOTE1NzYwNjUw.XJ-pzA.BZlxBgJVT58I93cPOvbqFn2YiWU")
