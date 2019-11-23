import os

import click

from .types import known_types
from . import git


class Group:
    def __init__(self, dir="."):
        self.dir = dir
        self.discover()

    def discover(self):
        self.commands = {}
        self.subgroups = {}

        # iterative the types in a specific order,
        # if duplicates, the first match is used for each command name
        paths = os.listdir(self.dir)

        for cmd_type in known_types:
            for p in paths:
                full_p = os.path.join(self.dir, p)
                if cmd_type._recognizes_path(full_p):
                    obj = cmd_type(full_p)

                    for command in obj._available_commands.values():
                        if command.name not in self.commands:
                            self.commands[command.name] = command

        # create subgroupings for any
        for command in self.commands.values():
            if command.group_name and command.group_name not in self.subgroups:
                self.subgroups[command.group_name] = Subgroup(command.group_name, self)

    def do_command(self, command, cmd_args):
        command = self.commands[command]

        if (
            os.path.exists(".git")
            and command.name == "install"
            or command.name in git.GIT_COMMANDS
        ):
            git.install_hooks(self.commands)

        command.run(cmd_args)


class Subgroup:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent

        self.commands = {
            k: v for k, v in self.parent.commands.items() if v.group_name == self.name
        }
