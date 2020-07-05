import discord
import os
from discord.ext import commands

# Created by coolfav on Github

client = commands.Bot(command_prefix="/")

tokenfile = open("token.txt", 'r')
token = tokenfile.read()
tokenfile.close()

@client.event
async def on_ready():
    print("good to go")
    game = discord.Game("/help")
    await client.change_presence(activity=game)


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
    if filename.endswith(".py"):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(token)
