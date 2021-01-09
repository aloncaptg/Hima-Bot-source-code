import discord
import json
import os
from discord.ext import commands , tasks

def new_prefix(client,message):

    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
    try:
        pre = prefixes[str(message.guild.id)]
    except:
        pre = 'c!'
def convert(time):
    time = time.lower()
    pos = ["s","m","h","d"]

    time_dict = {"s" : 1, "m" : 60, "h" : 3600 , "d" : 3600*24}

    unit = time[-1]

    if unit not in pos:
        return -1
    try:
        val = int(time[:-1])
    except:
        return -2


    return val * time_dict[unit]
Pfp = os.environ.get('PFP')

yesemoji = '✅'
emojiyes = '✅'
emojino = '❌'
boredemoji = '😐'