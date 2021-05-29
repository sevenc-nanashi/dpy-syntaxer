from typing import Optional

from discord.ext import commands, syntaxer
from discord.ext.commands import Greedy


# ================================ Simple =================================

@commands.command()
async def root_command(ctx, arg):
    """
    Root command
    arg: Description of arg
    """
    pass


@commands.command()
async def star(ctx, arg, *args):
    """
    Root command
    arg: Description of arg
    args: Description of args
    """
    pass


@commands.command()
async def kwarg(ctx, arg, *, kwarg):
    """
    Root command
    arg: Description of arg
    kwarg: Description of kwarg
    """
    pass


@commands.group()
async def group(ctx, arg):
    pass


@group.command()
async def subcommand(ctx, arg):
    """
    Subcommand
    arg: Description of arg
    """
    pass


@group.group()
async def group2(ctx, arg):
    pass


@group2.command()
async def subcommand2(ctx, arg):
    """
    Subcommand2
    arg: Description of arg
    """
    pass

# ================================ Types =================================


@commands.command()
async def optional(ctx, arg: Optional[int], arg2, arg3=None):
    """
    Root command
    arg: Description of arg
    arg2: Description of arg2
    arg3: Description of arg3
    """
    pass


@commands.command()
async def greedy(ctx, args: Greedy[int], arg):
    """
    Root command
    args: Description of args
    arg: Description of arg
    """
    pass


@commands.command()
async def simple_type(ctx, arg: int):
    """
    Root command
    arg: Description of args
    """
    pass


def test_root():
    synt = syntaxer.Syntax(root_command)
    assert str(synt) == "root_command <arg>"
    assert str(synt.names) == "root_command"
    assert str(synt.args) == "<arg>"


def test_star():
    synt = syntaxer.Syntax(star)
    assert str(synt) == "star <arg> <args...>"
    assert str(synt.names) == "star"
    assert str(synt.args) == "<arg> <args...>"


def test_kwarg():
    synt = syntaxer.Syntax(kwarg)
    assert str(synt) == "kwarg <arg> <kwarg"
    assert str(synt.names) == "kwarg"
    assert str(synt.args) == "<arg> <kwarg"


def test_group():
    synt = syntaxer.Syntax(subcommand)
    assert str(synt) == "group subcommand <arg>"
    assert str(synt.names) == "group subcommand"
    assert str(synt.args) == "<arg>"
    synt2 = syntaxer.Syntax(subcommand2)
    assert str(synt2) == "group group2 subcommand2 <arg>"
    assert str(synt2.names) == "group group2 subcommand2"
    assert str(synt2.args) == "<arg>"


def test_optional():
    synt = syntaxer.Syntax(optional)
    assert str(synt) == "optional [arg] <arg2> [arg3]"
    assert str(synt.names) == "optional"
    assert str(synt.args) == "[arg] <arg2> [arg3]"


def test_greedy():
    synt = syntaxer.Syntax(greedy)
    assert str(synt) == "greedy <args...> <arg>"
    assert str(synt.names) == "greedy"
    assert str(synt.args) == "<args...> <arg>"


def test_simple_type():
    synt = syntaxer.Syntax(simple_type)
    assert str(synt) == "simple_type <arg>"
    assert str(synt.names) == "simple_type"
    assert str(synt.args) == "<arg>"


def test_change():
    synt = syntaxer.Syntax(optional,
                           default_format="{prefix}{command_name}",
                           required_formats=("R:", ""),
                           optional_formats=("O:", ""))
    assert str(synt) == "optional O:arg R:arg2 O:arg3"
    assert str(synt.names) == "optional"
    assert str(synt.args) == "O:arg R:arg2 O:arg3"
