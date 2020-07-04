import discord
import shutil
import os
from discord.ext import commands
from discord.utils import get
from mainbot import client
import random


# Created by coolfav on Github

class Miscellaneous(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["roll", "dice"])
    async def rolldice(self, ctx, dices):
        number, sides = dices.split("d")
        number = int(number)
        sides = int(sides)
        total = 0
        for x in range(number):
            total = total + random.randint(0, sides)
        await ctx.send(f"{total}")

    @commands.command(aliases=["m"])
    async def math(self,ctx,operation,*nums):
        nums = list(map(int, nums))
        if operation == "add" or operation == "+":
            total = nums[0]
            for x in range (len(nums)-1):
                total = total + nums[x+1]
            await ctx.send(f"{total}")
        elif operation == "subtract" or operation == "-":
            total = nums[0]
            for x in range (len(nums)-1):
                total = total - nums[x+1]
            await ctx.send(f"{total}")
        elif operation == "multiply" or operation == "*" or operation == "x":
            total = nums[0]
            for x in range (len(nums)-1):
                total = total * nums[x+1]
            await ctx.send(f"{total}")
        elif operation == "divide" or operation == "/":
            total = nums[0]
            for x in range (len(nums)-1):
                total = total / nums[x+1]
            await ctx.send(f"{total}")


def setup(client):
    client.add_cog(Miscellaneous(client))
