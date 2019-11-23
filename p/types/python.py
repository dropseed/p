import os

from .base import BaseType


class Pipenv(BaseType):
    @classmethod
    def _recognizes_path(cls, path):
        return os.path.basename(path) == "Pipfile.lock"

    def _add_commands(self):
        self._add_command("install", "pipenv sync --dev")
