import os

import click

from .types import known_types


def do(method):
    # first look for project.yml
    # then look for scritps dir
    # then look for specific kinds of files if we haven't found anything yet (if found multiple then say so)
    # matches = inferredos.listdir()

    inferred = []
    paths = os.listdir()
    for t in known_types:
        for p in paths:
            if t.recognizes_path(p) and hasattr(t, method):
                inferred.append(t(p))

    if not inferred:
        click.secho("Not sure what to run", fg='red')
        return

    if len(inferred) > 1:
        print(inferred)
        print("choosing the first type...")

    click.secho(f"Running {method} using {inferred[0]}")
    to_call = getattr(inferred[0], method)
    to_call()


@click.group()
@click.pass_context
def cli(ctx):
    pass


@cli.command()
@click.pass_context
def setup(ctx):
    do("setup")


@cli.command()
@click.pass_context
def work(ctx):
    do("work")


if __name__ == '__main__':
    cli()
