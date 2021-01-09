import discord
import os
import asyncio
import datetime
import asyncio
from important import convert ,boredemoji
from discord.ext import commands
import datetime
prefix = 'c!'
import json
class Automod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    
    @commands.command(aliases=['softmuting'])
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.guild_only()
    @commands.has_permissions(manage_channels = True)
    @commands.bot_has_guild_permissions(manage_channels = True)
    async def tempmute(self ,ctx,member : discord.Member,times : convert,reason = 'Unspecified'):
        if member == ctx.author:
            return await ctx.send(f'You cannot mute yourself {boredemoji}')
        check = False
        for i in member.roles:
            if i in ctx.author.roles[1:]:
                check = True

        if(check):
            return await ctx.send('You cannot tempmute a Moderator/Admin')
        thetime = times
        end = datetime.datetime.utcnow() + datetime.timedelta(seconds=times)
        if times == -1:
            await ctx.send('Time error.')
        elif times == -2:
            await ctx.send('Time error.')
        em = discord.Embed(
            timestamp=end,
            description=f"{member.mention} has been muted for `{thetime}`\n\n**Reason:** {reason}",
            color=ctx.author.colour
        
        )
        
        em.set_author(name=f"Muted",icon_url = ctx.author.avatar_url)
        em.set_footer(text=f"Muted until ")

        role = (discord.utils.get(member.guild.roles, name='Muted'))
        roles = (discord.utils.get(member.guild.roles, name='muted'))
        try:
            try:
                await member.add_roles(discord.utils.get(member.guild.roles, name='Muted'))
                await ctx.send(embed=em)
                await asyncio.sleep(times)
                await member.remove_roles(discord.utils.get(member.guild.roles, name='Muted'))
                await ctx.send(f'Member has unmuted because already {thetime}')
                for channel in ctx.guild.channels:
                    await channel.set_permissions(role, send_messages=False)
            except:
                try:
                    await member.add_roles(discord.utils.get(member.guild.roles, name='muted'))
                    await ctx.send(embed=em)
                    await asyncio.sleep(times)
                    await member.remove_roles(discord.utils.get(member.guild.roles, name='muted'))
                    await ctx.send(f'Member has unmuted because already {thetime}')
                    await channel.set_permissions(roles, send_messages=False)
                except:
                    await ctx.send(f"I can't find the `muted role`. You can either make a role named `Muted` or use the `setup` command.")
                    return
        except Exception as e:
            await ctx.send(f"`{e}`")
    @commands.command(pass_context=True)
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.has_permissions(ban_members = True)
    @commands.guild_only()
    @commands.bot_has_guild_permissions(ban_members = True)
    async def tempban(self , ctx, member : discord.Member,times : convert,*,reason= None):
        if member == ctx.author:
            return await ctx.send(f'You cannot ban yourself {boredemoji}')
        if reason == None:
            reason = "No reason provided"
        check = False
        for i in member.roles:
            if i in ctx.author.roles[1:]:
                check = True

        if(check):
            return await ctx.send('You cannot tempban a Moderator/Admin')
        thetime = times
        end = datetime.datetime.utcnow() + datetime.timedelta(seconds=times)
        #kick Dm
        ems = discord.Embed(
            description=f"You got banned on {ctx.guild.name}!\n\n{ctx.author.name} Has banned you \n\n**Duration**: {thetime}\n\n`Reason = {reason}`",
            timestamp=end,
            color=ctx.author.colour
        
        )
        ems.set_footer(text=f"Banned until ")
        ems.set_author(name=f"Banned",icon_url = ctx.author.avatar_url)
        #Kick Message
        em = discord.Embed(
            description=f"{ctx.author.mention} Has banned member named : {member.name} <a:BlackVerifyCheck:774476123878457354>\n\n**Duration**: {thetime}\n\n`Reason = {reason}`",
            timestamp=end,
            color=ctx.author.colour
        
        )
        em.set_footer(text=f"Banned until ")
        em.set_author(name=f"Banned",icon_url = ctx.author.avatar_url)
        
        try:
            await member.ban(reason=reason)
            await ctx.channel.send(embed=em)
            await asyncio.sleep(times)
            await ctx.guild.unban(member)
            try:
                await member.send(embed=ems)
            except:
                await ctx.send(f"**{member.name}#{member.discriminator}** has their **DM**s closed.")
        except Exception as error:
            emd = discord.Embed(
            description=f"**{ctx.author.mention}! <:OkNo:783666946573991987>**\n `Error : {error}`",
            color=ctx.author.colour
        
        )
        emd.set_author(name=f"Error :",icon_url = f'{ctx.author.avatar_url}')
        await ctx.send(embed=emd)
    @commands.command(aliases=["checkwarn"])
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def checkwarns(self,ctx, *,member: discord.Member):
        user = member
        guild = ctx.guild
        with open("reports.json", "r") as f:
            users = json.load(f)
            if str(guild.id) not in users:
                users[str(guild.id)] = {}
            if str(user.id) not in users[str(guild.id)]:
                users[str(guild.id)][str(user.id)] = []
            warning_count = len(users[str(guild.id)][str(user.id)])
            reason = users[str(guild.id)][str(user.id)]
            if len(users[str(guild.id)][str(user.id)]) == 0:
                return await ctx.send(f'{member.mention} Didn`t even get a single warn.')
        await ctx.send(f'{member.mention} has `{warning_count}` warnings!')
    @commands.command()
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def warn(self,ctx, member: discord.Member =None, *, reason = None):
            user = member
            guild = ctx.guild
            with open("reports.json", "r") as f:
                users = json.load(f)
            if str(guild.id) not in users:
                users[str(guild.id)] = {}
                with open("reports.json", "w") as f: 
                    json.dump(users, f)
            if str(user.id) not in users[str(guild.id)]:
                users[str(guild.id)][str(user.id)] = []
            warning_count = len(users[str(guild.id)][str(user.id)])
            users[str(guild.id)][str(user.id)].append({str(warning_count+1) : reason})
            with open("reports.json", "w") as f: 
                json.dump(users, f)
            await ctx.send(f'{member.mention} has been warned\n\nReason = `{reason}`')
            try:
                await member.send(f'You have been warned in {ctx.guild}\n\nReason = `{reason}`')
            except:
                pass

def setup(bot):
    bot.add_cog(Automod(bot))