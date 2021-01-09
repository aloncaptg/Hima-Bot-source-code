import discord
import os
import asyncio
import datetime
import random
import json
from discord.ext import commands




emcolor = 0x777777
ercolor = 0xff0000

class GiveawayCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['gcreate'])
    @commands.guild_only()              
    @commands.has_permissions(manage_messages=True)
    async def gstart(self, ctx):
        with open("prefixes.json", "r") as f:
            prefixes = json.load(f)

            try:
                prefix = prefixes[str(ctx.guild.id)]
            except:
                prefix = 'a!'
        answers = []
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        await ctx.channel.send(embed=discord.Embed(
            description=f'Which channel should giveaway hosted in? , **Example : **{ctx.channel.mention}',
            color=emcolor
        ))
        try:
            msg = await self.bot.wait_for('message', timeout=45.0, check=check)
        except asyncio.TimeoutError:
            await ctx.message.delete()
            #await a1.delete()
            await ctx.channel.send(embed=discord.Embed(
                title='Error',
                description=f'Times out, You ran out of time. \n\nTry again by typing `{prefix}gstart`',
                color=emcolor
            ))
            return
        else:
            answers.append(msg.content)
        await ctx.channel.send(embed=discord.Embed(
            description=f'What is the giveaway duration? , **Example : **`| 15s | 2m | 1h | 13d |.`',
            color=emcolor))
        try:
            msg = await self.bot.wait_for('message', timeout=45.0, check=check)
        except asyncio.TimeoutError:
            await ctx.channel.send(embed=discord.Embed(
                title='Error',
                description=f'Times out, You ran out of time. \n\nTry again by typing `{prefix}gstart`',
                color=emcolor))
            return
        else:
            answers.append(msg.content)
        await ctx.channel.send(embed=discord.Embed(
            description=f'What Is The Giveaway Prize?',
            color=emcolor))
        try:
            msg = await self.bot.wait_for('message', timeout=45.0, check=check)
        except asyncio.TimeoutError:
            await ctx.channel.send(embed=discord.Embed(
                title='Error',
                description=f'Times out, You ran out of time. \n\nTry again by typing `{prefix}gstart`',
                color=emcolor))
            return
        else:
            answers.append(msg.content)
        def check2(message):
            try:
                int(message.content)
                return True
            except ValueError:
                return False

        await ctx.channel.send(embed=discord.Embed(
            description=f'How many winners do you want for this giveaway. (max: 25)',
            color=emcolor))
        try:
            msg = await self.bot.wait_for('message', timeout=45.0, check=check2)
        except asyncio.TimeoutError:
            await ctx.channel.send(embed=discord.Embed(
                title='Error',
                description=f'Times out, You ran out of time. \n\nTry again by typing `{prefix}gstart`',
                color=emcolor))
            return
        else:
            answers.append(msg.content)
        try:
            c_id = int(answers[0][2:-1])
        except:
            await ctx.channel.send(
                f"You didn't metion channel properly, \n**Example : **{ctx.channel.mention}. \n\nYou can  try again by typing `{prefix}giveaway`")
            return
        def convert(time):
            time = time.lower()
            pos = ['s', 'm', 'h', 'd']
            time_dict = {'s': 1, 'm': 60, 'h': 3600, 'd': 3600 * 24}
            unit = time[-1]
            if unit not in pos:
                return -1
            try:
                val = int(time[:-1])
            except:
                return -2
            return val * time_dict[unit]
        channel = self.bot.get_channel(c_id)
        time = convert(answers[1])
        if time == -1:
            await ctx.channel.send(
                f"The time is not integer please enter time with integer next time\n**Example : **`| 15s | 2m | 1h | 13d |.` \n\nYou can try again by typing `{prefix}giveaway`")
            return
        elif time == -2:
            await ctx.channel.send(
                f"You didn't answer time with proper unit, Please enter time with proper unit next time\n**Example : **`| 15s | 2m | 1h | 13d |.` \n\nYou can  try again by typing `{prefix}giveaway`")
            return
        end = datetime.datetime.utcnow() + datetime.timedelta(seconds=time)
        prize = answers[2]
        if int(answers[3]) < 25:
            win_amount = int(answers[3])
        else:
            win_amount = 25
        embed = discord.Embed(
            description=f"**Prize??? :🎉  {prize}  🎉**\n**React 🎉 To Join the giveaway**\n\n**Hosted By : {ctx.author.mention}**\n\n**Time remaining : {answers[1]}**",
            colour=discord.Color.green())
        embed.set_author(name=f"Giveaway!",icon_url = "https://cdn.discordapp.com/attachments/743425064921464833/767981650070994984/86c9a4dde5bb348b53f2fb7ff099e9d5-square-wrapped-gift-box-by-vexels.png")
        embed.set_footer(text = f"Ends {answers[1]} from now!")
        msg = await channel.send(embed=embed)
        await msg.add_reaction("🎉")
        
        await ctx.send(ctx.author.mention, embed=discord.Embed(description=f"<a:BlackVerifyCheck:774476123878457354> Successfully started giveaway in {channel.mention}"))
        
        await asyncio.sleep(time)
        
        msg2 = await channel.fetch_message(msg.id)
        
        users = await msg2.reactions[0].users().flatten()
        users.pop(users.index(self.bot.user))
        
        winners = []
        for i in range(win_amount):
            i = i
            winners.append(random.choice(users).mention)
        embed2 = discord.Embed(
            description=f"**React didnt do anything , Except host Want to reroll the giveaway.**\n\nHosted by: {ctx.author.mention}\n\nValid Entries: {len(users)}\nWinners: \n"+'\n'.join(winners)+"\n",
            colour=emcolor,
            timestamp=end)
        embed2.set_author(name='Giveaway ended', icon_url="https://cdn.discordapp.com/attachments/743425064921464833/767981650070994984/86c9a4dde5bb348b53f2fb7ff099e9d5-square-wrapped-gift-box-by-vexels.png")
        embed2.set_footer(text="Ended at")
        await channel.send(f"🎊 **Congratulations** {', '.join(winners)}! , You have won the prize , Prize : {prize}**\n\n**__{msg.jump_url}__**")
        await msg.edit(embed=embed2)

    @commands.command(aliases=['greroll'])
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def reroll_giveaway(self, ctx, channel: discord.TextChannel, id_: int):
        try:
            msg2 = await channel.fetch_message(id_)
        except:
            await ctx.channel.send("**Error:** ID was entered incorrectly.")
            return
        users = await msg2.reactions[0].users().flatten()
        users.pop(users.index(self.bot.user))
        winner = random.choice(users)
        emb = discord.Embed(
            description=f"Successfully re-rolled giveaway in {channel.mention}",
            color=discord.Color.green())
        await ctx.send(embed=emb)
        await channel.send(f"🎊 **Congratulations** {winner.mention}! You are the new winner!")

    @commands.command(aliases=['gend'])
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def end_giveaway(self, ctx, channel: discord.TextChannel, id_: int):
        try:
            msg2 = await channel.fetch_message(id_)
        except:
            await ctx.channel.send("**Error:** ID was entered incorrectly.")
            return
        users = await msg2.reactions[0].users().flatten()
        users.pop(users.index(self.bot.user))
        winner = random.choice(users)
        emb = discord.Embed(
            description=f"Successfully ended giveaway in {channel.mention}",
            color=discord.Color.green())
        await ctx.send(embed=emb)
        await channel.send(f"🎊 **Congratulations** {winner.mention}! You have won the giveaway!")

def setup(client):
    client.add_cog(GiveawayCommands(client))