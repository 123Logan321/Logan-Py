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
from datetime import datetime
from time import gmtime, strftime
import asyncio
import datetime

bot = commands.Bot(command_prefix="+")
bot.remove_command('help')
file = open('D:\\🐧\\Python files\\py bot\\bad-words.txt','r')
contents = file.readlines()
content = []
file.close()
for i in contents[0:len(contents)]:
    if i.endswith('\n'):
        content.append(i.rstrip('\n')) 

file = open('D:\\🐧\\Python files\\py bot\\jap.txt','r')
contents = file.readlines()
hiraganaList = []
file.close()
for i in contents[0:len(contents)]:
    if i.endswith('\n'):
        hiraganaList.append(i.rstrip('\n')) 


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error

@bot.event
async def on_ready():
    print ("It is currently",(strftime('%Y-%m-%d %H:%M:%S')))
    print ("I am running on " + bot.user.name)
    print ("With the id: " + bot.user.id)
    await bot.change_presence(game=discord.Game(name="Hi I like to eat cookies"))

@bot.event
async def on_message(message):
    logContent = None
    logCon = []
    messageList = []
    badCount = {}
    author = message.author  
    if "+stop" in message.content:
        await bot.send_message(message.channel,"Byebye")
        await bot.logout()
    
    if author.id != '561593801915760650':
        if author.id != '257225194391732237':
            '''
            This part under the if statement takes in every single sentence send in discord by users that my bot is in
            and then it writes them into a txt file for me to see later on when needed
            
            Usage of File IO and lists are most dominant here
            
            Except:
                Any possible error that could prevent my bot from working essentially.
            '''
            print(author.name,'  ',(message.channel.name))
            text = (str(strftime('%Y-%m-%d %H:%M:%S')+" ["+str(message.server.name)+"] ["+str(message.channel.name)+"] ["+str(author.name)+'] said: ['+str(message.content))+']')
            try:
                logfile = open('D:\\🐧\\Python files\\py bot\\logs.txt','r')
                logContent = logfile.readlines()
                for i in logContent[0:len(logContent)]:
                    if i.endswith('\n'):
                        logCon.append(i.rstrip('\n'))
                logfile.close()
                
                logfile = open('D:\\🐧\\Python files\\py bot\\logs.txt','w')
                logCon.append(text)
                for i in range(len(logCon)):
                    logfile.write(str(logCon[i])+'\n')
                logfile.close()
                
            except (ValueError,TypeError,UnicodeDecodeError,UnicodeEncodeError,InterruptedError,IndexError):
                pass
            
        messageList = list(message.content.lower())
        checks = ["i'm","i am","iam",'im']
        if author.id != '561593801915760650' and str(message.channel) != "moon" and str(message.channel) != "gayme":
            for x in checks:
                if x in message.content.lower(): 
                    checker = True
                    for i in range(len(messageList)):
                        try:
                            if messageList[i] == 'm' and messageList[i+1] == ' ':
                                del messageList[0:i+1]
                                break
                            elif messageList[i] == 'm' and messageList[i+1].isalpha():
                                checker = False
                        except IndexError:
                                messageList = ['no name']
                                break
                    if checker != False:
                        embed=discord.Embed(title="Hi", description=('Hi  ***__'+''.join(messageList).upper()+"__*** :rofl:, I am cookie eater."), color= discord.Colour.green())
                        message = await bot.send_message(message.channel,embed=embed)
                        time.sleep(3)
                        await bot.delete_message(message)
                    messageList = []
                    
                
        for i in message.content.lower().split(' '):
            
            if i in content and author.id != '561593801915760650' and author.id != '562014582466412565':
                '''
                This part is where the bot will reply to the user by mentioning the user while sending one of the lines in the reply.txt file 
                to the message channel.
                '''
                replyfile = open('D:\\🐧\\Python files\\py bot\\reply.txt','r')
                logContent = None
                logContent = replyfile.readlines()
                logCon = []
                for i in logContent[0:len(logContent)]:
                    if i.endswith('\n'):
                        logCon.append(i.rstrip('\n'))
                p = random.randint(0,len(logCon)-1)
                embed=discord.Embed(title="Swearing Alert!", description=str('<@'+str(author.id)+'> \n'+str((logCon[p]))), color= discord.Colour.red())
                message = await bot.send_message(message.channel,embed=embed)
                time.sleep(5)
                await bot.delete_message(message)
                replyfile.close()
                
                logCon = []
                badfile = open('D:\\🐧\\Python files\\py bot\\bad-count.txt','r')
                logContent = badfile.readlines()
                for i in logContent[0:len(logContent)]:
                    logCon.append(i.rstrip('\n'))
                badfile.close()

                badfile = open('D:\\🐧\\Python files\\py bot\\bad-count.txt','w')
                for x in range(len(logCon)):
                    x = logCon[x]
                    character = []
                    character = list(x)
                    y = []
                    for i in range(len(character)):
                        if character[i] == ',':
                            character[i] = ':'
                    del character[0]
                    del character[len(character) - 1]
                    character.reverse()
                    for i in range(len(character)):
                        if character[i].isdecimal():
                            y.append(character[i])
                        else:
                            break
                    character.reverse()
                    y.reverse()
                    y = ''.join(y)
                    del character[19:len(character)]
                    del character[0]
                    x = ''.join(character)
                    badCount.update({str(x):int(y)})
                if author.id not in badCount.keys():
                    (badCount[author.id]) = 1
                else:
                    (badCount[author.id]) += 1
                for i in badCount.items():
                    badfile.write(str(i)+'\n')
                badfile.close()
            
        if message.content.lower() == '=' or '= <@!' in message.content.lower():
            logCon = []
            badfile = open('D:\\🐧\\Python files\\py bot\\bad-count.txt','r')
            logContent = badfile.readlines()
            for i in logContent[0:len(logContent)]:
                logCon.append(i.rstrip('\n'))
            badfile.close()

            badfile = open('D:\\🐧\\Python files\\py bot\\bad-count.txt','r')
            for x in range(len(logCon)):
                x = logCon[x]
                character = []
                character = list(x)
                y = []
                for i in range(len(character)):
                    if character[i] == ',':
                        character[i] = ':'
                del character[0]
                del character[len(character) - 1]
                character.reverse()
                for i in range(len(character)):
                    if character[i].isdecimal():
                        y.append(character[i])
                    else:
                        break
                character.reverse()
                y.reverse()
                y = ''.join(y)
                del character[19:len(character)]
                del character[0]
                x = ''.join(character)
                badCount.update({str(x):int(y)})
            ime = ()
            ID = ()
            if '= <@!' in message.content.lower():
                for i in badCount.keys():
                    if i in message.content.lower():    
                        ime = badCount[i]
                        ID = i
                        break
                if ime > 0:
                    embed=discord.Embed(title="Status", description=str('<@'+str(ID)+'> has sworn '+str(ime)+' times. :japanese_goblin:'), color=discord.Colour.dark_magenta())
                    await bot.send_message(message.channel, embed=embed)
                elif ime == 0:
                    embed=discord.Embed(title="Status", description=str('<@'+str(ID)+'> has sworn 0 times.'), color= discord.Colour.green())
                    await bot.send_message(message.channel, embed=embed)
                else:
                    embed=discord.Embed(title="Status", description=str('<@'+str(ID)+'> has a clean record.'), color= discord.Colour.green())
                    await bot.send_message(message.channel, embed=embed)
                badfile.close()
                
            else:
                for i in badCount.keys():
                    if i == author.id:
                        ime = badCount[i]
                        break            
                if ime >= 0:
                    embed=discord.Embed(title="Status", description=str(' <@'+str(author.id)+'> you have sworn '+str(ime)+' times. :japanese_goblin:'), color= discord.Colour.orange())
                    await bot.send_message(message.channel,embed=embed)
                    
                else:
                    embed=discord.Embed(title="Status", description=str(' <@'+str(author.id)+'> you have not sworn yet.'), color= discord.Colour.orange())
                    await bot.send_message(message.channel,embed=embed)
                badfile.close()
        
        if '->kiss <@!' in message.content.lower():
            await bot.send_message(message.channel,' <@'+str(author.id)+"> don't forget to say no homo, unless you are wearing socks.")

        if 'e2j' in message.content.lower():
            japContent = ()
            japLetters = []
            bracketRemove = []
            hiraganaLetters = []
            hiragana = {}
            key = []
            value = []
            finalMessage = []
            vowel = list('aeiou')
            alpha = list('qwertyuiopasdfghjklzxcvbnm')
            japFile = open('D:\\🐧\\Python files\\py bot\\jap.txt','r')
            japContent = japFile.readlines()
            for i in japContent[0:len(japContent)-1]:
                japLetters.append(i.rstrip('\n'))
            japFile.close()
            x = 0
            for i in japLetters:
                bracketRemove += list(i)
                del bracketRemove[0]
                del bracketRemove[len(bracketRemove)-1]
                japLetters[x] = ''.join(bracketRemove)
                x += 1
                bracketRemove = []
            for i in range(len(japLetters)):
                for x in japLetters[i]:
                    if x == "'":
                        pass
                    else:
                        hiraganaLetters.append(x)
                japLetters[i] = ''.join(hiraganaLetters)
                hiraganaLetters = []
            for i in japLetters:
                for a in i:
                    if a in alpha:
                        key.append(a)
                    elif a.isalpha() and a not in alpha:
                        value.append(a)
                    x = ''.join(key)
                hiragana.update({str(x):value})
                value = []
                key = []
            try:
                for i in message.content.lower().split(' '):
                    if i in hiragana.keys():
                        finalMessage += (hiragana[i])
                finalMessage = ''.join(finalMessage)
                await bot.send_message(message.channel,str(finalMessage))
            except:
                await bot.send_message(message.channel,'a wild bug within the program has appeared. ***Updates are coming*** ')
    
    else:
        None
    await bot.process_commands(message)
    
@bot.command(pass_context=True)
async def date(ctx):
   await bot.say(str(strftime('%Y-%m-%d %H:%M:%S')))

@bot.command(pass_context=True)
async def cheer(ctx):
    cheers = []
    cheerQuo = open('D:\\🐧\\Python files\\py bot\\cheer.txt','r')
    Quotes = cheerQuo.readlines()
    for i in Quotes[0:len(Quotes)- 1]:
        cheers.append(i.rstrip('\n'))
    cheerQuo.close()    
    n = random.randint(0,len(cheers)-1)
    embed = discord.Embed(title = ":heart:Cheer up!:heart: ",description= str(cheers[n]),color = discord.Colour.blue())
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
    
    embed = discord.Embed(color = discord.Colour.blue())
    
    embed.set_author(name = '+Help')
    await bot.send_message(author, embed=embed)

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: pong! lol")
    channel = ctx.message.channel
    t1 = time.perf_counter()
    await bot.send_typing(channel)
    t2 = time.perf_counter()
    embed=discord.Embed(title="Pong!", description='By the way, it took {}ms.'.format(round((t2-t1)*1000)), color= discord.Colour.green())
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    await bot.say("The users name is : {}".format(user.name))
    await bot.say("The users ID is: {}".format(user.id))
    await bot.say("The users status is: {}".format(user.status))
    await bot.say("The users highest role is: {}".format(user.top_role))
    await bot.say("The user joined at: {}".format(user.joined_at))

@bot.command(pass_context=True)
async def roll(ctx):
    author = ctx.message.author
    roll = random.randint(0,5)
    dice = [':one:',':two:',':three:',':four:',':five:',':six:']
    embed = discord.Embed(title="Dice Rolls!",description=str('<@'+str(author.id)+'>\n',str(dice[roll])),color=discord.Colour.orange)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def hit(ctx, user: discord.Member):
    await bot.say(":punch:  {}.   Ya Loser!".format(user.name))
    await bot.kick(user)
    
@bot.command(pass_context=True)
async def flower(ctx, user: discord.Member):
    await bot.say(":sunflower: For {}!".format(user.name))

@bot.command(pass_context=True)
async def fish(ctx):
    FishType = (random.randint(1,10000))
    fishType = [":blowfish:",":fish:",":tropical_fish:",":jigsaw:"]
    if FishType < 6000:
        result = fishType[0]
    elif FishType < 8500:
        result = fishType[1]
    elif FishType < 9999:
        result = fishType[2]
    else:
        result = fishType[3]
        
    embed=discord.Embed(title="Fish!", 
                        description='''  ----:fishing_pole_and_fish:----
                        
                                           :ocean:  :ocean:    :ocean:\n
                                       :palm_tree:  :palm_tree:  :palm_tree:  ''', 
                        color=discord.Colour.dark_teal())
    message = await bot.say(embed=embed)
    time.sleep(0.8)
    await bot.delete_message(message)
    time.sleep(0.3)
    Embed=discord.Embed(title="Casting!", 
description=
str(''' :fish::blowfish::blowfish:
    :fish::blowfish::tropical_fish:
    :blowfish::fish::blowfish: '''), 
    color=discord.Colour.dark_teal())
    message = await bot.say(embed=Embed)
    time.sleep(0.8)
    await bot.delete_message(message)
    time.sleep(0.3)
    sEmbed = discord.Embed(title="Result!",description=str(result),color= discord.Color.dark_teal())
    if result == ':jigsaw:':
        await bot.say("Woah...! you get a reward from <@!257225194391732237>",embed=sEmbed)
    await bot.say(embed=sEmbed)
    
bot.run("")
