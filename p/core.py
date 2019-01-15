import os

import click

from .types import known_types
from . import git


def discover_commands(in_path="."):
    commands = {}

    paths = os.listdir(in_path)

    # iterative the types in a specific order,
    # if duplicates, the first match is used for each command name
    for cmd_type in known_types:
        for p in paths:
            full_p = os.path.join(in_path, p)
            if cmd_type._recognizes_path(full_p):
                obj = cmd_type(full_p)

                for command in obj._available_commands.values():
                    if command.base_command_name not in commands:
                        commands[command.base_command_name] = {}

                    if command.name not in commands[command.base_command_name]:
                        commands[command.base_command_name][command.name] = command

    # if any manual commands are provided, remove all inferred commands from that group
    for base_name, commands_by_name in commands.items():
        has_manual_commands = any([not x.inferred for x in commands_by_name.values()])
        if has_manual_commands:
            to_pop = [name for name, command in commands_by_name.items() if command.inferred]
            for p in to_pop:
                commands_by_name.pop(p)

    return {k: sorted(commands[k].values()) for k in sorted(commands.keys())}


def do_command(command, commands, cmd_args):
    # commands = discover_commands()

    if command not in commands:
        click.secho("Not sure what to run", fg="red")
        return False

    if os.path.exists(".git") and command == "install" or command in git.GIT_COMMANDS:
        git.install_hooks(commands)

    for subcommand in commands[command]:
        click.secho(f"Running command: {subcommand}")
        subcommand.run(cmd_args)
