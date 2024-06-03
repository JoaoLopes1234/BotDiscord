from datetime import datetime
import discord
from discord.ext import commands, tasks

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

discord_token = 'MTI0NjkwMTYwMDcxOTczNjg1Mw.GTsr1f.KxWBqfduJCjgwFKtrY3SIQLtCHM4PYN-vDKJU0'


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    check_alarm.start()

@bot.command()
async def inverse(ctx, message):

    await ctx.send(message[::-1])
    
    

@tasks.loop(minutes=1)
async def check_alarm():
    now = datetime.now()
    if now.hour == 10 and now.minute == 0:
        channel = bot.get_channel(1246900934127124503)
        if channel:
            await channel.send('⏰ Alarme! São 10h da manhã!')
            

bot.run(discord_token)