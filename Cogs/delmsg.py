import discord
from discord.ext import commands
import time
from firebaseConfig import firebase
db = firebase.database()

class deleteMsgCog(commands.Cog, name="deleteMsg command"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@discord.slash_command(name = "delete",
					description = "Enables or disables the delete message feature.")
	async def deleteMsg(self, ctx, true_or_false):
		if true_or_false.lower() == "true":
			await ctx.respond("Deleting messages is now enabled.")
			db.child("servers").child(f"{ctx.guild.id}").child("del_msg").set("True")
		elif true_or_false.lower() == "false":
			await ctx.respond("Deleting messages is now disabled.")
			db.child("servers").child(f"{ctx.guild.id}").child("del_msg").set("False")
			

def setup(bot:commands.Bot):
	bot.add_cog(deleteMsgCog(bot))