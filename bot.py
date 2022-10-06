#導入 Discord.py
import discord
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True
from discord.ext import commands

#client 是我們與 Discord 連結的橋樑
bot = commands.Bot(command_prefix='!', intents=intents)

    
@bot.command()
async def test(ctx):
    await ctx.send('pong')

bot.run('MTAyNjQ2NzMwNDQ3NDY4MTQxNA.GGSyj-.i0myh6JxGRPw_ahJ7q2yhPbQoIoe2leR3UsU-8') #TOKEN 在剛剛 Discord Developer 那邊「BOT」頁面裡面