import discord
import os
import asyncio
import datetime
import asyncio
import json
from important import convert
from discord.ext import commands
import datetime

Pfp = os.environ.get('PFP')
class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.group(case_insensitive = True,invoke_without_command = True)
    async def help(self,ctx):
        end = datetime.datetime.utcnow() + datetime.timedelta()
        with open("prefixes.json", "r") as f:
            prefixes = json.load(f)

        try:
            pre = prefixes[str(ctx.guild.id)]
        except:
            pre = 'hm!'
        if ctx.guild == None:
            ctx.guild = 'Hima'

        embed = discord.Embed(
        timestamp=end,
        description=f"**Prefix :**\nCurrent prefix of **__{ctx.guild}__** is `{pre}`.\nTo execute commands, first write the prefix and then the command, example : {pre}serverinfo.\n\n**Commands**", inline = True

        
        
        )
        
        embed.add_field(name="🏆 Games",value="Usage : `Help mod`", inline = False)
        embed.add_field(name="🛠️ Moderation",value="Usage : `Help mod`", inline = False)
        embed.add_field(name="🎶 Music",value="Usage : `Help music`\n", inline = False)
        embed.add_field(name="❌ Math",value="Usage : `Help math`", inline = False)
        embed.add_field(name="📷 Image",value="Usage : `Help image`", inline = False)
        embed.add_field(name="🍪 Misc",value="Usage : `Help misc`", inline = False)
        embed.add_field(name="⚙️ Configuration",value="Usage : `Help config`", inline = False)
        embed.add_field(name="<a:giveaway:787218481539842049> Giveaway",value="Usage : `Help giveaway`", inline = False)
        embed.set_author(name='Hima',icon_url = f'{Pfp}')
        embed.set_footer(text='Hima ')
        await ctx.send(embed=embed)
    @help.command()
    async def fun(self,ctx):
        end = datetime.datetime.utcnow() + datetime.timedelta()
        embed = discord.Embed(
        timestamp=end,
        description=f"**Fun**\n\n**Commands**\n`8ball [question]`\n`Ship [member]`\n`Howweeb`\n`Noice`\n`Snipe`", inline = False
        
        
        )
        embed.set_footer(text='Hima ')
        embed.set_author(name='Category: Fun',icon_url = f'{Pfp}')
        await ctx.send(embed=embed)
    @help.command(aliases=['moderation'])
    async def mod(self,ctx):
        end = datetime.datetime.utcnow() + datetime.timedelta()
        embed = discord.Embed(
        timestamp=end,
        description=f"**Moderation**\n\n**Commands**\n`Purge [Amount]`\n`Kick [Member Mention]`\n`Ban [Member mention]`\n`Unban [User]`\n`Mute [Member mention]`\n`Unmute [Member Mention]`\n`Tempmute [member] [duration] [reason]`\n`Warn [Member]`\n`Checkwarn [Member mention]`\n`Rename [New Nick] [Member]`\n`Normalnick [Member]`\n`Setdelay [Seconds]`\n`Createchannel [Name]`\n`Createvc [Name]` \n`Nuke`\n`Lock`\n`Unlock`", inline = False
        
        
        )
        embed.set_footer(text='Hima ')
        embed.set_author(name='Category: Mod',icon_url = f'{Pfp}')
        await ctx.send(embed=embed)
    @help.command(aliases=['miscellaneous'])
    async def misc(self,ctx):
        end = datetime.datetime.utcnow() + datetime.timedelta()
        embed = discord.Embed(
        timestamp=end,
        description=f"**Misc**\n\n**Commands**\n`Avatar [Member Mention]` Gets user avatar\n`fetchav [id]`\n`User-info [Member mention]`\n`ServerInfo`\n`Poll [Given question....]`\n`Members`\n`Invites`\n`Invite`", inline = False
        
        
        )

        embed.set_author(name='Category: Misc',icon_url = f'{Pfp}')
        embed.set_footer(text='Hima ')
        await ctx.send(embed=embed)
    @help.command(aliases=['games'])
    async def game(self,ctx):
        end = datetime.datetime.utcnow() + datetime.timedelta()
        embed = discord.Embed(
        timestamp=end,
        description=f"**Misc**\n\n**Commands**\n`RPS [Choices]`\n`Decipher [Option]`\n`Roll [user]`\n`Flip [Choice]`", inline = False
        
        
        )

        embed.set_author(name='Category: Misc',icon_url = f'{Pfp}')
        embed.set_footer(text='Hima ')
    @help.command()
    async def giveaway(self,ctx):
        end = datetime.datetime.utcnow() + datetime.timedelta()
        embed = discord.Embed(
        timestamp=end,
        description=f"**Misc**\n\n**Commands**\n`Gstart`\n`Greroll [Msg id] [Channel]`\n`Gend [Msg id] [Channel]`", inline = False
        
        
        )

        embed.set_author(name='Category: Misc',icon_url = f'{Pfp}')
        embed.set_footer(text='Hima ')
        await ctx.send(embed=embed)
    @help.command(aliases=['mathematics'])
    async def math(self,ctx):
        embed = discord.Embed(
        description=f"**Math**\n\n**Commands**\n`Substract [Number] [Number]`\n`Add [Number] [Number]`\n`Divide [Number] [Number]`\n`Multiply [Number] [Number]`", inline = False
        
        
        )

        embed.set_author(name='Category: Math',icon_url = f'{Pfp}')
        embed.set_footer(text = f'Credits : mutefx#2021')
        await ctx.send(embed=embed)
    @help.command(aliases=['configuration'])
    async def config(self,ctx):
        end = datetime.datetime.utcnow() + datetime.timedelta()
        embed = discord.Embed(
        timestamp=end,
        description=f"**Configuration**\n\n**Commands**\n`setprefix`\n`Setup`", inline = False
        
        
        )


        embed.set_author(name='Category: Configuration',icon_url = f'{Pfp}')
        embed.set_footer(text='Hima ')
        await ctx.send(embed=embed)
    @help.command(aliases=['Images'])
    async def image(self,ctx):
        end = datetime.datetime.utcnow() + datetime.timedelta()
        embed = discord.Embed(
        timestamp=end,
        description=f"**Image**\n\n**Commands**\n`Meme`\n`Cat`\n`Dog`\n`Fox`\n`Koala`\n`Panda`\n`Bird`\n`Comment [text]`\n`Wanted [User]`\n`Gay [User]`\n`Wasted [user]`\n`Triggered [user]`\n`Minecraft [Text]`", inline = False
        
        
        )


        embed.set_author(name='Category: Image',icon_url = f'{Pfp}')
        embed.set_footer(text='Hima ')
        await ctx.send(embed=embed)
    @help.command()
    async def music(self,ctx):
        end = datetime.datetime.utcnow() + datetime.timedelta()
        embed = discord.Embed(
        timestamp=end,
        description=f"**Music**\n\n**Commands**\n`Play [song]`\n`Stop`\n`Queue`\n`Now`\n`Resume`\n`Disconnect`\n`Join`\n`Summon`\n`Loops` \n`Volume [Amount]`\n`Remove (Song to remove)`\n`Skip`\n`Shuffle` Shuffles the queue"
        
        
        )

        embed.set_author(name='Category: Music',icon_url = f'{Pfp}')
        embed.set_footer(text='Hima ')
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))