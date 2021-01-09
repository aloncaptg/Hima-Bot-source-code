import discord
import os
import asyncio
import datetime
from important import convert
from discord.ext import commands
from PIL import Image
from io import BytesIO
import aiohttp
class image(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def gay(self ,ctx, *, args : discord.Member = 'None'):
        if args == 'None':
            args = ctx.author
        avatar = args.avatar_url_as(format='jpg')
        embed = discord.Embed(
            color = discord.Color(0xffff),
        )
        embed.set_image(url=f"https://some-random-api.ml/canvas/gay?avatar={avatar}")
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def triggered(self ,ctx, *, args : discord.Member = 'None'):
        if args == 'None':
            args = ctx.author
        avatar = args.avatar_url_as(format='jpg')
        embed = discord.Embed(
            color = discord.Color(0xffff),
        )
        await ctx.send(f"https://some-random-api.ml/canvas/triggered?avatar={avatar}")

    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def minecraft(self ,ctx, *, args):

        a = args.split(' ')
        b = '+'.join(a)
        c = ctx.author.avatar_url_as(format='jpg')
        e = ctx.author.name.split(' ')
        d = '+'.join(e)


        embed = discord.Embed(
            color = discord.Color(0xffff),
        )
        embed.set_author(name=f"Achievement Get!")
        embed.set_image(url=f"https://minecraftskinstealer.com/achievement/2/Achievement+Get%21/{b}")
        await ctx.send(embed=embed)

    @commands.command(aliases=['ytcomment','comment'])
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def youtubecomment(self ,ctx, *, args):

        a = args.split(' ')
        b = '+'.join(a)
        c = ctx.author.avatar_url_as(format='jpg')
        e = ctx.author.name.split(' ')
        d = '+'.join(e)


        embed = discord.Embed(
            color = discord.Color(0xffff),
        )
        embed.set_author(name=f"Youtube Comment")
        embed.set_image(url=f"https://some-random-api.ml/canvas/youtube-comment?username={d}&avatar={c}&comment={b}")
        await ctx.send(embed=embed)
    @commands.command(pass_context=True)
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def Cat(self,ctx):
        embed = discord.Embed(title="Cats")

        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://some-random-api.ml/img/cat') as r:
                res = await r.json()
                embed.add_field(name='Credits',value=res['link'] + "\n\nPowered by some random api")
                embed.set_image(url=res['link'])
                await ctx.send(embed=embed)
    @commands.command(pass_context=True)
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def dog(self,ctx):
        embed = discord.Embed(title="Dogs")

        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://some-random-api.ml/img/dog') as r:
                res = await r.json()
                embed.add_field(name='_ _',value=res['link'])
                embed.set_image(url=res['link'])
                await ctx.send(embed=embed)
    @commands.command(pass_context=True)
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def Bird(self,ctx):
        embed = discord.Embed(title="Birds")

        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://some-random-api.ml/img/birb') as r:
                res = await r.json()
                embed.add_field(name='Credits',value=res['link'])
                embed.set_image(url=res['link'])
                await ctx.send(embed=embed)
    @commands.command(pass_context=True)
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def fox(self,ctx):
        embed = discord.Embed(title="Fox")

        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://some-random-api.ml/img/fox') as r:
                res = await r.json()
                embed.add_field(name='Credits',value=res['link'])
                embed.set_image(url=res['link'])
                await ctx.send(embed=embed)
    @commands.command(pass_context=True)
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def panda(self,ctx):
        embed = discord.Embed(title="Panda")

        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://some-random-api.ml/img/panda') as r:
                res = await r.json()
                embed.add_field(name='Credits',value=res['link'])
                embed.set_image(url=res['link'])
                await ctx.send(embed=embed)
    @commands.command(pass_context=True)
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def koala(self,ctx):
        embed = discord.Embed(title="Koala")

        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://some-random-api.ml/img/koala') as r:
                res = await r.json()
                embed.add_field(name='Credits',value=res['link'])
                embed.set_image(url=res['link'])
                await ctx.send(embed=embed)
    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def glass(self,ctx, *, args : discord.Member = 'None'):
        if args == 'None':
            args = ctx.author
        avatar = args.avatar_url_as(format='jpg')
        embed = discord.Embed(
            color = discord.Color(0xffff),
        )
        embed.set_author(name=f"Nice Glass Man.")
        embed.set_image(url=f"https://some-random-api.ml/canvas/glass?avatar={avatar}")
        await ctx.send(embed=embed)
    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def wasted(self,ctx, *, args : discord.Member = 'None'):
        if args == 'None':
            args = ctx.author
        avatar = args.avatar_url_as(format='jpg')
        embed = discord.Embed(
            color = discord.Color(0xffff),
        )
        embed.set_author(name=f"Imagine get killed in gta v")
        embed.set_image(url=f"https://some-random-api.ml/canvas/wasted?avatar={avatar}")
        await ctx.send(embed=embed)
    @commands.command(pass_context=True,aliases=['pika'])
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def pikachu(self,ctx):
        embed = discord.Embed(title="Pika pika?")

        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://some-random-api.ml/img/pikachu') as r:
                res = await r.json()
                embed.set_image(url=res['link'])
                embed.add_field(name='Credits',value=res['link'])
                await ctx.send(embed=embed)
    @commands.command(pass_context=True,aliases=['hugs'])
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def hug(self,ctx,*,member : discord.Member):
        embed = discord.Embed(title="Hug", description=f"{ctx.author.mention} Hugs {member.mention}")

        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://some-random-api.ml/animu/hug') as r:
                res = await r.json()
                embed.set_image(url=res['link'])
                await ctx.send(embed=embed)
    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def wanted(self,ctx, member : discord.Member = None):
            if member == None:
                member = ctx.author

            wanted = Image.open("wanted.png")

            asset = member.avatar_url_as(format=None, static_format='png', size = 128)
            data = BytesIO(await asset.read())
            pfp = Image.open(data)

            pfp = pfp.resize((212,217))

            wanted.paste(pfp, (128,130))

            wanted.save(f'profile.png')
            await ctx.send(file=discord.File(f'profile.png'))
def setup(bot):
    bot.add_cog(image(bot))