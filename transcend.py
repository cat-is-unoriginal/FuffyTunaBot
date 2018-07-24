# FuffyTuna
# Version 0.0.6 bby
# By Cat#5854

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
import re
from random import sample

client = discord.Client()
sentences = ""
dadbot_censor = false # people on my server were not happy with the censoring of dadbot ( I love the censorship and begrudgingly obliged )
tuna_chance = 150 # a one in five hundred chance

@client.event
async def on_ready():
	print ("online")
	print ("name: " + client.user.name)
	print ("id: " + client.user.id)
	print ("ctx of the day: your computer is now infected by ligma")
	
@client.event
async def on_message(ctx):
	if ctx.content.lower() == 'this is so sad alexa play despacito' or ctx.content.lower() == 'despacito':
		twochance = random.randint(1,20)
		print("despacito roll: " + str(twochance)
		
		if twochance == 2: # stupid bug right here about syntax that i can't figure out
			await client.send_message(ctx.channel, 'You have been selected by the Illuminati to listen to Despacito 2.\nPlaying Despacito 2')
			voice = await client.join_voice_channel(ctx.author.voice_channel)
			player = await voice.create_ytdl_player('https://www.youtube.com/watch?v=W3GrSMYbkBE')
			player.start()
			
		else:
			await client.send_message(ctx.channel, 'Playing Despacito')
			voice = await client.join_voice_channel(ctx.author.voice_channel)
			player = await voice.create_ytdl_player('https://www.youtube.com/watch?v=kJQP7kiw5Fk')
			player.start()
		

@client.event
async def on_message(ctx): # I replaced message with ctx since thats what all the cool kids are doing

	luck = random.randint(1,tuna_chance)
	print("your lucky number is " + str(luck))
	
	
	if ctx.content.lower() == 'this is so sad alexa play despayeeto' or ctx.content.lower() == 'despayeeto': # didn't realize this was broken, now fixed
		twochance = random.randint(1,20)
		print("Playing Despayeeto")
		await client.send_message(ctx.channel, 'Playing Despayeeto')
		try:
			voice = await client.join_voice_channel(ctx.author.voice_channel)
		except:
			pass
		player = await voice.create_ytdl_player('https://www.youtube.com/watch?v=jEddfV8Ts3g')
		player.start()

	if ctx.content.lower() == 'fuffytuna disconnect':
		await client.send_message(ctx.channel, 'fine... jeez')
		for x in client.voice_clients:	# I don't understand how this words, I just ripped it from stack overflow
        if(x.server == ctx.message.server):
            return await x.disconnect()
		
	if ctx.content.lower() == 'fuffytuna please':
		await client.send_message(ctx.channel, "Have fun! <https://cdn.discordapp.com/attachments/438354111910379530/465959178775822345/FuffyTuna.txt>")
		
	if ctx.content.lower() == 'fuffytuna help':
		print("Helping")
		await client.send_message(ctx.channel, """
		...Heres FuffyTuna's commands! 
		FuffyTuna help: 
		...This 
		this is so sad alexa play despacito: 
		...Plays despacito in your voice channel 
		FuffyTuna disconnect: 
		... FuffyTuna leave the voice channel 
		FuffyTuna please: 
		...Gives you the whole original fanfic 
		""")
	
	if dadbot_censor == true:
		if ctx.content.lower().startswith("im") or ctx.content.lower().startswith("i'm"): #i wonder why .lower() has parenthesis for arguments even though it has none
			global victim #global bc i needed to use it in the next part the send message part
			victim = ctx.author.mention
		
		if ctx.author.id == "247852652019318795" and ctx.content.startswith("Hi"):
			await client.delete_message(ctx)
			await client.send_message(ctx.channel, "don\'t you fricking dare dadbot, trying to abuse poor " + victim + ", your on thin ice " + ctx.author.mention)
			victim = ""  
		
	if luck == 1:
		print("You win!!")
		with open('FuffyTunaWithXtraFullstops.txt') as fuffy:
			sentences = re.findall(r".*?[\.\!\?]+", fuffy.read())
		bibleverse = sample(sentences, 1)
		await client.send_message(ctx.channel, "And I quoth from FuffyTuna.txt \n" + bibleverse + "\n want to read more? Just say \"FuffyTuna please\"")

client.run("NDcwNjczNDMxODUxOTU4Mjgy.DjgBng.-MUfZVy8vpUMPHkn6QAff098o2o") #Hopefully I don't leak this again