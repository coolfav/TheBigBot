import discord
import shutil
import os
from discord.ext import commands
from discord.utils import get
from mainbot import client

# Created by coolfav on Github

class Wikipedia(commands.Cog):

    def __init__(self, client):
        self.client = client

# /wiki or something

def setup(client):
    client.add_cog(Wikipedia(client))