import os

from .base import BaseType


class Combine(BaseType):
    @classmethod
    def _recognizes_path(cls, path):
        return os.path.basename(path) == "combine.yml"

    def _add_commands(self):
        self._add_command("work", "combine work")
