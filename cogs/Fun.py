import discord
import os
import asyncio
import datetime
import random
import json
import aiohttp
import pyfiglet
from PIL import Image
from io import BytesIO
Pfp = os.environ.get('PFP')
from discord.ext import commands
emcolor = 0x777777
ercolor = 0xff0000
class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['8ball'])
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def eight_ball_answr(self ,ctx, *,question):
        answers = [
        "As I see it, yes.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don’t count on it.",
        "It is certain.",
        "It is decidedly so.",
        "Most likely.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Outlook good.",
        "Reply hazy, try again.",
        "Signs point to yes.",
        "Very doubtful.",
        "Without a doubt.",
        "Yes.",
        "Yes – definitely.",
        "You may rely on it."
        ]
        

        embed = discord.Embed(
            description=f"\n\nQuestion Asked = \n\n`{question}`\n\nAnswer = {random.choice(answers)}",
            color=ctx.author.colour
        )
        embed.set_author(name=f"8ball",icon_url = f'{Pfp}')
        embed.set_thumbnail(url=f'{Pfp}')

        await ctx.send(embed=embed)
    
    

    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def ship(self,ctx,member : discord.Member):
        if member == None:
            member = ctx.author
        
        number1 = random.randint(1,20)
        number2 = random.randint(20,30)
        number3 = random.randint(30,50)
        number4 = random.randint(50,70)
        number5 = random.randint(70,100)
        answers = [
        f'{number1}/100',
        f'{number2}/100',
        f'{number3}/100',
        f'{number4}/100',
        f'{number5}/100'
        ]
        embed = discord.Embed(
            description=f"💗 **MATCHMAKING** 💗\n\n{random.choice(answers)}",
            color= discord.Colour.red()
        
        )
        embed.add_field(name="Member 2",value=f"**{member.mention}**", inline = True)
        embed.add_field(name="Member 1",value=f"**{ctx.author.mention}**", inline = True)
        await ctx.send(embed=embed)
        wanted = Image.open("ok.png")

        asset = member.avatar_url_as(format=None, static_format='png', size = 128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)

        pfp = pfp.resize((249,245))

        wanted.paste(pfp, (8,132))

        d = ctx.author.avatar_url_as(format=None, static_format='png', size = 128)
        data = BytesIO(await d.read())
        pfps = Image.open(data)

        pfps = pfp.resize((249,245))

        wanted.paste(pfp, (581,135))
        
        wanted.save(f'ship.png')

        await ctx.send(file=discord.File(f'ship.png'))
    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def howweeb(self,ctx,*,member : discord.Member = None):
        if member == None:
            member = ctx.author
        number1 = random.randint(1,20)
        number2 = random.randint(20,30)
        number3 = random.randint(30,50)
        number4 = random.randint(50,70)
        number5 = random.randint(70,100)
        answers = [
        f'{number1}/100',
        f'{number2}/100',
        f'{number3}/100',
        f'{number4}/100',
        f'{number5}/100'
        ]
        embed = discord.Embed(
            description=f"💗 **{member} Weeb** 💗\n\n= **You are {random.choice(answers)}**",
            color= discord.Colour.red()
        
        )
        embed.set_author(name=f"Weeb Machine")
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Fun(client))
