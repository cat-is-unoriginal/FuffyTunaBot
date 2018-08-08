# FuffyTuna
# Version 0.2.0 bby
# By Cat#5854

# Make this into a command: despatomatone, https://www.youtube.com/watch?v=bQJU82Lk79g

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
from random import sample
import re
import numpy as np
import pandas as pd

client = discord.Client()
sentences = ""
dadbot_censor = False # people on my server were not happy with the censoring of dadbot ( I love the censorship and but I begrudgingly obliged )
tuna_chance = 150 # a one in five hundred chance

@client.event
async def on_ready():
	print ("online")
	print ("name: " + client.user.name)
	print ("id: " + client.user.id)
	print ("message of the day: your computer is now infected by ligma")

@client.event
async def on_message(ctx): # I replaced message with ctx since thats what all the cool kids are doing

	luck = random.randint(1,tuna_chance)
	print("your lucky number is " + str(luck))
	
	if ctx.content.lower() == 'this is so sad alexa play despacito' or ctx.content.lower() == 'despacito' or ctx.content.lower() == 'alex play despacito':
		print(ctx.author.voice_channel)
		if ctx.author.voice_channel:
			twochance = random.randint(1,20)
			print("despacito roll: " + str(twochance))
		
			if twochance == 2:
				await client.send_message(ctx.channel, 'You have been selected by the Illuminati to listen to Despacito 2.\nPlaying Despacito 2')
				voice = await client.join_voice_channel(ctx.author.voice_channel)
				player = await voice.create_ytdl_player('https://www.youtube.com/watch?v=W3GrSMYbkBE')
				player.start()
				
			else:
				await client.send_message(ctx.channel, 'Playing Despacito')
				voice = await client.join_voice_channel(ctx.author.voice_channel)
				player = await voice.create_ytdl_player('https://www.youtube.com/watch?v=kJQP7kiw5Fk')
				player.start()
	
		else:
			await client.send_message(ctx.channel, 'ur not in a voice channel u dumb dumb')
		
	
	if ctx.content.lower() == 'this is so sad alexa play despayeeto' or ctx.content.lower() == 'despayeeto' or ctx.content.lower() == 'alex play despayeeto':
		print("Playing Despayeeto")
		await client.send_message(ctx.channel, 'Playing Despayeeto')
		try:
			voice = await client.join_voice_channel(ctx.author.voice_channel)
		except:
			pass
		player = await voice.create_ytdl_player('https://www.youtube.com/watch?v=jEddfV8Ts3g')
		player.start()

	if ctx.content.lower() == 'this is so sad alexa play despatomatone' or ctx.content.lower() == 'despatomatone' or ctx.content.lower() == 'alex play despatomatone':
		print("Playing Despatomatone")
		await client.send_message(ctx.channel, 'Playing Despatomatone')
		try:
			voice = await client.join_voice_channel(ctx.author.voice_channel)
		except:
			pass
		player = await voice.create_ytdl_player('https://www.youtube.com/watch?v=bQJU82Lk79g')
		player.start()

	if ctx.content.lower() == 'asdf':
		await client.send_message(ctx.channel, 'fine... jeez')
		for x in client.voice_clients:	# I don't understand how this works, I just ripped it from stack overflow
			if(x.server == ctx.server):
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
		this is so sad alexa play despayeeto: 
		...Plays despayeeto in your voice channel 
		asdf: 
		...FuffyTuna leave the voice channel 
		FuffyTuna please: 
		...Gives you the whole original fanfic 
		FuffyTuna make command # <insert command name>;<insert command result>: 
		...Gives you the whole original fanfic
		FuffyTuna help make command
		...More in depth explanation of command syntax
		FuffyTuna show commands:
		...Shows all custom commands
		FuffyTuna delete command:
		...Deletes that command (DO NOT LET COMMANDS BECOME LESS THAN TWO)
		""")

	if ctx.content.lower() == 'fuffytuna help make command':
		await client.send_message(ctx.channel,"""
		FuffyTuna will let you make a automatic response to any word!
		To create this 'command' simple type
		FuffyTuna make command <insert command>;<insert response>
		Example:
		FuffyTuna make command oh hi mark;i did not hit her i did not
		WARNING:
		ALWAYS HAVE AT LEAST TWO COMMANDS OR IT DOESN'T WORK
		HELP IT ISN'T WORKING!?
		Did you add a space after the command?
		If that doesn't work ask Cat#5854
		""")

	# read custom commands
	print(str(ctx.author.id))
	if ctx.author.id != client.user.id:
		with open(r'C:\Users\Cat\Documents\FuffyTunaBot\commands.txt','r') as f: # short for command wink wink
			for i, l in enumerate(f):
				pass
			count =  i + 1
			print(str(count))
			
			cmd_array = np.genfromtxt('commands.txt', dtype='str', delimiter=';') # FINALLLLY I FIGURED IT OUT
			print(str(cmd_array[:]))
	
			i = 0
			for i in range(count):
				if ctx.content == cmd_array[i,0]:
					await client.send_message(ctx.channel, cmd_array[i,1])

	# write custom commands
	if ctx.content.lower().startswith("fuffytuna make command"):
		if ';' in ctx.content:
			spliced_ctx = ctx.content[23:]
			print(spliced_ctx)
			with open(r'C:\Users\Cat\Documents\FuffyTunaBot\commands.txt','a') as f:
				f.write('\n' + spliced_ctx)
			split_ctx = ctx.content[23:].split(";")
			await client.send_message(ctx.channel, "MADE COMMAND!\nCommand: " + split_ctx[0] + "\nWith responcs: " + split_ctx[1])
		else:
			await client.send_message(ctx.channel, "Improper syntax")

	# show custom commands
	if ctx.content.lower() == 'fuffytuna show commands':
		command_listing = ''
		with open(r'C:\Users\Cat\Documents\FuffyTunaBot\commands.txt') as f:
			for line in f:
				command_listing += line
		await client.send_message(ctx.channel, "Custom commands available are:\n" + command_listing)

	# delete custom commands
	if ctx.content.lower().startswith("fuffytuna delete command"): #25
		command = ctx.content[25:]
		with open(r'C:\Users\Cat\Documents\FuffyTunaBot\commands.txt',"r") as f:
			lines = f.readlines()
		with open(r'C:\Users\Cat\Documents\FuffyTunaBot\commands.txt',"w") as f:
			for line in lines:
				if line.startswith(command) == False:
					f.write(line)
		await client.send_message(ctx.channel, "Deleted command: " + command)
	if dadbot_censor == True:
		if ctx.content.lower().startswith("im") or ctx.content.lower().startswith("i'm"): # i wonder why .lower() has parenthesis for arguments even though it has none
			global victim # global bc i needed to use it in the next part the send message part
			victim = ctx.author.mention
		
		if ctx.author.id == "247852652019318795" and ctx.content.startswith("Hi"):
			await client.delete_message(ctx)
			await client.send_message(ctx.channel, "don\'t you fricking dare dadbot, trying to abuse poor " + victim + ", your on thin ice " + ctx.author.mention)
			victim = ""  
		
	if luck == 1:
		if ctx.author.bot == False:
			print("You win!!")
			with open('FuffyTunaWithXtraFullstops.txt') as fuffy:
				sentences = re.findall(r".*?[\.\!\?]+", fuffy.read())
			bibleverse = sample(sentences, 1)
			await client.send_message(ctx.channel, "And I quoth from FuffyTuna.txt \n" + str(bibleverse) + "\n want to read more? Just say \"FuffyTuna please\"")

client.run("") # Fuck you Klasa