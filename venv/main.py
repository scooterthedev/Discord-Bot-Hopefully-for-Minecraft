import constants
import discord
from discord import app_commands


MY_GUILD = discord.Object(id=constants.guildID)


class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)


    async def setup_hook(self):
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)


intents = discord.Intents.default()
client = MyClient(intents=intents)


@client.event
async def on_ready():
    await client.tree.sync(guild=discord.Object(id=constants.guildID))
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')


@client.tree.command()
async def soup(interaction: discord.Interaction):
    await interaction.response.send_message(f'Hi, {interaction.user.mention}')

client.run(constants.botToken)