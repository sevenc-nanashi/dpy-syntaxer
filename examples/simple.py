import os
from textwrap import dedent

import discord
from discord.ext import commands, syntaxer

bot = commands.Bot(
    "b ",
    help_command=None,
    allowed_mentions=discord.AllowedMentions(everyone=False, replied_user=False)
)


@bot.event
async def on_ready():
    print(f"Logged in as: {bot.user}")


@bot.command("help", aliases=["?"])
async def _help(ctx, *, command_name=None):
    """
    Gets help of the command.
    Command Name: Command name to get help, return all command name if None.
    """
    if command_name is None:
        return await ctx.reply(" ".join([f"`{c}`" for c in bot.commands]))
    command = bot.get_command(command_name)
    if command is None:
        return await ctx.reply("Unknown command.")
    syntax = syntaxer.Syntax(command)
    e = discord.Embed(
        title=f"Help of `{command}`",
        description=dedent(f"""
        ``` {syntax} ```
        {command.callback.__doc__}
        """))
    return await ctx.reply(embed=e)


@bot.command()
async def foo(ctx, argument):
    """
    Says bar.
    Arg: Test argument
    """
    await ctx.reply("bar, passed" + argument)


@bot.command()
async def echo(ctx, *, text):
    """
    Says text.
    Text: text to say.
    """
    await ctx.send(text)


@bot.command()
async def neko(ctx, count=1):
    """
    I am neko.
    Times: Times to say, default by 1.
    """
    for _ in range(count):
        await ctx.send("Nyan")

bot.run(os.getenv("token"))
