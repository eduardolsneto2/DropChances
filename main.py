import discord
import os
import random
from keep_alive import keep_alive

client = discord.Client()

kekw = 'https://freetwitchemotes.com/wp-content/uploads/2021/03/Kekw-Shocked-Twitch-Emotes-ft-1200x675.png'

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  msg = message.content
  if msg.startswith('..mvp'):
    await mvp_chance_response(message)
  elif msg.startswith('..chance'):
    await chance_response(message)

async def chance_response(message):
  msgContent = message.content
  msgWithoutChance = msgContent.split("..chance ",1)[1]
  allPartsOfMsg = msgWithoutChance.split(" ")
  chance = allPartsOfMsg[0]
  numberTrys = allPartsOfMsg[1]
  prob = (1 - float(chance)/100) ** float(numberTrys)
  response = (1-prob)*100
  await message.channel.send(str(response) + '%')

 
async def mvp_chance_response(message):
  msgContent = message.content
  msgWithChance = msgContent.split("..mvp ",1)[1]
  if msgWithChance.startswith('1x '):
    number = msgWithChance.split("1x ",1)[1]
    prob = 0.9998 ** float(number)
    response = (1-prob)*100
    await message.channel.send(str(response) + '%')
    if random.randint(0,1000) < 52:
      await message.reply('btw rocha dropou a dele com 50 kekw')
      await message.channel.send(kekw)
  elif msgWithChance.startswith('2x'):
    number = msgWithChance.split("2x ",1)[1]
    prob = 0.9996 ** float(number)
    response = (1-prob)*100
    await message.channel.send(str(response) + '%')
  elif msgWithChance.startswith('3x'):
    number = msgWithChance.split("3x ",1)[1]
    prob = 0.9994 ** float(number)
    response = (1-prob)*100
    await message.channel.send(str(response) + '%')
  else:
    await message.channel.send('error')

keep_alive()
client.run(os.getenv('TOKEN'))