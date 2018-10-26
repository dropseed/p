import os

import click

from .run import run
from .types import known_types
from . import git


def discover_commands(in_path="."):
    commands = {}

    paths = os.listdir(in_path)

    # iterative the types in a specific order,
    # if duplicates, the first match is used for each command name
    for t in known_types:
        for p in paths:
            full_p = os.path.join(in_path, p)
            if t._recognizes_path(full_p):

                obj = t(full_p)

                for name in dir(obj):
                    value = getattr(obj, name)
                    if (
                        not name.startswith("_")
                        and name not in commands
                        and (callable(value) or isinstance(value, str))
                    ):
                        commands[name] = value

    return commands


def do_command(command):
    commands = discover_commands()

    if command not in commands:
        click.secho("Not sure what to run", fg="red")
        return False

    if command == "setup" or command in git.GIT_COMMANDS:
        git.install_hooks(commands)

    cmd = commands[command]

    click.secho(f"Running {command} using {cmd}")
    if isinstance(cmd, str):
        run(cmd)
    else:
        cmd()
