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
	await ctx.send("Choose a race.")
	response_race = await bot.wait_for('message', timeout=30)
	print(response_race)


bot.run('NTAxMjM2Mzc0MTE3MDIzNzQ0.DqWc6g.B9cQG8ecydbRfhkM-QbxKy5VqVM')
