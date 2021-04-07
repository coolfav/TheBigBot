import discord
import shutil
import os

import wikipedia
from discord.ext import commands


# Created by coolfav on Github
# Re-created by Cynthia Dev#0001 (VerstreuteSeele on Github) and ryann#7322 (Mysttt on Github)


class Wikipedia(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["wiki", "w"])
    async def wikipedia(self, ctx, *query):
        thequery = " ".join(query)
        link = wikipedia.page(thequery)
        await ctx.send(link.url)


def setup(client):
    client.add_cog(Wikipedia(client))
