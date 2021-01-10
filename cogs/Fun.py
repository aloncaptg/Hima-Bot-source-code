import discord
import os
import asyncio
import datetime
import random
import json
import aiohttp
import pyfiglet
from PIL import Image
from io import BytesIO
import random
import datetime
import time
from important import emojino
import discord
from discord.ext import commands
from discord.ext.commands import BucketType, cooldown
import os
import requests
import aiohttp

from Others import IMG,CO,gender
Co = CO
Pfp = os.environ.get('PFP')
from discord.ext import commands
emcolor = 0x777777
ercolor = 0xff0000
class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['8ball'])
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def eight_ball_answr(self ,ctx, *,question):
        answers = [
        "As I see it, yes.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don’t count on it.",
        "It is certain.",
        "It is decidedly so.",
        "Most likely.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Outlook good.",
        "Reply hazy, try again.",
        "Signs point to yes.",
        "Very doubtful.",
        "Without a doubt.",
        "Yes.",
        "Yes – definitely.",
        "You may rely on it."
        ]
        

        embed = discord.Embed(
            description=f"\n\nQuestion Asked = \n\n`{question}`\n\nAnswer = {random.choice(answers)}",
            color=ctx.author.colour
        )
        embed.set_author(name=f"8ball",icon_url = f'{Pfp}')
        embed.set_thumbnail(url=f'{Pfp}')

        await ctx.send(embed=embed)
    
    

    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def ship(self,ctx,member : discord.Member):
        if member == None:
            member = ctx.author
        
        number1 = random.randint(1,20)
        number2 = random.randint(20,30)
        number3 = random.randint(30,50)
        number4 = random.randint(50,70)
        number5 = random.randint(70,100)
        answers = [
        f'{number1}/100',
        f'{number2}/100',
        f'{number3}/100',
        f'{number4}/100',
        f'{number5}/100'
        ]
        embed = discord.Embed(
            description=f"💗 **MATCHMAKING** 💗\n\n{random.choice(answers)}",
            color= discord.Colour.red()
        
        )
        embed.add_field(name="Member 2",value=f"**{member.mention}**", inline = True)
        embed.add_field(name="Member 1",value=f"**{ctx.author.mention}**", inline = True)
        await ctx.send(embed=embed)
        wanted = Image.open("ok.png")

        asset = member.avatar_url_as(format=None, static_format='png', size = 128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)

        pfp = pfp.resize((249,245))

        wanted.paste(pfp, (8,132))

        d = ctx.author.avatar_url_as(format=None, static_format='png', size = 128)
        data = BytesIO(await d.read())
        pfps = Image.open(data)

        pfps = pfp.resize((249,245))

        wanted.paste(pfp, (581,135))
        
        wanted.save(f'ship.png')

        await ctx.send(file=discord.File(f'ship.png'))
    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def howweeb(self,ctx,*,member : discord.Member = None):
        if member == None:
            member = ctx.author
        number1 = random.randint(1,20)
        number2 = random.randint(20,30)
        number3 = random.randint(30,50)
        number4 = random.randint(50,70)
        number5 = random.randint(70,100)
        answers = [
        f'{number1}/100',
        f'{number2}/100',
        f'{number3}/100',
        f'{number4}/100',
        f'{number5}/100'
        ]
        embed = discord.Embed(
            title='Weeb',
            description=f"{ctx.author} are {random.choice(answers)} weeb",
            color= discord.Colour.red()
        
        )
        await ctx.send(embed=embed)

    @commands.command(aliases=['slots', 'bet'])
    @cooldown(1, 5, BucketType.user)
    async def slot(self, ctx):
        emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
        a = random.choice(emojis)
        b = random.choice(emojis)
        c = random.choice(emojis)

        slotmachine = f"**[ {a} | {b} | {c} ]\n{ctx.author.name}**,"

        if a == b == c:
            await ctx.send(embed=discord.Embed(title='Slot Machine:',
                                               description=slotmachine + ' has gotten 3/3 he wins!!! :tada:',
                                               colour=discord.Colour.red()))
        elif (a == b) or (a == c) or (b == c):
            await ctx.send(embed=discord.Embed(title='Slot Machine:',
                                               description=slotmachine + ' has gotten 2/3 he wins!!! :tada:',
                                               colour=discord.Colour.red()))
        else:
            await ctx.send(embed=discord.Embed(title='Slot Machine:',
                                               description=slotmachine + ' has gotten 0/3 he looses. :pensive:',
                                               colour=discord.Colour.red()))

    @commands.command(aliases=['Latency'])
    @cooldown(1, 5, BucketType.user)
    async def ping(self, ctx):
        msg = await ctx.send("`Bot Latency...`")
        times = []
        counter = 0
        embed = discord.Embed(title="More Information:", description="Pings from BOT to YOU::", colour=discord.Color.red())
        for _ in range(3):
            counter += 1
            start = time.perf_counter()
            await msg.edit(content=f"Trying Ping... {counter}/3")
            end = time.perf_counter()
            speed = round((end - start) * 1000)
            times.append(speed)
            if speed < 160:
                embed.add_field(name=f"Ping {counter}:", value=f"🟢 | {speed}ms", inline=True)
            elif speed > 170:
                embed.add_field(name=f"Ping {counter}:", value=f"🟡 | {speed}ms", inline=True)
            else:
                embed.add_field(name=f"Ping {counter}:", value=f"🔴 | {speed}ms", inline=True)
        embed.set_author(name="🏓    PONG    🏓", icon_url="https://img.icons8.com/ultraviolet/40/000000/table-tennis.png")
        embed.add_field(name="Bot Latency", value=f"{round(self.bot.latency * 1000)}ms", inline=True)
        embed.add_field(name="Normal Speed", value=f"{round((round(sum(times)) + round(self.bot.latency * 1000))/4)}ms")
        embed.set_footer(text=f"Total estimated elapsed time: {round(sum(times))}ms")
        await msg.edit(content=f":ping_pong: **{round((round(sum(times)) + round(self.bot.latency * 1000))/4)}ms**", embed=embed)

    @commands.command()
    @commands.cooldown(1, 5, BucketType.guild)
    async def useless(self, ctx):
        user = ctx.author
        await ctx.send('Hello ' + user.name)
        await ctx.send('Type `press` to press the useless button.')

        def check(m):
            if m.author.id == user.id and m.content.lower() == 'press':
                return True
            return False
        try:
            await self.bot.wait_for('message', timeout=10.0, check=check)
            await ctx.send(embed=discord.Embed(
                title='Button has been pressed!',
                description='Button has been pressed by {}'.format(ctx.author),
                colour=discord.Colour.green()
            ).set_image(url='http://66.media.tumblr.com/d1483298e112b3bf08d35a2bd345a097/tumblr_n5ig6cjyk81t2csv8o2_500.gif'))
        except asyncio.TimeoutError:
            ctx.command.reset_cooldown(ctx)
            return await ctx.send(embed=discord.Embed(
                description='<a:nope:787764352387776523> Button press has failed.',
                colour=discord.Colour.red()
            ))

    @commands.command(aliases=['le'])
    @commands.cooldown(1, 5, BucketType.user)
    async def lifeexpectancy(self, ctx, user: discord.Member = None):
        user = user or ctx.author
        number1 = random.randint(1,20)
        number2 = random.randint(20,30)
        number3 = random.randint(30,50)
        number4 = random.randint(50,70)
        number5 = random.randint(90,150)
        answers = [
        f'{number1}/100',
        f'{number2}/100',
        f'{number3}/100',
        f'{number4}/100',
        f'{number5}/100'
        ]
        counter=random.choice(answers)
        embed = discord.Embed(
            title="{}'s life expectancy is:".format(user),
            color=discord.Color.red(),
            description=f'**{counter} yrs old!**'
        )
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 5, BucketType.user)
    async def bweight(self, ctx, user: discord.Member = None):
        user = user or ctx.author
        weight = ['Pinweight\t(44 - 46 Kg)', 'Light Flyweight\t(Below 48Kg)', 'Flyweight\t(49 - 52 Kg)', 'Bantamweight\t(52 - 53.5 Kg)', 'Featherweight\t(54 - 57 Kg)', 'Lightweight\t(59 - 61 Kg)', 'Lighter welterweight\t(54 - 67 Kg)', 'Welterweight\t(64 - 69 Kg)', 'Middleweight\t(70 - 73 Kg)', 'Light heavyweight\t(76 - 80 Kg)', 'Heavyweight\t(Above 81 Kg)', 'Super Heavyweight\t(Above 91 Kg)']
        choice = random.choice(weight)
        embed = discord.Embed(
            title='What is {} boxing weight?'.format(user),
            color=discord.Color.red(),
            description=f'{choice}'
        )
        await ctx.send(embed=embed)

    @commands.command(aliases=['Weight', 'WI'])
    @commands.cooldown(1, 10, BucketType.user)
    async def weighin(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author
        number1 = random.randint(1,20)
        number2 = random.randint(20,30)
        number3 = random.randint(30,50)
        number4 = random.randint(50,70)
        number5 = random.randint(70,200)
        answers = [
        f'{number1}/100',
        f'{number2}/100',
        f'{number3}/100',
        f'{number4}/100',
        f'{number5}/100'
        ]
        weight = random.choice(answers)
        embed = discord.Embed(
            title='How much do {} weigh?'.format(user),
            color=discord.Color.red(),
            description=f'**`{weight}` Kg**'
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def beer(self, ctx, user: discord.Member = None, *, reason: commands.clean_content = ""):
        if not user or user.id == ctx.author.id:
            return await ctx.send(f"**{ctx.author.mention}**: fieeeeestaaa!🎉🍺")
        if user.bot:
            return await ctx.send(f"You that lonely? Give an actual person not a bot.")
        beer_offer = f"**{user.mention}**, You have a 🍺 offered from **{ctx.author.mention}**"
        beer_offer = beer_offer + f"\n\n**Reason:** {reason}" if reason else beer_offer
        msg = await ctx.send(beer_offer)

        def reaction_check(m):
            if m.message_id == msg.id and m.user_id == user.id and str(m.emoji) == "🍻":
                return True
            return False

        try:
            await msg.add_reaction("🍻")
            await self.bot.wait_for('raw_reaction_add', timeout=10.0, check=reaction_check)
            await msg.edit(content=f"**{user.mention}** and **{ctx.author.mention}** Are enjoying a lovely 🍻")
            await msg.clear_reactions()
        except asyncio.TimeoutError:
            await msg.delete()
            await ctx.send(f"well it seems **{user.name}** didn't want a beer with **{ctx.author.name}** ;-;")
        except discord.Forbidden:
            beer_offer = f"**{user.name}**, you have a 🍺 from **{ctx.author.name}**"
            beer_offer = beer_offer + f"\n\n**reason:** {reason}" if reason else beer_offer
            await msg.edit(content=beer_offer)

    @commands.command()
    @commands.cooldown(1, 10, BucketType.user)
    async def reverse(self, ctx, *args):
        if not args:
            ctx.command.reset_cooldown(ctx)
            return await ctx.send('Give me something to reverse!')
        args = ' '.join(map(str, args))
        await ctx.send(embed=discord.Embed(
            description=args[::-1],
            colour=discord.Colour.red()
        ))

    @commands.command()
    @cooldown(1, 10, BucketType.user)
    async def simp(self, ctx, user: discord.Member = None):
        user = user or ctx.author
        number1 = random.randint(1,20)
        number2 = random.randint(20,30)
        number3 = random.randint(30,50)
        number4 = random.randint(50,70)
        number5 = random.randint(70,101)
        answers = [
        f'{number1}/100',
        f'{number2}/100',
        f'{number3}/100',
        f'{number4}/100',
        f'{number5}/100'
        ]
        simp=random.choice(answers)
        embed = discord.Embed(
            title=f'How much of a simp are they?',
            color=discord.Color.red()
        )
        embed.add_field(name='**Simp**', value=f'{user.display_name} is {simp} simp')
        await ctx.send(embed=embed)

    @commands.command()
    @cooldown(1, 10, BucketType.user)
    async def retard(self, ctx, user: discord.Member = None):
        user = user or ctx.author
        number1 = random.randint(1,20)
        number2 = random.randint(20,30)
        number3 = random.randint(30,50)
        number4 = random.randint(50,70)
        number5 = random.randint(70,100)
        answers = [
        f'{number1}/100',
        f'{number2}/100',
        f'{number3}/100',
        f'{number4}/100',
        f'{number5}/100'
        ]
        retard = random.choice(answers)
        embed = discord.Embed(
            title='',
            color=discord.Color.red()
        )
        embed.add_field(name='**Retard**', value=f'{user.display_name} is {retard} retarded')
        await ctx.send(embed=embed)

    @commands.command()
    @cooldown(1, 10, BucketType.user)
    async def human(self, ctx, user: discord.Member = None):
        user = user or ctx.author
        embed = discord.Embed(
            title='',
            color=discord.Color.red()
        )
        number1 = random.randint(1,20)
        number2 = random.randint(20,30)
        number3 = random.randint(30,50)
        number4 = random.randint(50,70)
        number5 = random.randint(70,100)
        answers = [
        f'{number1}/100',
        f'{number2}/100',
        f'{number3}/100',
        f'{number4}/100',
        f'{number5}/100'
        ]
        human = random.choice(answers)
        embed.add_field(name='**Human**', value=f'{user.display_name} is {human} human')
        await ctx.send(embed=embed)

    @commands.command()
    @cooldown(1, 10, BucketType.user)
    async def buff(self, ctx, user: discord.Member = None):
        user = user or ctx.author
        embed = discord.Embed(color=discord.Color.red())
        embed.add_field(name='**Buffness**', value=f'{user.display_name} is {random.randint(0, 101)}/100 Buff :muscle:')
        await ctx.send(embed=embed)

    @commands.command()
    @cooldown(1, 10, BucketType.user)
    async def waifu(self, ctx, user: discord.Member = None):
        user = user or ctx.author
        embed = discord.Embed(
            color=discord.Color.red()
        )
        embed.add_field(name='**Waifu**', value=f'{user.display_name} is {random.choice(IMG.Number1)}')
        await ctx.send(embed=embed)

    @commands.command()
    @cooldown(1, 10, BucketType.user)
    async def dad(self, ctx, *, message: str = None):
        if message == None:
            ctx.command.reset_cooldown(ctx)
            return await ctx.send('I cant name you anything.')
        embed = discord.Embed(
            color=discord.Color.red()
        )
        embed.add_field(name='Daddo Machine 9000', value=f'Hello {message}, Im Dad')
        await ctx.send(embed=embed)

    @commands.command()
    @cooldown(1, 10, BucketType.user)
    async def howgay(self, ctx, user: discord.Member = None):
        user = user or ctx.author
        number1 = random.randint(1,20)
        number2 = random.randint(20,30)
        number3 = random.randint(30,50)
        number4 = random.randint(50,70)
        number5 = random.randint(70,100)
        answers = [
        f'{number1}/100',
        f'{number2}/100',
        f'{number3}/100',
        f'{number4}/100',
        f'{number5}/100'
        ]
        gay = random.choice(answers)
        embed = discord.Embed(
            color=random.randint(0x000000, 0xFFFFFF),
            description=f'{user.display_name} is {gay} gay :rainbow_flag:'
        )
        await ctx.send(embed=embed)

    @commands.command(aliases=['jokes'])
    @cooldown(1, 10, BucketType.user)
    async def joke(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    'https://sv443.net/jokeapi/v2/joke/Miscellaneous?blacklistFlags=nsfw,religious,political,racist,sexist&type=twopart') as r:
                r = await r.json()
        embed = discord.Embed(colour=random.randint(0x000000, 0xFFFFFF), timestamp=datetime.datetime.utcnow())
        embed.add_field(name='Setup:', value=r['setup'])
        embed.add_field(name='Delivery:', value=r['delivery'], inline=False)
        embed.set_footer(text='Prompted by {}'.format(ctx.author), icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(aliases=['fact'])
    @cooldown(1, 10, BucketType.user)
    async def facts(self, ctx):
        embed = discord.Embed(
            title='**Fun Facts:**',
            color=discord.Color.teal()
        )
        embed.add_field(name='‏‏‎ ', value=f'{random.choice(Co.fact)}')
        await ctx.send(embed=embed)

    @commands.command(aliases=['gender'])
    @cooldown(1, 10, BucketType.user)
    async def genderfinder(self, ctx, user: discord.Member = None):
        user = user or ctx.author
        genders = random.choice(gender.gend)
        embed = discord.Embed(
            title=f"**{user.display_name}'s Gender!**",
            description=genders,
            color=discord.Color.magenta()
        )
        await ctx.send(embed=embed)


    @commands.command(name='IQ')
    @cooldown(1, 10, BucketType.user)
    async def iq(self, ctx, user: discord.Member = None):
        user = user or ctx.author
        iq = ['130 and above (Very Superior)',
              '120–129 (Superior)',
              '110–119 (High Average)',
              '90–109 (Average)',
              '80–89 (Low Average)',
              '70–79 (Borderline)',
              '69 and below	(Extremely Low)']
        e = discord.Embed(
            color=discord.Colour.red()
        )
        e.add_field(name='**IQ Machine 9000**', value=f'{user.display_name} IQ is {random.choice(iq)}')
        await ctx.send(embed=e)

    @commands.command(aliases=['Penis'], name='PP')
    @cooldown(1, 10, BucketType.user)
    async def pp(self, ctx, user: discord.Member = None):
        user = user or ctx.author
        former = ['8', 'D']
        for i in range(random.randrange(10)):
            former.insert(1, '=')
        e = discord.Embed(
        color=0x50C878
        
        )
        e.add_field(name="**{}'s penis is:**".format(user),
                    value=''.join(map(str, former)))
        await ctx.send(embed=e)

    @commands.command(aliases=['insult'])
    @cooldown(1, 10, BucketType.user)
    async def roast(self, ctx):
        A = ['You’re the reason God created the middle finger.',
             'You’re a grey sprinkle on a rainbow cupcake.',
             'If your brain was dynamite, there wouldn’t be enough to blow your hat off.',
             'You are more disappointing than an unsalted pretzel.',
             'Light travels faster than sound which is why you seemed bright until you spoke.',
             'We were happily married for one month, but unfortunately we’ve been married for 10 years.',
             'Your kid is so annoying, he makes his Happy Meal cry.',
             'You have so many gaps in your teeth it looks like your tongue is in jail.',
             'Your secrets are always safe with me. I never even listen when you tell me them.',
             'I’ll never forget the first time we met. But I’ll keep trying.',
             'I forgot the world revolves around you. My apologies, how silly of me.',
             'I only take you everywhere I go just so I don’t have to kiss you goodbye.',
             'Hold still. I’m trying to imagine you with personality.',
             'Our kid must have gotten his brain from you! I still have mine.',
             'Your face makes onions cry.',
             'The only way my husband would ever get hurt during an activity is if the TV exploded.',
             'You look so pretty. Not at all gross, today.',
             'Her teeth were so bad she could eat an apple through a fence.',
             'I’m not insulting you, I’m describing you.',
             'I’m not a nerd, I’m just smarter than you.',
             'Keep rolling your eyes, you might eventually find a brain.',
             'Your face is just fine but we’ll have to put a bag over that personality.',
             'You bring everyone so much joy, when you leave the room.',
             'I thought of you today. It reminded me to take out the trash.',
             'Don’t worry about me. Worry about your eyebrows.',
             'there is approximately 1,010,030 words in the language english, but i cannot string enough words together to express how much i want to hit you with a chair']

        await ctx.send(embed=discord.Embed(
            colour=discord.Colour.red(),
            description=random.choice(A)
        ).set_author(name=self.bot.user.display_name, icon_url=self.bot.user.avatar_url))

    @commands.command(aliases=['murder'])
    @cooldown(1, 10, BucketType.user)
    async def kill(self, ctx, *, user: discord.Member = None):
        user = user or ctx.author
        died = ['rolling out of the bed and the demon under the bed ate them.',
                'getting impaled on the bill of a swordfish.',
                'falling off a ladder and landing head first in a water bucket.',
                'his own explosive while trying to steal from a condom dispenser.',
                'a coconut falling off a tree and smashing there skull in.',
                'taking a selfie with a loaded handgun shot himself in the throat.',
                'shooting himself to death with gun carried in his breast pocket.',
                'getting crushed while moving a fridge freezer.',
                'getting crushed by his own coffins.',
                'getting crushed by your partner.',
                'laughing so hard at The Goodies Ecky Thump episode that he died of heart failure.',
                'getting run over by his own vehicle.',
                'car engine bonnet shutting on there head.',
                'tried to brake check a train.',
                'dressing up as a cookie and cookie monster ate them.',
                'tried to react Indiana Jones, died from a snake bite.',
                'tried to short circuit me, not that easy retard'
                ]
        await ctx.send(embed=discord.Embed(
            colour=discord.Colour.red(),
            description='{} was killed by {}'.format(user.display_name, random.choice(died))
        ).set_author(name=self.bot.user.display_name, icon_url=self.bot.user.avatar_url))

    @commands.command(aliases=['punch'], name='PunchMachine')
    @cooldown(1, 10, BucketType.user)
    async def punchmachine(self, ctx):
        answer = random.randint(0, 999)
        response = ['**Nice shot bro**',
                    '**Did you miss the machine**',
                    '**DAHM HAVE SOME MERCY**',
                    '**Even a baby can hit harder**',
                    '**Weakling lmfao**',
                    '**You wasted money to get that score**',
                    ]
        embed = discord.Embed(
            color=discord.Color.red()
        )
        embed.add_field(name='**Punch MACHINE**',
                        value=f'\n\nYou swing and hit a **{answer}**\n\nThe crowd around you: **{random.choice(response)}**')
        await ctx.send(embed=embed)
        
    @commands.command()
    @commands.cooldown(1, 10, BucketType.user)
    async def say(self, ctx, *, quote: str = None):
        if not quote:
            ctx.command.reset_cooldown(ctx)
            return await ctx.send('What are u saying!')
        await ctx.send('{}\n\t- **{}**'.format(quote, ctx.author))
        
    @commands.command()
    @commands.cooldown(1, 60, BucketType.user)
    async def annoy(self, ctx, member: discord.Member = None):
        if not member:
            ctx.command.reset_cooldown(ctx)
            return await ctx.send('Please ping a user.')

        if ctx.message.content == '<@!{}>'.format(member.id):
            return await ctx.send('I will have to ping him for you!\n{}'.format(member.mention))
        await ctx.send('You have successfully pinged {}'.format(member))

    @commands.command()
    async def f(self, ctx, *, message: str = None):
        if message == None:
            await ctx.send('<:F_:745287381816574125>')
            return await ctx.send('**{} Has Paid Their Respects.**'.format(ctx.author.display_name))
        await ctx.send('<:F_:745287381816574125>')
        await ctx.send('**{} Has Paid There Respects:** {}'.format(ctx.author.display_name, message.title()))

    @commands.command()
    async def spoiler(self, ctx, *, message: str = None):
        if message == None:
            ctx.command.reset_cooldown(ctx)
            return await ctx.send('||{} Is a retard. Retry with an actual message.||'.format(ctx.author))
        await ctx.send('||{}||'.format(message))

    @commands.command()
    @commands.bot_has_guild_permissions(read_message_history=True, read_messages=True)
    async def pings(self, ctx, limit='10', user: discord.Member = None):
        user = ctx.author if not user else user
        try:
            limit = int(limit)
        except ValueError:
            return await ctx.send('The limit for the searching must be a number.')
        counter = 0
        async for message in ctx.channel.history(limit=limit):
            if '<@!{}>'.format(user.id) in message.content:
                counter += 1
        await ctx.send('You have been pinged {} times in the last {} messages'.format(counter, limit))
def setup(client):
    client.add_cog(Fun(client))
