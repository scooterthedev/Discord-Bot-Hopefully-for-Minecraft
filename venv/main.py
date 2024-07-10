import constants
import discord
from discord.ext import commands
import os
import cog


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync(guild=discord.Object(id=constants.guildID))
    print(f'Logged in as {bot.user}')

async def load():
        bot.load_extension('C:\\Users\\yekut\\IdeaProjects\\Discord Bot\\venv\\cog\\hello.py')
        await bot.tree.sync()

@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
    bot.reload_extension(f'cogs.{extension}')
    await ctx.send(f'Reloaded {extension}')
    await self.tree.sync()

bot.run(constants.botToken)
