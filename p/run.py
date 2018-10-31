import sys
import shlex
import subprocess

import click


def run(args, split=True):
    if split:
        args = shlex.split(args)
    click.secho(f"Running {args}", fg="green")
    try:
        subprocess.check_call(args)
    except subprocess.CalledProcessError as e:
        click.secho(f"Failed to run {e.cmd}", fg="red")
        sys.exit(e.returncode)
