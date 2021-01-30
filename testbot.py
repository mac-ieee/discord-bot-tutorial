import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

client = commands.Bot(command_prefix="?")

load_dotenv()
TOKEN = os.getenv('DISCORDTOKEN')

@client.event
async def on_ready():
	print("Bot is online!")



client.run(TOKEN)