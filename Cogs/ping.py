import discord
from discord.ext import commands
import time

class View(discord.ui.View): # Create a class called View that subclasses discord.ui.View
    @discord.ui.button(label="Click me!", style=discord.ButtonStyle.primary, emoji="😎") # Create a button with the label "😎 Click me!" with color Blurple
    async def button_callback(self, button, interaction):
        await interaction.response.send_message("You clicked the button!") # Send a message when the button is clicked

class PingCog(commands.Cog, name="ping command"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@discord.slash_command(name = "ping",
					usage="",
					description = "Display the bot's ping.")
	async def ping(self, ctx):
		await ctx.respond('Pong! {0}'.format(round(discord.latency, 1)))

def setup(bot:commands.Bot):
	bot.add_cog(PingCog(bot))