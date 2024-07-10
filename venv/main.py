import constants
import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync(guild=discord.Object(id=constants.guildID))
    print(f'Logged in as {bot.user}')

@bot.tree.command(name="hello", description="Say hello to the bot", guild=discord.Object(id=constants.guildID))
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("Hello!")

for filename in os.listdir('cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
    bot.reload_extension(f'cogs.{extension}')
    await ctx.send(f'Reloaded {extension}')

bot.run(constants.botToken)
