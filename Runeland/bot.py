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
	user_race = None
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

	await ctx.send("You got the race: " + user_race)


	# Getting user a background.
	background_roll = random.randint(1, 100)
	user_background = None
	if background_roll < 8:
		user_background = "Apprentice"
	elif background_roll < 15:
		user_background = "Bodyguard"
	elif background_roll < 22:
		user_background = "Diplomat"
	elif background_roll < 29:
		user_background = "Exile or Expatriate"
	elif background_roll < 36:
		user_background = "Former Slave"
	elif background_roll < 43:
		user_background = "High Born"
	elif background_roll < 50:
		user_background = "Hermit"
	elif background_roll < 57:
		user_background = "Initiate of the Flame"
	elif background_roll < 64:
		user_background = "Peasant"
	elif background_roll < 71:
		user_background = "Rebel"
	elif background_roll < 78:
		user_background = "Reaver"
	elif background_roll < 85:
		user_background = "Veteran"
	elif background_roll < 92:
		user_background = "Urchin"
	else:
		await ctx.send("You get to choose a background! Please enter it below.")
		response_background = await bot.wait_for('message', check=pred, timeout=30)
		user_background = response_background.content

	await ctx.send("You got the background: " + user_background)

	


bot.run('NTAxMjM2Mzc0MTE3MDIzNzQ0.DqWc6g.B9cQG8ecydbRfhkM-QbxKy5VqVM')
