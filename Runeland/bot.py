import discord
from discord.ext import commands
import random

command_prefix = "!"
description = "Bot for helping Runeland Discord Server"
bot = commands.Bot(command_prefix)

# Assigns a user a role if it exists or takes off the role if they have it.
@bot.command()
async def roleme(ctx, role):
	if role is None:
		return await ctx.send("You need to specify role!")

	user = ctx.message.author
	r = discord.utils.get(user.guild.roles, name=role)
	if r in user.roles:
		await user.remove_roles(r)
	else:
		await user.add_roles(r)



# Generates and stores a Runeland Character for user that called command.
@bot.command()
async def createchar(ctx):
	user = ctx.message.author
	races = ['human', 'elf', 'dwarf']

	def pred(m):
		return m.author == user and m.channel == ctx.message.channel
	
	# Getting user response for character race.
	await ctx.send("Choose a race OR say 'roll' to roll for a unique race.")
	response_race = await bot.wait_for('message', check=pred, timeout=30)
	
	# Checks to see if user wants to roll for a unique race.
	if response_race.content == 'roll':
		race_roll = random.randint(1, 100)

		# Assigns a unique race if user gets the required roles
		if race_roll >= 85 and race_roll < 90:
			await ctx.send("You rolled the Half-Orc of the Numb!")
			user_race = 'Half-Orc of the Numb'
		elif race_roll >= 90:
			await ctx.send("You rolled the Drakon of Inox!")
			user_race = 'Drakon of Inox'
		# Gives user another pick at the race if they cant get a unique one.
		else:
			await ctx.send("You did not get a unique race! Please choose from the available ones.")
			response_race = await bot.wait_for('message', check=pred, timeout=30)
			if response_race.content in races:
				user_race = response_race.content
			else:
				return await ctx.send("You need to specify a specific race!")
	elif response_race.content in races:
		user_race = response_race.content
	else:
		return await ctx.send("You need to specify a specific race!")

	ctx.send()


bot.run('NTAxMjM2Mzc0MTE3MDIzNzQ0.DqWc6g.B9cQG8ecydbRfhkM-QbxKy5VqVM')
