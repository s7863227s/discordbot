#導入 Discord.py
import discord
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
from discord.ext import commands
#client 是我們與 Discord 連結的橋樑
bot = commands.Bot(command_prefix='[', intents=intents)

#調用 event 函式庫
@bot.event
#當機器人完成啟動時
async def on_ready():
    print("上線中")


bot.run('MTAyNjQ2NzMwNDQ3NDY4MTQxNA.GbRJfT.W_DCfdEqdw0bpNIDCcQpXJk3MeqrnNr0CjfLdE') #TOKEN 在剛剛 Discord Developer 那邊「BOT」頁面裡面