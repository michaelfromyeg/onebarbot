# This file doubles as both a command-line interface for getting lyrics and a way of gathering lyrics for the Twitter bot
import sys
import random

import lyricsgenius
import click

from credentials import *

def setup():
	# Configure lyrics genius
	genius = lyricsgenius.Genius(genius_client_access_token)


def main():
	print("This function needs to be implemneted")

@click.command()
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", prompt="Your name", help="The person to greet.")
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for _ in range(count):
        click.echo(f"Hello, {name}!")

if __name__ == '__main__':
	setup()
  hello()
