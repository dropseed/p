import sys
import shlex
import subprocess

import click


def run(cmd_str, cmd_args):
    args = shlex.split(cmd_str) + list(cmd_args)

    if sys.stdout.isatty():
        click.secho(f"Running {' '.join(args)}", bold=True)

    result = subprocess.run(args)

    if result.returncode != 0:
        if sys.stdout.isatty():
            click.secho(f"Failed {' '.join(args)}", fg="red")

        sys.exit(result.returncode)
