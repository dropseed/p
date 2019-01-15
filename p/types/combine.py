import os

from .base import BaseType


class Combine(BaseType):
    @classmethod
    def _recognizes_path(cls, path):
        return os.path.basename(path) == "combine.yml"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._add_command("work", "combine work")
