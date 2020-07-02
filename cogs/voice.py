import discord
import shutil
import os
import youtube_dl
from discord.ext import commands
from discord.utils import get
from mainbot import client


# Created by coolfav on Github

class Voice(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['j'])
    async def join(self, ctx):
        channel = ctx.message.author.voice.channel
        voice1 = get(client.voice_clients, guild=ctx.guild)

        if voice1 is not None:
            return await voice1.move_to(channel)

        await channel.connect()

        await ctx.send(f"Joined {channel}")

    @commands.command()
    async def leave(self, ctx):
        channel = ctx.message.author.voice.channel
        voice = get(client.voice_clients, guild=ctx.guild)

        if voice and voice.is_connected():
            await voice.disconnect()
            await ctx.send(f"Disconnected from {channel}")
        else:
            await ctx.send("Unable to disconnect, probably not in a voice channel")

    @commands.command(aliases=['p'])
    async def play(self, ctx, *url: str):
        print("accepted play command")
        channel = ctx.message.author.voice.channel
        voice1 = get(client.voice_clients, guild=ctx.guild)

        if voice1 is not None:
            await voice1.move_to(channel)

        try:
            await channel.connect()
        except:
            print("already in voice channel")

        def checkqueue():
            Queue_infile = os.path.isdir("D:\Miscellaneous\projects\Python VSCodes\DiscordMusicBot\Queue")
            if Queue_infile:
                DIR = os.path.abspath(os.path.realpath("Queue"))
                length = len(os.listdir(DIR))
                still_q = length - 1
                try:
                    first_file = os.listdir(DIR)[0]
                    print("first file =" + first_file)
                except:
                    print("No more queued songs")
                    queues.clear()
                    return
                main_location = os.path.dirname(
                    os.path.realpath("D:\Miscellaneous\projects\Python VSCodes\DiscordMusicBot\Queue"))
                print("main location = " + main_location)
                song_path = os.path.abspath(os.path.realpath("Queue") + "\\" + first_file)
                print("song path = " + song_path)
                if length != 0:
                    print("Song done, playing next queued song\n")
                    print(f"Songs still in queue: {still_q}")
                    song_exists = os.path.isfile("song.mp3")
                    if song_exists:
                        os.remove("song.mp3")
                    shutil.move(song_path, main_location)
                    for file in os.listdir("D:\Miscellaneous\projects\Python VSCodes\DiscordMusicBot"):
                        if file.endswith(".mp3"):
                            os.rename(file, 'song.mp3')
                    voicenew.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: checkqueue())
                    voicenew.source = discord.PCMVolumeTransformer(voicenew.source)
                    voicenew.source.volume = 0.15
                else:
                    queues.clear()
                    return
            else:
                queues.clear()
                print("No songs were queued before the ending of the last song")

        song_exists = os.path.isfile("song.mp3")
        try:
            if song_exists:
                os.remove('song.mp3')
                queues.clear()
                print("removed existing song")
        except PermissionError:
            await ctx.send("Another song is already playing")
            print("exception error")
            return

        Queue_infile = os.path.isdir("D:\Miscellaneous\projects\Python VSCodes\DiscordMusicBot\Queue")
        try:
            Queue_folder = "D:\Miscellaneous\projects\Python VSCodes\DiscordMusicBot\Queue"
            if Queue_infile is True:
                print("Removed old Queue Folder")
                shutil.rmtree(Queue_folder)
        except:
            print("No old queue folder")

        await ctx.send("Hold on, getting everything ready (this clears the queue as well)")

        voicenew = get(client.voice_clients, guild=ctx.guild)

        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': 'D:\Miscellaneous\projects\Python VSCodes\DiscordMusicBot\song.mp3',
            'postprocessors': [{
                'key': "FFmpegExtractAudio",
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        song_search = " ".join(url)

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            print("downloading audio now...\n")
            ydl.download([f"ytsearch1:{song_search}"])

        voicenew.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: checkqueue())
        voicenew.source = discord.PCMVolumeTransformer(voicenew.source)
        voicenew.source.volume = 0.15

        print("playing song successfully")
        await ctx.send(f"Playing song")

    @commands.command()
    async def pause(self, ctx):
        voice2 = get(client.voice_clients, guild=ctx.guild)

        if voice2 and voice2.is_playing():
            voice2.pause()
            await ctx.send("Music is paused")
        elif voice2.is_paused():
            voice2.resume()
            await ctx.send("Resuming music")
        else:
            await ctx.send("Music isn't playing")

    @commands.command()
    async def skip(self, ctx):
        voice3 = get(client.voice_clients, guild=ctx.guild)
        queues.clear()
        if voice3 and voice3.is_playing():
            voice3.stop()
            await ctx.send("Song skipped")
        else:
            await ctx.send("Music is not playing")

    global queues
    queues = {}

    @commands.command(aliases=["q", "qu", "que"])
    async def queue(self, ctx, *url: str):
        queue_infile = os.path.isdir("D:\Miscellaneous\projects\Python VSCodes\DiscordMusicBot\Queue")
        if queue_infile is False:
            os.mkdir("D:\Miscellaneous\projects\Python VSCodes\DiscordMusicBot\Queue")
        DIR = os.path.abspath(os.path.realpath("Queue"))
        qlength = len(os.listdir(DIR))
        qlength += 1
        add_queue = True
        while add_queue:
            if qlength in queues:
                qlength += 1
            else:
                add_queue = False
                queues[qlength] = qlength
        queue_path = os.path.abspath(os.path.realpath("Queue") + f"\song{qlength}.%(ext)s")
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': queue_path,
            'postprocessors': [{
                'key': "FFmpegExtractAudio",
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        song_search = " ".join(url)

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            print("downloading queue audio now...\n")
            ydl.download([f"ytsearch1:{song_search}"])
        await ctx.send("Adding song " + str(qlength) + " to the queue")

    @commands.command()
    async def reset(self, ctx):
        voice4 = get(client.voice_clients, guild=ctx.guild)
        try:
            voice4.stop()
        except:
            await ctx.send("There was nothing currently playing, but")
        queues.clear()
        queue_infile = os.path.isdir("D:\Miscellaneous\projects\Python VSCodes\DiscordMusicBot\Queue")
        if queue_infile:
            shutil.rmtree("D:\Miscellaneous\projects\Python VSCodes\DiscordMusicBot\Queue")
        try:
            for filename in os.listdir('D:\Miscellaneous\projects\Python VSCodes\DiscordMusicBot'):
                if filename.endswith(".mp3"):
                    os.remove(filename)
        except:
            await ctx.send("Stopped music and cleared queue")

    @commands.command(aliases = ["v", "vol"])
    async def volume(self, ctx, volume: int):
        if ctx.voice_client is None:
            return await ctx.send("Not ocnnected to voice channel")

        print(volume/100)

        ctx.voice_client.source.volume = volume / 100
        await ctx.send(f"Changed volume to {volume}%")


def setup(client):
    client.add_cog(Voice(client))
