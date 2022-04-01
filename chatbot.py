import requests
import json
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="chatbot")
bot.remove_command("help")

language = "en" # [en, es, vn, zh, ru, ph, tr, si, ml, pt, de ja, fr, ar, ko, id]

@bot.event
async def on_message(message):
	if message.author == bot.user:
		return
	r = requests.get(f"https://api.simsimi.net/v2/?text={message.content}&lc={language}")
	await message.channel.send(r.json()['success'])

bot.run('')
