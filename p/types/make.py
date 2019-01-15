import os

from .base import BaseType


class Makefile(BaseType):
    @classmethod
    def _recognizes_path(cls, path):
        return os.path.basename(path) == "Makefile"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        commands = []

        for line in open(self._path, "r"):
            if line.startswith(".PHONY"):
                between_def_and_comments = line.split(":")[1].split("#")[0]
                items = between_def_and_comments.split()
                commands = commands + items

        for cmd in commands:
            self._add_command(cmd, f"make {cmd}", inferred=False)
