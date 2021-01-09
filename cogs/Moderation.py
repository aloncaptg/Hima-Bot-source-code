import discord
import os
import asyncio
import datetime
import asyncio
from discord.ext import commands
from important import boredemoji,yesemoji
prefix = 'c!'

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True)
    @commands.guild_only()
    @commands.has_permissions(ban_members = True)
    async def unban(self, ctx, *, member):
        try:
            if '#' in str(member):
                banned_users = await ctx.guild.bans()
                member_name, member_discriminator = member.split('#')

                for ban_entry in banned_users:
                    user = ban_entry.user

                    if (user.name, user.discriminator) == (member_name, member_discriminator):
                        try:
                            await ctx.guild.unban(user)
                            await ctx.send(f"{ctx.author.mention}, I have unbanned **{user}**.")
                            return
                        except Exception as e:
                            await ctx.send(f"```{e}```")
            else:
                userid = int(member)
                user = await discord.utils.get(discord.Member, id=userid)
                try:
                    await ctx.guild.unban(user)
                    await ctx.send(f"{ctx.author.mention}, I have unbanned {user}.")
                    return
                    
                except Exception as e:
                    await ctx.send(f"```{e}```")
        except Exception as e:
            await ctx.send("```{}```".format(e))

    @commands.command(pass_context = True)
    @commands.guild_only()
    @commands.has_guild_permissions(mute_members=True)
    async def mute(self, ctx, member: discord.Member):
        if member == ctx.author:
            return await ctx.send(f'You cannot mute yourself {boredemoji}')
        check = False
        for i in member.roles:
            if i in ctx.author.roles[1:]:
                check = True

        if(check):
            return await ctx.send('You cannot mute a Moderator/Admin')
        em = discord.Embed(
            description=f"{ctx.author.mention} `Has muted member named : {member.name}`{yesemoji}",
            color=ctx.author.colour
        
        )
        
        em.set_author(name=f"Muted",icon_url = ctx.author.avatar_url)
        role = (discord.utils.get(member.guild.roles, name='Muted'))
        try:
            try:
                await member.add_roles(discord.utils.get(member.guild.roles, name='Muted'))
                for channel in ctx.guild.channels:
                    await channel.set_permissions(role, send_messages=False)
            except:
                try:
                    await member.add_roles(discord.utils.get(member.guild.roles, name='muted'))
                except:
                    await ctx.send(f"I can't find the `muted role`. You can either make a role named `Muted` or use the `setup` command.")
                    return
            await ctx.send(embed=em)
        except Exception as e:
            await ctx.send(f"`{e}`")
            #await ctx.send(f"I can't find the `muterole`. You can either make a role named `Muted` or use the `{prefix}setup` command.")

    @commands.command(pass_context=True)
    @commands.guild_only()
    @commands.has_guild_permissions(mute_members=True)
    async def unmute(self, ctx, member: discord.Member):
        try:
            try:
                await member.remove_roles(discord.utils.get(member.guild.roles, name='Muted'))
            except:
                try:
                    await member.remove_roles(discord.utils.get(member.guild.roles, name='muted'))
                except:
                    await ctx.send(f"User is not muted.")
                    return
            await ctx.send(f"I have unmuted {member.mention} {yesemoji}")
        except Exception as e:
            await ctx.send(f"`{e}`")

    @commands.command(pass_context=True)
    @commands.guild_only()
    @commands.has_guild_permissions(manage_guild=True)
    async def setup(self, ctx):
        prgrs = 0.0

        a = await ctx.send(f"Setting up things... (Progress: `{prgrs}%`)")
        await ctx.send(f"Finding `Muted role`...")
        try:
            global muterole
            muterole = discord.utils.get(ctx.guild.roles, name='Muted')
            await ctx.send(f"Muted role found! (**{muterole.name}**)")
        except:
            try:
                muterole = discord.utils.get(ctx.guild.roles, name='muted')
                await ctx.send(f"Muterole found! (**{muterole.name}**)")
            except:
                await ctx.send("Muterole not found . Creating new role...")
                try:
                    role = await ctx.guild.create_role(name="Muted")
                    await asyncio.sleep(0.1)
                    prgrs = 23.4
                    await a.edit(content=f"Setting up things... (Progress: `{prgrs}%`)")
                    await ctx.send(f"Muted role created! (**{role.name}**)")
                    await asyncio.sleep(0.16)
                    await ctx.send(f"Setting Permissions for **{role.name}**...")
                    await asyncio.sleep(0.16)
                    try:
                        for channel in ctx.guild.channels:
                            await channel.set_permissions(role, send_messages=False)
                            await asyncio.sleep(0.16)
                        prgrs = 78.6
                        await a.edit(content=f"Setting up things... (Progress: `{prgrs}%`)")
                        await ctx.send(f"Permissions created for **{len(ctx.guild.channels)}** channels.")
                    except Exception as e:
                        await ctx.send(f"```{e}```")
                    await ctx.send("Assigning the created muterole as the main muterole...")
                    await asyncio.sleep(0.2)
                    prgrs = 100.0
                    await a.edit(content=f"Set up things. (Progress: `{prgrs}%`)")
                    await ctx.send(f"Saved! Setup finished. {yesemoji}")
                except Exception as e:
                    await ctx.send(f"`{e}`")
        await asyncio.sleep(0.16)
        await ctx.send(f"Setting Permissions for **{muterole.name}**...")
        await asyncio.sleep(0.16)
        try:
            for channel in ctx.guild.channels:
                await channel.set_permissions(muterole, send_messages=False)
                await asyncio.sleep(0.16)
            prgrs = 78.6
            await a.edit(content=f"Setting up things... (Progress: `{prgrs}%`)")
            await ctx.send(f"Permissions created for **{len(ctx.guild.channels)}** channels.")
        except Exception as e:
            await ctx.send(f'`{e}`')
        await ctx.send("Assigning the created Muted role as the main muted role...")
        await asyncio.sleep(0.2)
        prgrs = 100.0
        await a.edit(content=f"Set up things. (Progress: `{prgrs}%`)")
        await ctx.send(f"Saved! Setup finished. {yesemoji}")
    @commands.command(pass_context=True)
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.has_permissions(ban_members = True)
    @commands.guild_only()
    @commands.bot_has_guild_permissions(ban_members = True)
    async def ban(self , ctx, member : discord.Member,*,reason= 'No reason provided'):
        check = False
        for i in member.roles:
            if i in ctx.author.roles[1:]:
                check = True

        if(check):
            return await ctx.send('You cannot ban a moderator/admins')
        if member == ctx.author:
            return await ctx.send(f'You cannot ban yourself {boredemoji}')
        #kick Dm
        ems = discord.Embed(
            description=f"You got banned on {ctx.guild.name}!\n\n{ctx.author.name} Has banned you {yesemoji}\n\n`Reason = {reason}`",
            color=ctx.author.colour
        
        )
        
        ems.set_author(name=f"Banned",icon_url = ctx.author.avatar_url)
        #Kick Message
        em = discord.Embed(
            description=f"{ctx.author.mention} Has banned member named : {member.name} {yesemoji}\n\n`Reason = {reason}`",
            color=ctx.author.colour
        
        )
        
        em.set_author(name=f"Banned",icon_url = ctx.author.avatar_url)
        
        try:
            await member.ban(reason=reason)
            await ctx.channel.send(embed=em)
            try:
                await member.send(embed=ems)
            except:
                await ctx.send(f"**{member.name}#{member.discriminator}** has their **DM**s closed.")
        except Exception as error:
            await ctx.send(error)
    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.has_permissions(kick_members = True)
    @commands.bot_has_guild_permissions(kick_members = True)
    @commands.guild_only()
    async def kick(self ,ctx,member : discord.Member,*,reason= None):
        if reason == None:
            reason = "No reason provided"
        if member == ctx.author:
            return await ctx.send(f'You cannot mute yourself {boredemoji}')
        check = False
        for i in member.roles:
            if i in ctx.author.roles[1:]:
                check = True

        if(check):
            return await ctx.send('You cannot kick a Moderator/Admin')
        #kick Dm
        ems = discord.Embed(
            description=f"You got kicked on {ctx.guild.name}!\n\n{ctx.author.name} Has kicked you {yesemoji}\n\n`Reason = {reason}`",
            color=ctx.author.colour
        
        )
        
        ems.set_author(name=f"Kicked",icon_url = ctx.author.avatar_url)
        #Kick Message
        em = discord.Embed(
            description=f"{ctx.author.mention} Has kicked member named : {member.name} {yesemoji}\n\n`Reason = {reason}`",
            color=ctx.author.colour
        
        )
        
        em.set_author(name=f"Kicked",icon_url = ctx.author.avatar_url)
        
        try:
            await member.kick(reason=reason)
            await ctx.channel.send(embed=em)
            try:
                await member.send(embed=ems)
            except:
                await ctx.send(f"**{member.name}#{member.discriminator}** has their **DM**s closed.")
        except Exception as error:
            await ctx.send(error)
#MUTE COMMAND

    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.has_permissions(manage_nicknames = True)
    @commands.bot_has_guild_permissions(manage_nicknames = True)
    @commands.guild_only()
    async def rename(self ,ctx,member : discord.Member = None,*,Newnick):
        if member == None:
            member = ctx.author
        check = False
        for i in member.roles:
            if i in ctx.author.roles[1:]:
                check = True

        if(check):
            return await ctx.send('You cannot rename a Moderator/Admin')
        embed = discord.Embed(
            description=f"{ctx.author.mention} I've renamed {member} nick to {Newnick} {yesemoji}",
            color=ctx.author.colour
        
        )
        
        embed.set_author(name=f"Renamed",icon_url = f'{ctx.author.avatar_url}')
        #error

        try:
            await member.edit(nick=f"{Newnick}")
            await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send(e)

    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.has_permissions(manage_nicknames = True)
    @commands.bot_has_guild_permissions(manage_nicknames = True)
    @commands.guild_only()
    async def normalnick(self , ctx,*, member : discord.Member = None):
        if member == None:
            member = ctx.author
        check = False
        for i in member.roles:
            if i in ctx.author.roles[1:]:
                check = True

        if(check):
            return await ctx.send('You cannot rename a Moderator/Admin')
        embed = discord.Embed(
            description=f"`I have renamed {member} nick to {member.name}` {yesemoji}",
            color=ctx.author.colour
        
        )
        embed.set_author(name=f"{ctx.author.name}",icon_url = f'{ctx.author.avatar_url}')
        #error

        try:
            await member.edit(nick=f"{member.name}")
            await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send(e)

    @commands.command(aliases=['nuked'])
    @commands.cooldown(1, 500, commands.BucketType.user)
    @commands.has_permissions(manage_channels = True)
    @commands.bot_has_guild_permissions(manage_channels = True)
    @commands.guild_only()
    async def nuke(self ,ctx,*,channel : discord.TextChannel = None):
        if channel == None:
            new_channel = await ctx.channel.clone()
            await ctx.channel.delete()
            await new_channel.send("Channel nuked.\nhttps://tenor.com/view/explosion-mushroom-cloud-atomic-bomb-bomb-boom-gif-4464831")
        else:
            new_channel = await channel.clone()
            await channel.delete()
            await ctx.channel.send(f"Nuked {new_channel.mention} <:tick:781706203117912085>")
        await channel.send('https://tenor.com/view/explosion-nuke-boom-nuclear-gif-5791468\nNuked  the channel.')
    @commands.command(aliases=['setdelay'])
    @commands.has_guild_permissions(manage_channels=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def slowmode(self, ctx, time : int=0):
        if time < 0:
            await ctx.send('Give a positive number.')
            return
        try:
            if time > 21600:
                await ctx.send('Number is too large. You can only have a maximum time of `21600` seconds (6 Hours)')
            else:
                await ctx.channel.edit(slowmode_delay=time)
                await ctx.send(f'The channel {ctx.channel.mention} now has a slowmode of {time} seconds')
        except Exception:
            await ctx.send('Not a number!')

    @commands.command(pass_context=True)
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.guild_only()
    @commands.has_permissions(manage_roles = True)
    @commands.bot_has_guild_permissions(manage_roles = True)
    async def giverole(self, ctx, user: discord.Member, role: discord.Role):
        try:
            await user.add_roles(role)
            await ctx.send(f"{ctx.author.mention}, gived member role named: {role.mention}")
        except Exception as e:
            await ctx.send(e)    
    @commands.command(pass_context=True)
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.guild_only()
    @commands.has_permissions(manage_roles = True)
    @commands.bot_has_guild_permissions(manage_roles = True)
    async def removerole(self, ctx, user: discord.Member, role: discord.Role):
        try:
            await user.remove_roles(role)
            await ctx.send(f"{ctx.author.mention}, removed member role named: {role.mention}")
        except Exception as e:
            await ctx.send(e)        
    @commands.command(aliases=['clear'])
    @commands.guild_only()
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.has_permissions(manage_messages = True)
    @commands.bot_has_guild_permissions(manage_messages = True)
    async def purge(self ,ctx, amount: int):
        try:
                await ctx.channel.purge(limit=amount+1)
                embed = discord.Embed(
                    description=f"{ctx.author.mention}, Deleted `{amount}` messages! <a:BlackVerifyCheck:774476123878457354>",
                    color=ctx.author.colour
                    
                    )
                    
                embed.set_author(name=f"Purged",icon_url = f'{ctx.author.avatar_url}')
                await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send(f'`{e}`')

    #channel.
    @commands.command(aliases=['cchannel'])
    @commands.guild_only()
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.has_permissions(manage_channels = True)
    @commands.bot_has_guild_permissions(manage_channels = True)
    async def createchannel(self ,ctx,*,channel):
        await ctx.guild.create_text_channel(f'{channel}')
        embed = discord.Embed(
            description=f"{ctx.author.mention}, Created channel named : `{channel}` {yesemoji}",
            color=ctx.author.colour
        
        )
        
        embed.set_author(name=f"{ctx.author.name}",icon_url = f'{ctx.author.avatar_url}')
        await ctx.send(embed=embed)
    @commands.command(aliases=['createvoicechannel'])
    @commands.guild_only()
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.has_permissions(manage_channels = True)
    @commands.bot_has_guild_permissions(manage_channels = True)
    async def createvc(self ,ctx,*,channel):
        await ctx.guild.create_voice_channel(f'{channel}')
        embed = discord.Embed(
            description=f"{ctx.author.mention}, Created channel named : `{channel}` {yesemoji}",
            color=ctx.author.colour
        
        )
        
        embed.set_author(name=f"{ctx.author.name}",icon_url = f'{ctx.author.avatar_url}')
        await ctx.send(embed=embed)
    @commands.command(aliases=['deletech'])
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.has_permissions(manage_channels = True)
    @commands.guild_only()
    @commands.bot_has_guild_permissions(manage_channels = True)
    async def deletechannel(self ,ctx,*,channel : discord.TextChannel):
        await channel.delete()
        embed = discord.Embed(
            description=f"Deleted channel named: `{channel}` {yesemoji}",
            color=ctx.author.colour
        
        )
        
        embed.set_author(name=f"{ctx.author.name}",icon_url = f'{ctx.author.avatar_url}')
        await ctx.send(embed=embed)
    @commands.command(aliases=['deletevc'])
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.has_permissions(manage_channels = True)
    @commands.guild_only()
    @commands.bot_has_guild_permissions(manage_channels = True)
    async def deletevoichannel(self ,ctx,*,channel : discord.VoiceChannel):
        await channel.delete()
        embed = discord.Embed(
            description=f"Deleted channel named: `{channel}` {yesemoji}",
            color=ctx.author.colour
        
        )
        
        embed.set_author(name=f"{ctx.author.name}",icon_url = f'{ctx.author.avatar_url}')
        await ctx.send(embed=embed)
    
    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def lock(self, ctx, channel: discord.TextChannel=None):
        channel = channel or ctx.channel

        if ctx.guild.default_role not in channel.overwrites:
            overwrites = {
            ctx.guild.default_role: discord.PermissionOverwrite(send_messages=False)
            }
            await channel.edit(overwrites=overwrites)
            await ctx.send("**The channel {} has successfully been locked!**".format(ctx.channel.mention))
        elif channel.overwrites[ctx.guild.default_role].send_messages == True or channel.overwrites[ctx.guild.default_role].send_messages == None:
            overwrites = channel.overwrites[ctx.guild.default_role]
            overwrites.send_messages = False
            await channel.set_permissions(ctx.guild.default_role, overwrite=overwrites)
            await ctx.send("**The channel {} has successfully been locked!**".format(ctx.channel.mention))
        else:
            overwrites = channel.overwrites[ctx.guild.default_role]
            overwrites.send_messages = True
            await channel.set_permissions(ctx.guild.default_role, overwrite=overwrites)
            await ctx.send('**The channel {} has now been unlocked!**'.format(ctx.channel.mention))
    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def unlock(self, ctx, channel: discord.TextChannel=None):
        channel = channel or ctx.channel

        if ctx.guild.default_role not in channel.overwrites:
            overwrites = {
            ctx.guild.default_role: discord.PermissionOverwrite(send_messages=True)
            }
            await channel.edit(overwrites=overwrites)
            await ctx.send("**The channel {} has successfully been locked!**".format(ctx.channel.mention))
        elif channel.overwrites[ctx.guild.default_role].send_messages == True or channel.overwrites[ctx.guild.default_role].send_messages == None:
            overwrites = channel.overwrites[ctx.guild.default_role]
            overwrites.send_messages = True
            await channel.set_permissions(ctx.guild.default_role, overwrite=overwrites)
            await ctx.send("**The channel {} has successfully been locked!**".format(ctx.channel.mention))
        else:
            overwrites = channel.overwrites[ctx.guild.default_role]
            overwrites.send_messages = True
            await channel.set_permissions(ctx.guild.default_role, overwrite=overwrites)
            await ctx.send('**The channel {} has now been unlocked!**'.format(ctx.channel.mention))
def setup(bot):
    bot.add_cog(Moderation(bot))