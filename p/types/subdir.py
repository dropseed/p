import os

from .base import BaseType


class Subdirectory(BaseType):
    @classmethod
    def _recognizes_path(cls, path):
        return os.path.basename(path).startswith("p-")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # avoid circular import for now...
        from ..core import discover_commands

        for name, value in discover_commands(self._path).items():
            setattr(self, name, value)
