import discord
import shutil
import os
from googlesearch import search
import wikipedia
from discord.ext import commands
from discord.utils import get
from mainbot import client


# Created by coolfav on Github

class Wikipedia(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["wiki", "w"])
    async def wikipedia(self, ctx, *query):
        thequery = " ".join(query)
        for j in search(thequery, tld="com", num=1, stop=1, pause=2):
            await ctx.send(j)
        await ctx.send(wikipedia.summary(wikipedia.search(thequery, results=1, suggestion=False), sentences=3, chars=0,
                                   auto_suggest=True, redirect=True))



def setup(client):
    client.add_cog(Wikipedia(client))
