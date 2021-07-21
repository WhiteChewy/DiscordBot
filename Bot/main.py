# -*- coding: utf-8 -*-
from config import SETTINGS
import discord
import random
from discord.ext import commands


bot = commands.Bot(command_prefix=SETTINGS['prefix'])  #Префикс которым распознаются команды

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command(name='цитата')
async def quote(ctx):
    quotes = []
    with open("quotes.txt", 'r', encoding='utf-8') as file:
        for line in file:
            quotes.append(line)
    if len(quotes):
        await ctx.send(random.choice(quotes))
    else:
        await ctx.send("Никто пока ничем не запомнился :(")


@bot.command(name='добавь')
async def quote(ctx, *args):
    quote = args[0]+" сказал: \" "
    for arg in args[1:]:
        quote += arg + " "
    with open("quotes.txt", 'w', encoding='utf-8') as file:
        file.write(quote)
    await ctx.send("Цитата добавлена!")


@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send('Добро пожаловать на борт нашего 1000-летнего Сокола, {0.name}. Хана Соло нет, так что пока я тут главный!'.format(member))


bot.run(SETTINGS['token'])