import discord
import random

from discord.ext import commands

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print("RefBot is ready :-)")


# HELP------------------------------------------------------------------------------------------------------------------
@bot.command()
async def getHelp(ctx):
    await ctx.send("**REFBOT GUIDE:**\n"
                   "**Uploading Images:**\nUse one of the following commands to upload an image depending on its "
                   "category:\n "
                   "*!upPeople/!upPlace/!upAnimal/!upThing*\n"
                   "Follow this command with the image URL!\n*For example, if you wanted to upload a picture of a "
                   "cute bird, "
                   "you would type: !upAnimal [URL]*\n"
                   "**Requesting Reference:**\nUse one of the following commands to request an image depending on its "
                   "category:\n*!people/!place/!animal/!thing*\n")


# UPLOADING AN IMAGE----------------------------------------------------------------------------------------------------
@bot.command()
async def upPeople(ctx, url):
    f = open("people.txt", "a")
    f.write("\n{}".format(url))
    f.close()
    await ctx.channel.purge(limit=1)
    await ctx.send('Image of a person uploaded successfully! :-)')


@bot.command()
async def upPlace(ctx, url):
    f = open("place.txt", "a")
    f.write("\n{}".format(url))
    f.close()
    await ctx.channel.purge(limit=1)
    await ctx.send('Image of a place uploaded successfully! :-)')


@bot.command()
async def upAnimal(ctx, url):
    f = open("animal.txt", "a")
    f.write("\n{}".format(url))
    f.close()
    await ctx.channel.purge(limit=1)
    await ctx.send('Image of an animal uploaded successfully! :-)')


@bot.command()
async def upThing(ctx, url):
    f = open("thing.txt", "a")
    f.write("\n{}".format(url))
    f.close()
    await ctx.channel.purge(limit=1)
    await ctx.send('Image of a thing uploaded successfully! :-)')


# ----------------------------------------------------------------------------------------------------------------------

# REQUESTING AN IMAGE---------------------------------------------------------------------------------------------------
@bot.command()
async def people(ctx):
    f = open("people.txt", "r")
    urlList = f.readlines()
    total = len(urlList)
    f.close()

    rand = random.randint(1, total)
    url = urlList[rand - 1]
    await ctx.send(url)


@bot.command()
async def place(ctx):
    f = open("place.txt", "r")
    urlList = f.readlines()
    total = len(urlList)
    f.close()

    rand = random.randint(1, total)
    url = urlList[rand - 1]
    await ctx.send(url)


@bot.command()
async def animal(ctx):
    f = open("animal.txt", "r")
    urlList = f.readlines()
    total = len(urlList)
    f.close()

    rand = random.randint(1, total)
    url = urlList[rand - 1]
    await ctx.send(url)


@bot.command()
async def thing(ctx):
    f = open("thing.txt", "r")
    urlList = f.readlines()
    total = len(urlList)
    f.close()

    rand = random.randint(1, total)
    url = urlList[rand - 1]
    await ctx.send(url)


@bot.command()
async def ref(ctx):
    category = random.randint(1, 4)
    urlList = []
    total = 0

    def one():
        f = open("people.txt", "r")
        urlList = f.readlines()
        total = len(urlList)
        f.close()

    def two():
        f = open("place.txt", "r")
        urlList = f.readlines()
        total = len(urlList)
        f.close()

    def three():
        f = open("animal.txt", "r")
        urlList = f.readlines()
        total = len(urlList)
        f.close()

    def four():
        f = open("thing.txt", "r")
        urlList = f.readlines()
        total = len(urlList)
        f.close()

    options = {1: one, 2: two, 3: three, 4: four}
    options[category]()

    rand = random.randint(1, total)
    url = urlList[rand - 1]
    await ctx.send(url)


bot.run('NzkwMjg2NjA5MjIzMzg1MTA4.X9-Zwg._31oaJCprqlRpbmNLltzsryvAQI')
