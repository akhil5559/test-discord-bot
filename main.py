import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load .env file (optional, for local testing)
load_dotenv()

# Bot intents
intents = discord.Intents.default()
intents.message_content = True  # Enable message content intent

# Bot setup
bot = commands.Bot(command_prefix="!", intents=intents)

# Event - when bot is ready
@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user} (ID: {bot.user.id})")

# Basic test command
@bot.command()
async def hello(ctx):
    await ctx.send("Hello! Your bot is working!")

# Run bot with token
TOKEN = os.getenv("DISCORD_TOKEN")
if TOKEN:
    bot.run(TOKEN)
else:
    print("❌ DISCORD_TOKEN not found in environment.")