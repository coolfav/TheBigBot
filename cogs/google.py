import discord
import shutil
import os
from googlesearch import search
from google_images_search import GoogleImagesSearch
from bs4 import BeautifulSoup
from mainbot import client
from discord.ext import commands
from discord.utils import get

# Created by coolfav on Github

apikeyfile = open("apikey.txt", 'r')
apikey = apikeyfile.read()
apikeyfile.close()

cxfile = open("cx.txt", 'r')
cx = cxfile.read()
cxfile.close()

gis = GoogleImagesSearch(apikey, cx)


class Google(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["wikilink","wl", "wikil", "wikipedial", "wlink"])
    async def wikipedialink(self, ctx, *lookfor):
        looking = " ".join(lookfor)
        query = "en.wikipedia.org" + looking
        for j in search(query, tld="com", num=1, stop=1, pause=2):
            await ctx.send(j)

    @commands.command(aliases=["gi","googleimages","googlei","gimage","gimages"])
    async def googleimage(self, ctx, num:int,*imaged):
        Images_infile = os.path.isdir(".\Images")
        await ctx.send("This might take a few seconds")
        try:
            Images_folder = ".\Images"
            if Images_infile is True:
                shutil.rmtree(Images_folder)
                print("Removed old Images folder")
                os.mkdir(".\Images")
                print("Made new Images folder")
            else:
                os.mkdir(".\Images")
                print("images_infile was false, making images folder")
        except:
            print("No old images folder")
            os.mkdir(".\Images")
            print("Made new images folder")
        Images_infile2 = os.path.isdir(".\Images")
        if Images_infile2 is False:
            return await ctx.send("Error: something happened. Try again if you like.")
        q = " ".join(imaged)
        start = 1
        _search_params = {
            'q': q,
            'searchType': 'image',
            'num': num,
            'start': start,
            'safe': 'medium',
            'fileType': 'jpg',
            'imgType': None,
            'imgSize': None,
            'imgDominantColor': None
        }
        gis.search(search_params=_search_params, path_to_dir='.\Images')
        count = 1
        dirrr = ".\Images"
        for file in os.listdir(dirrr):
            if file.endswith(".jpg"):
                os.rename(f".\Images\{file}",
                          f".\Images\image{count}.jpg")
                count += 1
        for image in os.listdir('.\Images'):
            if image.startswith("image"):
                await ctx.send(file=discord.File(f'.\Images\{image}'))


def setup(client):
    client.add_cog(Google(client))
