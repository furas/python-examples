# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.03.13

import os
import discord
from discord.ext import commands, tasks

TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_connect():
    print("[on_connect] connected as", bot.user.name)

@bot.event
async def on_ready():
    #print("[on_ready] ready as", bot.user.name)

my_commands = {
    '!test': 'Hello World!'
}

@bot.command('create')
async def create(ctx, *args):
    #print('[create] ctx:', ctx)
    #print('[create] args:', args)
    
    if len(args) >= 2:
        key = '!' + args[0]
        val = args[1]
        my_commands[key] = val
    
@bot.event
async def on_message(msg, *args):
    #print("[on_ready] msg:", msg)
    #print("[on_ready] args:", args)
    
    #print("[on_message] got message as", bot.user.name)
    #print("[on_message] msg.author:", msg.author)
    #print("[on_message] msg.author.bot:", msg.author.bot)
    #print("[on_message] msg.content:", msg.content)

    # skip messages from bots
    if msg.author.bot:
        return

    cmd, *args = msg.content.split(' ')
    
    if cmd in my_commands:
        answer = my_commands[cmd]
        await msg.reply(answer) 
    else:
        # send to other commands
        await bot.process_commands(msg)

bot.run(TOKEN)
 
