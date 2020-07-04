import discord
import shutil
import os
from googlesearch import search
from google_images_search import GoogleImagesSearch
from bs4 import BeautifulSoup
from mainbot import client
from discord.ext import commands
from discord.utils import get
gis = GoogleImagesSearch('API key', 'cx')
# Created by coolfav on Github

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
        Images_infile = os.path.isdir("D:\Miscellaneous\projects\Python VSCodes\DiscordMusicBot\Images")
        await ctx.send("This might take a few seconds")
        try:
            Images_folder = "D:\Miscellaneous\projects\Python VSCodes\DiscordMusicBot\Images"
            if Images_infile is True:
                shutil.rmtree(Images_folder)
                print("Removed old Images folder")
                os.mkdir("D:\Miscellaneous\projects\Python VSCodes\DiscordMusicBot\Images")
                print("Made new Images folder")
            else:
                os.mkdir("D:\Miscellaneous\projects\Python VSCodes\DiscordMusicBot\Images")
                print("images_infile was false, making images folder")
        except:
            print("No old images folder")
            os.mkdir("D:\Miscellaneous\projects\Python VSCodes\DiscordMusicBot\Images")
            print("Made new images folder")
        Images_infile2 = os.path.isdir("D:\Miscellaneous\projects\Python VSCodes\DiscordMusicBot\Images")
        if Images_infile2 is False:
            return await ctx.send("Error: something happened. Try again if you like.")
        q = " ".join(imaged)
        _search_params = {
            'q': q,
            'searchType': 'image',
            'num': num,
            'start': 1,
            'safe': 'medium',
            'fileType': 'jpg',
            'imgType': None,
            'imgSize': None,
            'imgDominantColor': None
        }
        gis.search(search_params=_search_params, path_to_dir='D:\Miscellaneous\projects\Python VSCodes\DiscordMusicBot\Images')
        count = 1
        dirrr = "D:\Miscellaneous\projects\Python VSCodes\DiscordMusicBot\Images"
        for file in os.listdir(dirrr):
            if file.endswith(".jpg"):
                os.rename(f"D:\Miscellaneous\projects\Python VSCodes\DiscordMusicBot\Images\{file}",
                          f"D:\Miscellaneous\projects\Python VSCodes\DiscordMusicBot\Images\image{count}.jpg")
                count += 1
        for image in os.listdir('D:\Miscellaneous\projects\Python VSCodes\DiscordMusicBot\Images'):
            if image.startswith("image"):
                await ctx.send(file=discord.File(f'D:\Miscellaneous\projects\Python VSCodes\DiscordMusicBot\Images\{image}'))

def setup(client):
    client.add_cog(Google(client))
