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

#當有訊息時
async def on_message(message):
    #排除自己的訊息，避免陷入無限循環
    if message.author == bot.user:
        return
    #如果以「說」開頭
    if message.content.startswith('說'):
      #分割訊息成兩份
      tmp = message.content.split(" ",2)
      #如果分割後串列長度只有1
      if len(tmp) == 1:
        await message.channel.send("你要我說什麼啦？")
      else:
        await message.channel.send(tmp[1])

bot.run('MTAyNjQ2NzMwNDQ3NDY4MTQxNA.GbRJfT.W_DCfdEqdw0bpNIDCcQpXJk3MeqrnNr0CjfLdE') #TOKEN 在剛剛 Discord Developer 那邊「BOT」頁面裡面