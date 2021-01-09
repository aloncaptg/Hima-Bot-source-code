import discord
import os
import asyncio
import datetime
import random
import json
Pfp = os.environ.get('PFP')
from discord.ext import commands

class Poll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def poll(self,ctx , title = None , question1 = None , question2 = None , question3 = None , question4 = None , question5 = None ,*,question6 = None):
        if title == None:
            await ctx.send("`Enter a title / Missing required argument.`")
        elif question1==None:
            await ctx.send("`Must more than 1 question / Missing required argument.`")
        elif question2==None:
            await ctx.send("`Must more than 1 question / Missing required argument.`")
        elif question3==None:
            embed = discord.Embed(
            title=f"Poll", 
            description=f"1️⃣ {question1} \n\n 2️⃣ {question2}\n\n Poll By {ctx.author.mention}"


            )
            embed.set_author(name=f'{title}',icon_url = f'{ctx.author.avatar_url}')
            message = await ctx.send(embed=embed)
            await message.add_reaction('1️⃣')
            await message.add_reaction('2️⃣')
        elif question4==None:
            embed = discord.Embed(
            title=f"Poll", 
            description=f"1️⃣ {question1} \n\n 2️⃣ {question2} \n\n 3️⃣ {question3} \n\n Poll By {ctx.author.mention}"


            )

            embed.set_author(name=f'{title}',icon_url = f'{ctx.author.avatar_url}')
            message = await ctx.send(embed=embed)
            await message.add_reaction('1️⃣')
            await message.add_reaction('2️⃣')
            await message.add_reaction('3️⃣')
        elif question5==None:
            embed = discord.Embed(
            title=f"Poll", 
            description=f"1️⃣ {question1} \n\n 2️⃣ {question2} \n\n 3️⃣ {question3} \n\n 4️⃣ {question4} \n\n Poll By {ctx.author.mention}"


            )

            embed.set_author(name=f'{title}',icon_url = f'{ctx.author.avatar_url}')
            message = await ctx.send(embed=embed)
            await message.add_reaction('1️⃣')
            await message.add_reaction('2️⃣')
            await message.add_reaction('3️⃣')
            await message.add_reaction('4️⃣')
        elif question6==None:
            embed = discord.Embed(
            title=f"Poll", 
            description=f"1️⃣ {question1} \n\n 2️⃣ {question2} \n\n 3️⃣ {question3} \n\n4️⃣ {question4} \n\n5️⃣ {question5}\n\n Poll By {ctx.author.mention}"


            )

            embed.set_author(name=f'{title}',icon_url = f'{ctx.author.avatar_url}')
            msg = await ctx.send(embed=embed)
            await msg.add_reaction('1️⃣')
            await msg.add_reaction('2️⃣')
            await msg.add_reaction('3️⃣')
            await msg.add_reaction('4️⃣')
            await msg.add_reaction('5️⃣')
        else:
            embed = discord.Embed(
            title=f"Poll", 
            description=f"1️⃣ {question1} \n\n 2️⃣ {question2} \n\n 3️⃣ {question3} \n\n4️⃣ {question4} \n\n5️⃣ {question5}\n\n6️⃣ {question6}\n\n Poll By {ctx.author.mention}"


            )

            embed.set_author(name=f'{title}',icon_url = f'{ctx.author.avatar_url}')
            
            msg = await ctx.channel.send(embed=embed)
            
            await msg.add_reaction('1️⃣')
            await msg.add_reaction('2️⃣')
            await msg.add_reaction('3️⃣')
            await msg.add_reaction('4️⃣')
            await msg.add_reaction('5️⃣')
            await msg.add_reaction('6️⃣')
def setup(client):
    client.add_cog(Poll(client))
