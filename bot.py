from datetime import datetime
import discord
from better_profanity import profanity
from discord.ext import commands, tasks

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='/', intents=intents)

discord_token = ''

profanity.load_censor_words()


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    check_alarm.start()


@bot.command()
async def inverse(ctx, message):

    await ctx.send(message[::-1])



@bot.command()
async def CallAll(ctx):
    await ctx.send("@everyone" + "Lets start our meeting")


@tasks.loop(minutes=1)
async def check_alarm():
    now = datetime.now()
    if now.hour == 10 and now.minute == 0:
        channel = bot.get_channel(1246900934127124503)
        if channel:
            await channel.send('⏰ Alarme! São 10h da manhã!')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if profanity.contains_profanity(message.content):
        await message.delete()
        await message.channel.send(f"{message.author.mention}, sua mensagem foi removida por conter linguagem ofensiva.")

    await bot.process_commands(message)


bot.run(discord_token)
