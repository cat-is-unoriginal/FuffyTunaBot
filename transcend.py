# Cats really neato bot: FuffyTuna
# Version 0.0.5 bby
# By Cat#5854

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import chalk
import random
import re
from random import sample

client = discord.Client()
sentences = ""

@client.event
async def on_ready():
	print ("online")
	print ("name: " + client.user.name)
	print ("id: " + client.user.id)
	print ("message of the day: fuck you nibba")
	
@client.event
async def on_message(message):

	luck = random.randint(1,200)
	print("your lucky number is " + str(luck))
	
	if message.content.lower() == 'this is so sad alexa play despacito':
		twochance = random.randint(1,20)
		#print("despacito roll: " + str(twochance)
		
		#if twochance == 2:
		#	print("Playing Despacito 2")
		#	await client.send_message(message.channel, 'You have been selected by the Illuminati to listen to Despacito 2.\nPlaying Despacito 2')
		#	voice = await client.join_voice_channel(message.author.voice_channel)
		#	player = await voice.create_ytdl_player('https://www.youtube.com/watch?v=W3GrSMYbkBE')
		#	player.start()
			
		#else:
		print("Playing Despacito")
		await client.send_message(message.channel, 'Playing Despacito')
		voice = await client.join_voice_channel(message.author.voice_channel)
		player = await voice.create_ytdl_player('https://www.youtube.com/watch?v=kJQP7kiw5Fk')
		player.start()

	if message.content.lower() == 'fuffytuna disconnect':
		await client.send_message(message.channel, 'fine... jeez')
		voice.disconnect()
		
	if message.content.lower() == 'fuffytuna please':
		await client.send_message(message.channel, "Have fun! <https://cdn.discordapp.com/attachments/438354111910379530/465959178775822345/FuffyTuna.txt>")
		
	if message.content.lower() == 'fuffytuna help':
		print("Helping")
		await client.send_message(message.channel, """
		___Heres FuffyTuna's commands! 
		FuffyTuna help: 
		___This 
		this is so sad alexa play despacito: 
		___Plays despacito in your voice channel 
		FuffyTuna disconnect: 
		___Makes FuffyTuna leave the voice channel 
		FuffyTuna please: 
		___Gives you the whole original fanfic 
		""")
		
	if message.content.lower().startswith("im") or message.content.lower().startswith("i'm"):
		global victim
		victim = message.author.mention
		
	if message.author.id == "247852652019318795" and message.content.startswith("Hi"):
		await client.delete_message(message)
		await client.send_message(message.channel, "don\'t you fricking dare dadbot, trying to abuse poor " + victim + ", your on thin ice " + message.author.mention)
		victim = ""
		
	if luck == 1:
		print("You win!!")
		with open('FuffyTunaWithXtraFullstops.txt') as fuffy:
			sentences = re.findall(r".*?[\.\!\?]+", fuffy.read())
		bibleverse = sample(sentences, 1)
		await client.send_message(message.channel, "And I quoth from FuffyTuna.txt \n" + str(bibleverse) + "\n want to read more? Just say \"FuffyTuna please\"")

client.run("")
