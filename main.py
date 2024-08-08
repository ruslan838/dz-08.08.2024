import discord, os, texts
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def info(ctx, n:str = '0'):
    if n.isdigit():
        n = int(n)
        if n == 0:
            await ctx.send('отправьте $info[номер]')
            await ctx.send('1 - тепловые электростанции')
            await ctx.send('2 - гидроэлектростанции')
            await ctx.send('3 - атомные электростанции')
            await ctx.send('4 - ветряные электростанции')
            await ctx.send('5 - солнечные электростанции')
            await ctx.send('6 - геотермальные электростанции')
        elif n >= 1 and n <= 6:
            await ctx.send(texts.textl[n-1])
        else:
            await ctx.send('ошибка')
    else:
        await ctx.send('ошибка')

bot.run('MTI2MDk4MzYyNjc5MTY1MzQzOA.GndmIX.OiT3yLrBYcISdviDyKeRW9Q2TdoYeP_0Ynrxsg')