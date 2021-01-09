import discord
import os
import asyncio
import datetime
import random
import json
import aiohttp
from PIL import Image
from io import BytesIO
import mfx2_math as mfmath
Pfp = os.environ.get('PFP')
from discord.ext import commands
emcolor = 0x777777
ercolor = 0xff0000
class Math(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(aliases=['multiply'])
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def math_multiply_cmd(self,ctx, arg5 : int, arg6 : int, n1 : int = '0', n2 : int = '0'):
        embed = discord.Embed(
            description=f"***Math!***\n{mfmath.multiply(arg5, arg6, n1, n2)}",
            color=ctx.author.colour
        
        )
        await ctx.send(embed=embed)

    @commands.command(aliases=['divide'])
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def math_divide_cmd(self,ctx, arg7 : int, arg8 : int, n1 : int = '0', n2 : int = '0'):
        embed = discord.Embed(
            description=f"***Math!***\n{mfmath.divide(arg7, arg8, n1, n2)}",
            color=ctx.author.colour
        
        )
        await ctx.send(embed=embed)
    @commands.command(aliases=['add'])
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def math_add_cmd(self,ctx, arg9 : int, arg10 : int, n1 : int = '0', n2 : int = '0'):
        embed = discord.Embed(
            description=f"***Math!***\n{mfmath.add(arg9, arg10, n1, n2)}",
            color=ctx.author.colour
        
        )
        await ctx.send(embed=embed)
    @commands.command(aliases=['substract'])
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def math_substract_cmd(self,ctx, arg11 : int, arg12 : int, n1 : int = '0', n2 : int = '0'):
        embed = discord.Embed(
            description=f"***Math!***\n{mfmath.substract(arg11, arg12, n1, n2)}",
            color=ctx.author.colour
        
        )
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Math(bot))