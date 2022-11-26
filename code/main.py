import discord
import os
import requests
import json
import random
from keepalive import keep_alive

intents = discord.Intents.all()
client = discord.Client(intents=intents)

pictures = ["https://media.discordapp.net/attachments/1039276555718905906/1045373420180885534/Screenshot_2022-11-07_161936.png", "https://media.discordapp.net/attachments/1039276555718905906/1045373635050864800/image.png?width=897&height=577", "https://media.discordapp.net/attachments/1039276555718905906/1045373635499671552/image.png?width=554&height=577", "https://i.pinimg.com/564x/10/c8/7e/10c87e0119f2f0dfca85924113720ce3.jpg", "https://i.pinimg.com/564x/53/61/39/5361396c2ab72d20f9a55caa3c2a2b9e.jpg", "https://i.pinimg.com/564x/6e/f3/80/6ef380bc5cda61ef083651fcd2a73c7e.jpg" ]

gifs = ["https://media.tenor.com/72HInq8c0wgAAAAS/kaveh-genshin-impact.gif", "https://media.tenor.com/utazGSdGMjEAAAAd/kaveh-genshin-impact.gif", "https://media.tenor.com/KPep59IIdW4AAAAM/kaveh-genshin-impact.gif", "https://media.tenor.com/S86iD4YOsDwAAAAd/kaveh-genshin-impact.gif"]

@client.event 
async def on_ready():
  print("{0.user} is here.".format(client))

@client.event
async def on_message(message):
  msg = message.content
  if message.author == client.user:
    return
    #check if message from bot
  if msg.startswith("/helloka"):
    await message.channel.send("Traveller, it's great to see you!")
  if msg.startswith("/nightska"):
    await message.channel.send("Have a good rest and sweet dreams, traveller 💖")
  if msg.startswith("/encka"):
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]["q"] + " -" + json_data[0]["a"]
    await message.channel.send(quote)
  if msg.startswith("/profileka"):
    await message.channel.send("https://genshin-impact.fandom.com/wiki/Kaveh#:~:text=Kaveh%20is%20the%20architect%20behind,the%20Sumeru%20Akademiya%20with%20honors.")
  if msg.startswith("/alhaitham?"):
    await message.channel.send("https://media.discordapp.net/attachments/1039276555718905906/1045373419669160039/Screenshot_2022-11-07_161911.png")
  if msg.startswith("/huhka"):
    await message.channel.send("https://media.discordapp.net/attachments/1039276555718905906/1045373633159241829/image.png?width=591&height=577")
  if msg.startswith("/frownka"):
    await message.channel.send("https://media.discordapp.net/attachments/1039276555718905906/1045373635952640060/image.png?width=485&height=577")
  if msg.startswith("/picka"):
    pic = random.choice(pictures)
    await message.channel.send(pic)
  if msg.startswith("/gifka"):
    gif = random.choice(gifs)
    await message.channel.send(gif)
  if msg.startswith("/helpka"):
    await message.channel.send("```/helloka - greetings\n/nightska - goodnights\n/profileka - profile\n/encka - a random encouragement\n/picka - random picture of yours truly\n/gifka - a random gif of yours truly\n/alhaitham? - thoughts on alhaitham\n/huhka - confused\n/frownka - frown```")


keep_alive() #to keep the bot alive
client.run(os.getenv("TOKEN"))
