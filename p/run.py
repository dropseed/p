import shlex
import subprocess

import click


def run(args, split=True):
    if split:
        args = shlex.split(args)
    click.secho(f"Running {args}", fg="green")
    subprocess.check_call(args)
