from discord.ext.commands.context import Context
import settings
import random
import discord
from discord.ext import commands
from cogs.greetings import Greetings

logger = settings.logging.getLogger("bot")

class Slapper(commands.Converter):
    use_nicknames : bool

    def __init__(self, *, use_nicknames) -> None:
        self.use_nicknames = use_nicknames

    async def convert(self, ctx, argument: str):
        someone = random.choice(ctx.guild.members)
        nickname = ctx.author
        if self.use_nicknames:
            nickname = ctx.author.nick
        return f"{nickname} slaps {someone} with {argument}"

def run():
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")

        for cmd_file in settings.CMDS_DIR.glob("*.py"):
            if cmd_file.name != "__init__.py":
                await bot.load_extension(f"cmds.{cmd_file.name[:-3]}")

    @bot.command(
            aliases=['p'],
    )
    async def ping(ctx):
        """Answers with pong"""
        await ctx.send('pong')

    @bot.command()
    async def hello(ctx):
        await ctx.send(f"Hello! {ctx.author.nick}")

    @bot.command()
    async def say(ctx, what = "what?"):
        await ctx.send(what)

    @bot.command()
    async def choice(ctx, *options):
        await ctx.send(random.choice(options)) 

    @bot.command()
    async def slap(ctx, reason : Slapper(use_nicknames=True)):
        await ctx.send(reason)  

    bot.run(settings.DISCORD_API_SECRET, root_logger=True)

if __name__ == "__main__":
    run()