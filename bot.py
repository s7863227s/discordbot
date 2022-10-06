#導入 Discord.py
import discord
#client 是我們與 Discord 連結的橋樑
client = discord.Client()

#調用 event 函式庫
@client.event
#當機器人完成啟動時
async def on_ready():
    print('目前登入身份：', client.user)

@client.event
#當有訊息時
async def on_message(message):
    #排除自己的訊息，避免陷入無限循環
    if message.author == client.user:
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

client.run('MTAyNjQ2NzMwNDQ3NDY4MTQxNA.GbRJfT.W_DCfdEqdw0bpNIDCcQpXJk3MeqrnNr0CjfLdE') #TOKEN 在剛剛 Discord Developer 那邊「BOT」頁面裡面