import discord
from discord.ext import commands
import json
import os
from dotenv import load_dotenv
from firebaseConfig import firebase
import re
import requests
from bs4 import BeautifulSoup
load_dotenv()
db = firebase.database()
# Get configuration.json
with open("configuration.json", "r") as config: 
	data = json.load(config)
	token = data["token"]
	prefix = data["prefix"]
	owner_id = data["owner_id"]


class Greetings(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self._last_member = None

# Intents
intents = discord.Intents.default()
# The bot
bot = discord.Bot(debug_guilds=[917823554433712218])

# Load cogs
if __name__ == '__main__':
	for filename in os.listdir("Cogs"):
		if filename.endswith(".py"):
			bot.load_extension(f"Cogs.{filename[:-3]}")

@bot.event
async def on_ready():
	print(f"We have logged in as {bot.user}")
	print(discord.__version__)
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name =f"your messages"))
@bot.event
async def on_message(message):
	if message.author.bot:
		return
	if f"https://" in message.content:
		del_msg = db.child("servers").child(message.guild.id).child("del_msg").get().val()
		serv_chan = db.child("servers").child(message.guild.id).child("channel").get().val()
		if del_msg == "True":
			await message.delete()
		linkChan = bot.get_channel(int(serv_chan))
		embed = discord.Embed(title="Link detected", description=f"{message.author.mention} has sent a link.", color=0x00ff00)
		embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}")
		uri = re.search("(?P<url>https?://[^\s]+)", message.content).group("url")
		url_url = uri.replace("https://", "")
		embed.set_thumbnail(url=f"https://imaginative-brown-mink.faviconkit.com/{url_url}/256")
		reqs = requests.get(uri)
		# using the BeautifulSoup module
		soup = BeautifulSoup(reqs.text, 'html.parser')
		for title in soup.find_all('title'):
			type_Link = title.get_text()
		embed.add_field(name="Message", value=message.content)
		embed.add_field(name="Link", value=uri, inline=False)
		embed.add_field(name="Channel", value=message.channel.mention, inline=False)
		embed.add_field(name="HTTPS", value="Yes", inline=False)
		embed.add_field(name="Title", value=f"{type_Link}", inline=False)
		await linkChan.send(embed=embed)
	elif f"http://" in message.content:
		del_msg = db.child("servers").child(message.guild.id).child("del_msg").get().val()
		serv_chan = db.child("servers").child(message.guild.id).child("channel").get().val()
		if del_msg == "True":
			await message.delete()
		linkChan = bot.get_channel(int(serv_chan))
		embed = discord.Embed(title="Link detected", description=f"{message.author.mention} has sent a link.", color=0x00ff00)
		embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}")
		uri = re.search("(?P<url>http?://[^\s]+)", message.content).group("url")
		url_url = uri.replace("http://", "")
		embed.set_thumbnail(url=f"https://imaginative-brown-mink.faviconkit.com/{url_url}/256")
		reqs = requests.get(uri)
		# using the BeautifulSoup module
		soup = BeautifulSoup(reqs.text, 'html.parser')
		for title in soup.find_all('title'):
			type_Link = title.get_text()
		embed.add_field(name="Message", value=message.content)
		embed.add_field(name="Link", value=uri, inline=False)
		embed.add_field(name="Channel", value=message.channel.mention, inline=False)
		embed.add_field(name="HTTPS", value="No", inline=False)
		embed.add_field(name="Title", value=f"{type_Link}", inline=False)
		await linkChan.send(embed=embed)
bot.run(token)