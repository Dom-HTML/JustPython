import random
import asyncio
import aiohttp
import discord
from discord import Guild
from discord import Game
from discord.ext.commands import Bot
import datetime


##### INITIALISATION #####

BOT_PREFIX = ("!")#change this accordingly example command: !ping
TOKEN = ""#bot token found on discord developer website

players = {}

client = Bot(command_prefix=BOT_PREFIX)

## --- ##

##### DEBUG COMMANDS #####

#ping pong function
@client.command(name="ping",
                description="ping test",
                brief="ping",
                aliases=["pg"],
                pass_context=True)
async def ping(context):
    await context.send("Pong")

#random number
@client.command(name="rand",
                description="random number",
                brief="rand",
                aliases=["sixtynine"],
                pass_context=True)
async def rand(context):
    randNum = random.randint(0, 100)
    await context.send(str(randNum))

#rock paper scissors 
@client.command(name="rps",
                description="rock paper sissors",
                brief="rock paper scissors",
                aliases=["rockpaperscissors"],
                pass_context=True)
async def rps(context, play):

    cplay = ""
    randState = random.randint(1,3)
    if (randState == 1):
        cplay = "rock"
    elif (randState == 2):
        cplay = "paper"
    elif (randState == 3):
        cplay = "scissors"

    if play.lower() == "r" or play.lower() == "rock":
        await context.send(str(cplay))
    elif play.lower() == "p" or play.lower() == "paper":
        await context.send(str(cplay))
    elif play.lower() == "s" or play.lower() == "scissors":
        await context.send(str(cplay))

## --- ##

async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        print("Date and Time: ")
        currentDT = datetime.datetime.now()
        print(currentDT)
        await asyncio.sleep(600)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.loop.create_task(list_servers())
client.run(TOKEN)
