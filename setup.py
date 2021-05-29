import setuptools
from discord.ext.syntaxer import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dpy-syntaxer",
    version=__version__,
    author="sevenc-nanashi",
    author_email="sevenc-nanashi@sevenbot.jp",
    description="Syntax maker for discord.py's command",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sevenc-nanashi/dpy-syntaxer",
    packages=["discord.ext.syntaxer"],
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "discord.py>1.0.0<2.0.0",
    ],
)
