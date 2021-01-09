import discord
import os
import asyncio
from discord.ext import commands
import json
class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(Events(bot))
