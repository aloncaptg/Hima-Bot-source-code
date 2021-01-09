import discord
import os
import asyncio
import datetime
import random
import json
import aiohttp
from PIL import Image
from io import BytesIO
Pfp = os.environ.get('PFP')
from discord.ext import commands
emcolor = 0x777777
ercolor = 0xff0000
class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['avatar','av'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def av_cmd(self , ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
        pngav = member.avatar_url_as(static_format='png')
        jpghav = member.avatar_url_as(static_format='jpg')
        webpav = member.avatar_url_as(static_format='webp')
        embed = discord.Embed(
            color = discord.Color(0xffff),
            description=f"Avatar For {member.mention}\n\n[Png]({pngav}) | [Jpg]({jpghav}) | [Webp]({webpav}) ",
            title=f"Avatar"
        )
        embed.set_image(url=f"{pngav}")
        await ctx.send(embed=embed)
    @commands.command(aliases=['fetchavatar','fetchav'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def fetchav_cmd(self , ctx, members: int = None):
        if members == None:
            await ctx.send('You must provide the user id.')
        member = await self.bot.fetch_user(members)
        pngav = member.avatar_url_as(static_format='png')
        jpghav = member.avatar_url_as(static_format='jpg')
        webpav = member.avatar_url_as(static_format='webp')
        embed = discord.Embed(
            color = discord.Color(0xffff),
            description=f"Avatar For {member.mention}\n\n[Png]({pngav}) | [Jpg]({jpghav}) | [Webp]({webpav}) |\nID : {member.id}",
            title=f"Avatar"
        )
        embed.set_image(url=f"{webpav}")
        await ctx.send(embed=embed)
    @commands.command(aliases=['user-info','userinfo'])
    @commands.guild_only()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def user_info(self ,ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
        roles= [role for role in member.roles]
        embed = discord.Embed(
            color=discord.Color(0xffff))
        embed.set_author(name=f'Info for {member}',icon_url = f'{Pfp}')
        embed.set_thumbnail(url = member.avatar_url)
        embed.add_field(name='Info for member', value=f'{member.mention}\n[Direct Link]({member.avatar_url})')
        embed.add_field(name='ID', value=f'{member.id}')
        embed.add_field(name='Tag', value=f'#{member.discriminator}')
        embed.add_field(name='Member name', value=f'{member.name}')
        embed.add_field(name= "Member Status" , value = f"{member.status}")
        embed.add_field(name='Account created', value=member.created_at.strftime("%A, %d. %B %Y @ %H:%M:%S"))
        embed.add_field(name='Join date', value=member.joined_at.strftime("%A, %d. %B %Y @ %H:%M:%S"))
        embed.add_field(name="Bot?", value=f'*{member.bot}*')
        await ctx.send(embed=embed)

    @commands.command(aliases=['members'])
    @commands.guild_only()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def member(self , ctx, member: discord.Member = None):
        guild = ctx.guild
        await ctx.send(f'**__{ctx.guild.name}__** Has `{guild.member_count} Total members , Humans : {len(list(filter(lambda m: not m.bot, ctx.guild.members)))} , Bots : {len(list(filter(lambda m: m.bot, ctx.guild.members)))}`')
    @commands.command(aliases=['server_info'])
    @commands.guild_only()
    async def serverinfo(self, ctx):
        emojis = [str(x) for x in ctx.guild.emojis]
        guild = ctx.guild
        statuses = [len(list(filter(lambda m: str(m.status) == "online", ctx.guild.members))),
                    len(list(filter(lambda m: str(m.status) == "idle", ctx.guild.members))),
                    len(list(filter(lambda m: str(m.status) == "dnd", ctx.guild.members))),
                    len(list(filter(lambda m: str(m.status) == "offline", ctx.guild.members)))]
        embed = discord.Embed(
        color=discord.Color(0xffff),
        title=f"{ctx.guild.name}"
        )
        if ctx.guild.features == []:
            perk_strng = 'No Perks'
        else:
            perk_strng = ', '.join([str(p).replace("_", " ").title() for p in ctx.guild.features if p[1]])
        embed.set_author(name=f"Server Info!",icon_url = f'{ctx.author.avatar_url}')
        embed.set_thumbnail(url=f"{guild.icon_url}")
        embed.add_field(name='Guild Logo', value=f"**[Direct Link]({guild.icon_url})**")
        embed.add_field(name='Region', value=f"`{guild.region}`")
        embed.add_field(name='Member', value=f"`Total : {guild.member_count} , Humans : {len(list(filter(lambda m: not m.bot, ctx.guild.members)))} , Bots : {len(list(filter(lambda m: m.bot, ctx.guild.members)))}`")
        embed.add_field(name='Channels Counts', value=f'<:Textchanel:777387784192786433> {len(guild.text_channels)}\n<:Voicechannel:777387784432386048>{len(guild.voice_channels)}')
        embed.add_field(name='Boost', value=f'`{guild.premium_subscription_count}`')
        embed.add_field(name='Role Count', value=f'{len(guild.roles)}')
        embed.set_footer(text = f'Created At : {guild.created_at.strftime("%A, %d. %B %Y% @ H:%M:%S")}')
        embed.add_field(name="Owner", value=f"{guild.owner}({guild.owner.mention})")
        embed.add_field(name="Perks", value=f"{perk_strng}")
        embed.add_field(name="Categories", value=f"{len(ctx.guild.categories)}")
        embed.add_field(name="Verification Level", value=f"{guild.verification_level}")
        embed.add_field(name="Status", value=f"🟢 Online : {statuses[0]} 🟠 Idle : {statuses[1]} 🔴 DND : {statuses[2]} ⚪ Offline {statuses[3]}")
        await ctx.send(embed=embed)

    @commands.command(aliases=['invs'])
    @commands.guild_only()
    async def invites(self, ctx, user: discord.Member = 'self'):
        if user == 'self':
            user = ctx.author

        total = 0
        for i in await ctx.guild.invites():
            if i.inviter == user:
                total += i.uses

        def thing(c: int):
            if c == 1:
                return 'user'
            else:
                return 'users'

        e = discord.Embed(
            description=f'{user.mention} has invited {total} {thing(total)}.',
            color=emcolor
        )
        await ctx.send(embed=e)
def setup(bot):
    bot.add_cog(Misc(bot))