import discord
from discord.ext import commands
import time

class inviteCog(commands.Cog, name="invite command"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@discord.slash_command(name = "invite",
					description = "Get an invite link for the bot.")
	async def invite(self, ctx):
		await ctx.respond('https://discord.com/api/oauth2/authorize?client_id=949918069281685545&permissions=321616&scope=bot%20applications.commands')
			

def setup(bot:commands.Bot):
	bot.add_cog(inviteCog(bot))