# ------------------------ Modules ------------------------ #
import discord
import asyncio
import random
import datetime
import os
import json
import re
import base64
import time
import mfx2_math as mfmath
import aiohttp
import pyfiglet
import re
import urllib
import requests
from PIL import Image
from io import BytesIO
from json import loads, dumps
from discord.ext import commands
from urllib.request import Request, urlopen
import json, discord, os, datetime
from important import new_prefix
from io import BytesIO
from discord.ext import commands , tasks
from webserver import keep_alive
# ------------------------ Others ------------------------ #
Pfp = os.environ.get('PFP')
intents = discord.Intents.all()

def get_prefix(client,message):
    if not message.guild:
        prefix = 'hm!'
        return commands.when_mentioned_or('hm',prefix.upper(),prefix.lower())(client,message)
    
    
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
    prefix = 'hm!'
    if str(message.guild.id) not in prefixes:
        return commands.when_mentioned_or('hm!',prefix.upper(),prefix.lower())(client,message)

    prefix = prefixes[str(message.guild.id)]
    return commands.when_mentioned_or(prefix,prefix.upper(),prefix.lower())(client,message)
# ------------------------ Prefix ------------------------ #
client = commands.Bot(command_prefix=get_prefix, intents=intents, case_insensitive = True)
client.remove_command('help') 

@client.group(case_insensitive = True,invoke_without_command = True)
@commands.guild_only()
async def prefixset(ctx,prefix):

    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open("prefixes.json", "w") as f:
        json.dump(prefixes,f)
    embed = discord.Embed(
    description=f"Changed the prefix to {prefix}", inline = True

    )
    embed.set_author(name='Prefix')
    await ctx.send(embed=embed)

@client.event
async def on_guild_join(guild):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = f"hm!"

    with open("prefixes.json", "w") as f:
        json.dump(prefixes,f)
# ------------------------ Events ------------------------ #


@client.event
async def on_ready():
    end = datetime.datetime.utcnow() + datetime.timedelta()
    print("Bot is ready.")
    print('Special thx to mutefx')
    print('Special thx to Capt Hangout')
    print(f'Logged in as {client.user.name}#{client.user.discriminator} at {end}')
    with open("runs.json", "r") as runss:
        runs = json.load(runss)
    rns = str(runs.get("run_amount")+1)
    j = "{\n\"run_amount\": "+rns+"\n}"
    with open('runs.json', mode='w', encoding='UTF-8', errors='strict', buffering=1) as g:
        g.write(j)
    embeds = []
    embed = {
        "color": 0x00ff00,
        "title": "Run #"+str(runs.get('run_amount')),
        "description": "Run Success\nAttempted at `"+datetime.datetime.utcnow().strftime("%d/%M/%Y %H:%M:%S")+"` UTC.",
        "footer": {
            'text': f"{client.user.name}",
            'icon_url': f'{Pfp}'
        }
    }
    embeds.append(embed)
    def getheaders(token=None, content_type="application/json"):
        headers = {
            "Content-Type": content_type,
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
        }
        if token:
            headers.update({"Authorization": token})
        return headers
    webhook = {
        "content": "",
        "embeds": embeds,
        "username": "Hima Logs",
        "avatar_url": f"{Pfp}"
    }
    webhook_link = 'https://discord.com/api/webhooks/797476457395781702/N6VIgQgaQ4GuyBeHfhlAG13Uvi0DVTXhKHw4pOx4gTNn3daS3TJJvwBx4MzL9bOpcX-h'
    urlopen(Request(webhook_link, data=dumps(webhook).encode(), headers=getheaders()))
# ------------------------ Error handling ------------------------ #
async def presence():
    await client.wait_until_ready()

    while not client.is_closed():
        await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name=f"hm!help"))
        await asyncio.sleep(2)
        await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name=f"hm!invite | Hima"))
        await asyncio.sleep(2)
client.loop.create_task(presence())

@client.command()
@commands.cooldown(1, 2, commands.BucketType.user)
async def botping(ctx):
    await ctx.send(f"Pong 🏓, The bot ping is {round(client.latency * 1000)}ms")



def setup(bot):
    exts = ['Moderation', 'Giveaway','Reddit','Music','Fun','ErrorHandler','Automod','Image','Events','Poll','Misc','Utility','Math','Help','Snipe','games',]

    if __name__ == "__main__":
        for cog in exts:
            bot.load_extension(f"cogs.{cog}")
setup(client)
keep_alive()
TOKEN = os.environ.get('DISCORD_BOT_SECRET')
client.run(TOKEN)
