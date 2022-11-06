# SPDX-FileCopyrightText: 2022-present fmowl10 <jinseok1001@hotmail.com>
#
# SPDX-License-Identifier: MIT


from discord.ext import commands 
import discord
from deadList import deadList


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)


TOKEN=''


@bot.command()
async def helpdetail(ctx):
    out = (
        "/helpdetail - show this message\n"
        "/list show of videos\n"
        "/listchara __video__ dead list of __video__\n"
        "/isxdead __video__ __name__ is __name__ of __video__ dead"
    )
    await ctx.send(out)
    




@bot.command()
async def list(ctx):
    out = "list of movies"
    for movie in deadList.keys():
        out = out +"\n" + movie
    out = out + "\n" + "someone dead in these movies"
    await ctx.send(out)
    
    
@bot.command()
async def listchara(ctx, movieName):
    
    if not movieName in deadList.keys():
        out = f"we dont know about {movieName}\nPhew"
        await ctx.send(out)
        return

    out = "Spolier Alert\n Click to see\n"

    for name in deadList[movieName]:
        out = out + '\n|| ' + name + ' ||'

    await ctx.send(out)

@bot.command()
async def isxdead(ctx, movieName, name):
    if not movieName in deadList:
        out = f"we dont know about {movieName}Phew"
        await ctx.send(out)
        return

    out = "Spolier Alert\n Click to see\n||"

    if name in deadList[movieName]:
        out += "\n"+f"{name} gonna die"
    else:
        out += "\n" + f"Phew {name} not dead. unless writer kill"

    out += "||"

    await ctx.send(out)


bot.run(TOKEN)
