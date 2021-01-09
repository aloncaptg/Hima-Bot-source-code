import discord
import os
import asyncio
from discord.ext import commands
import json
import random
import aiohttp
Pfp = os.environ.get('PFP')
class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def invite(self,ctx):
        embed = discord.Embed(
        description=f"Admin invite : [Hover to invite](https://discord.com/api/oauth2/authorize?client_id=796708021694496809&permissions=8&scope=bot) \n\nRecommended Invite : [Hover to invite](https://discord.com/api/oauth2/authorize?client_id=796708021694496809&permissions=0&scope=bot)\n\nDeveloped By • [NotCapt#6349](https://www.youtube.com/channel/UClHDPZ-vw4M3LDuludJYW2g?view_as=subscriber)", inline = False
        )

        
        embed.set_author(name='Invite Hima',icon_url = f'{Pfp}')
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Utility(bot))
