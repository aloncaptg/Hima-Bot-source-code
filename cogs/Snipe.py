from datetime import datetime

from discord import Color, Embed
from discord.ext import commands

class Snipe(commands.Cog):
    def __init__(self, bot, *args, **kwargs):
        self.bot = bot
        self.delete_snipes = dict()
        self.edit_snipes = dict()
        
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        self.delete_snipes[message.channel] = message

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        self.edit_snipes[after.channel] = (before, after)

    @commands.group(case_insensitive = True,invoke_without_command = True)
    async def snipe(self, ctx):
        '''Snipe a deleted message'''
        if ctx.invoked_subcommand is None:
            try:
                sniped_message = self.delete_snipes[ctx.channel]
            except KeyError:
                await ctx.send('Theres nothing to snipe.')
            else:
                result = Embed(
                    color=Color.red(),
                    description=sniped_message.content,
                    timestamp=sniped_message.created_at
                )
                result.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
                await ctx.send(embed=result)
    @snipe.command()
    async def edit(self, ctx):
        '''Snipes an edited message'''
        try:
            before, after = self.edit_snipes[ctx.channel]
        except KeyError:
            await ctx.send('There are no message edits in this channel to snipe!')
        else:
            result = Embed(
                color=Color.red(),
                timestamp=after.edited_at
            )
            result.add_field(name='Before', value=before.content, inline=False)
            result.add_field(name='After', value=after.content, inline=False)
            result.set_author(name=after.author.display_name, icon_url=after.author.avatar_url)
            await ctx.send(embed=result)

def setup(bot, *args, **kwargs):
    bot.add_cog(Snipe(bot, *args, **kwargs))