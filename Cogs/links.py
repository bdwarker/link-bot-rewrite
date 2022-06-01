#TODO: Rename the file to the command name.
#TODO: Rename "links" with the command name.
#TODO(Optional): Remove these comments.

import discord
from discord.ext import commands
import time
from firebaseConfig import firebase
db = firebase.database()
class linksCog(commands.Cog, name="links command"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@discord.slash_command(name = "link", #TODO: Replace with command name.
					description = "Set the channel to the links channel.")#TODO: Add a command's description.
	async def links(self, ctx, channel_id):
		chan_Men = channel_id
		try:
			channel_id = channel_id.replace("<", "")
			channel_id = channel_id.replace(">", "")
			channel_id = channel_id.replace("#", "")
			channel_id=int(channel_id)
			channel = self.bot.get_channel(channel_id)
			if channel is None:
				await ctx.respond("Channel not found.")
				return
			await ctx.respond(f"Setting channel to {chan_Men}")
			# type done
			async with ctx.typing():
				db.child("servers").child(f"{ctx.guild.id}").child("channel").set(f"{channel_id}")
				await ctx.respond("Done.")
		except Exception:
			await ctx.respond("Invalid channel id.")

def setup(bot:commands.Bot):
	bot.add_cog(linksCog(bot))