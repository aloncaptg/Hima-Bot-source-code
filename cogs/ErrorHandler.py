import discord
import os
import asyncio
from discord.ext import commands
import json
class ErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        print(error)
        with open("prefixes.json", "r") as f:
            prefixes = json.load(f)
        try:
            pre = prefixes[str(ctx.guild.id)]
        except:
            pre = 'a!'
        if isinstance(error, discord.ext.commands.errors.CommandNotFound):
            pass
        if isinstance(error, discord.ext.commands.errors.BadArgument):
            await ctx.send(f'<:OkNo:783666946573991987> {ctx.author.mention}, Theres error while executing the command `Error : {error}`')
        if isinstance(error, discord.ext.commands.errors.CommandOnCooldown):
            try:
                await ctx.send(f'{ctx.author.mention}, This command is on cooldown please try it after {error.retry_after:.2f}s')
            except:
                pass
        if isinstance(error, discord.ext.commands.errors.MissingPermissions):
            missing = [perm.replace('_', ' ').replace('guild', 'server').title() for perm in error.missing_perms]
            if len(missing) > 2:
                fmt = '{}, and {}'.format("**, **".join(missing[:-1]), missing[-1])
            else:
                fmt = ' and '.join(missing)
            await ctx.send(f'{ctx.author.mention}, `You are missing {fmt} permissions(s) to run the command`')
        if isinstance(error, discord.ext.commands.errors.BotMissingPermissions):
            missing = [perm.replace('_', ' ').replace('guild', 'server').title() for perm in error.missing_perms]
            if len(missing) > 2:
                fmt = '{}, and {}'.format("**, **".join(missing[:-1]), missing[-1])
            else:
                fmt = ' and '.join(missing)
        try:
            await ctx.send(f'{ctx.author.mention}, `im missing {fmt} permissions(s) to run this command`')
        except:
            pass
        if isinstance(error, discord.ext.commands.errors.NoPrivateMessage):
            try:
                await ctx.send(f'{ctx.author.mention}, `Sorry but this command is usable in Dm`s`')
            except:
                pass
        if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
            try:
                await ctx.send(f'{ctx.author.mention}, `Error : Theres atleast one requred argument that missing!`')
            except:
                pass
def setup(bot):
    bot.add_cog(ErrorHandler(bot))