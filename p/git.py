import os
import subprocess

import click


GIT_COMMANDS = (
    # TODO should pre-commit be git-pre-commit?
    "pre-commit",
    "post-merge",
)


def install_hooks(available_commands):
    hooks_path = os.path.join(".git", "hooks")
    if not os.path.exists(hooks_path):
        return

    git_commands_in_use = [x for x in GIT_COMMANDS if x in available_commands]

    for cmd in git_commands_in_use:
        hook_path = os.path.join(hooks_path, cmd)
        if not os.path.exists(hook_path):
            if click.confirm(
                f"We found a {cmd} command in this project but your git {cmd} hook is not set up yet. Do that now?"
            ):
                with open(hook_path, "w+") as f:
                    f.write(f"#!/bin/sh -e\np {cmd}")
                subprocess.check_output(["chmod", "+x", hook_path])
