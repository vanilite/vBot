import settings
import discord
from discord.ext import commands

def run():
    print(settings.DISCORD_API_SECRET)

if __name__ == "__main__":
    run()