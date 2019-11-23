import os

from .base import BaseType


class Carthage(BaseType):
    @classmethod
    def _recognizes_path(cls, path):
        return os.path.basename(path) in ("Cartfile", "Cartfile.resolved")

    def _add_commands(self):
        self._add_command("install", "carthage update")
