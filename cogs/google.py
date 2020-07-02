import discord
import shutil
import os
import google
import googlesearch
from mainbot import client
from discord.ext import commands
from discord.utils import get

# Created by coolfav on Github

class Google(commands.Cog):

    def __init__(self, client):
        self.client = client

# if discord/ctx.TextChannel.is_nsfw():     for google images
#   you cant do that here
# make a file called nsfwwords.txt

def setup(client):
    client.add_cog(Google(client))