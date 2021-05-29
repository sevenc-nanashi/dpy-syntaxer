[![PyPI - Version](https://img.shields.io/pypi/v/dpy-syntaxer)](https://pypi.org/project/dpy-syntaxer) [![PyPI - Downloads](https://img.shields.io/badge/dynamic/json?label=downloads&query=%24.total_downloads&url=https%3A%2F%2Fapi.pepy.tech%2Fapi%2Fprojects%2Fdpy-syntaxer)](https://pepy.tech/project/dpy-syntaxer/) [![readthedocs](https://readthedocs.org/projects/dpy-syntaxer/badge/?version=latest)](https://dpy-syntaxer.readthedocs.io)  

# dpy-syntaxer

Syntax maker for discord.py's command.

# How to use

`python3 -m pip install dpy-syntaxer`

```py
from typing import Optional

from discord.ext import commands, syntaxer


@commands.command()
async def command(ctx, arg1: Optional[int], arg2, *, arg3):
    """
    Command description
    arg_first: Description of arg1
    arg_second: Description of arg2
    arg_third: Description of arg3
    """
    pass


syntax = syntaxer.Syntax(command)
str(syntax)
# => 'command <arg_first> <arg_second> <arg_third'
syntax[0]
# => CommandName(name='command', parent=None)
syntax[1]
# => CommandArgument(name='arg_first', required=False, description='Description of arg1', format='[arg_first]', flag=<ArgumentType.optional: 2>, default=<class 'inspect._empty'>)
syntax[2]
# => CommandArgument(name='arg_second', required=True, description='Description of arg2', format='<arg_second>', flag=<ArgumentType.required: 1>, default=None)
syntax[3]
# => CommandArgument(name='arg_third', required=True, description='Description of arg3', format='<arg_third', flag=<ArgumentType.kwarg|required: 9>, default=None)
```

Please read the [documentation](https://dpy-syntaxer.readthedocs.io) for more information.