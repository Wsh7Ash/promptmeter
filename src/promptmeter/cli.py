#!/usr/bin/env python3
import click, sys
from rich.console import Console
from .estimate import estimate_tokens, estimate_cost
console = Console()
@click.group()
@click.version_option()
def main(): pass
@main.command()
@click.argument('file', required=False)
@click.option('--rate', default=0.50, help='USD per 1M input tokens')
def meter(file, rate):
    text = open(file).read() if file else sys.stdin.read()
    tokens = estimate_tokens(text)
    console.print(f'[green]~{tokens} tokens[/green]')
    console.print(f'[blue]~${estimate_cost(tokens, rate)} at ${rate}/1M[/blue]')
if __name__ == '__main__': main()
