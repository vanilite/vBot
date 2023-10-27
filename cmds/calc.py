from discord.ext import commands

@commands.group()
async def math(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send(f"i can't, {ctx.subcommand_passed} the numbers doesn't legit!")

# add
@math.command()
async def add(ctx, a : int , b : int):
    await ctx.send(a + b)

# subtract
@math.command()
async def subtract(ctx, a : int , b : int):
    await ctx.send(a - b)

# by
@math.command()
async def by(ctx, a : int , b : int):
    await ctx.send(a * b)

# divide
@math.command()
async def divide(ctx, a : int , b : int):
    await ctx.send(a / b)
async def setup(bot):
    bot.add_command(math)
    bot.add_command(add)
    bot.add_command(subtract)
    bot.add_command(by)
    bot.add_command(divide)