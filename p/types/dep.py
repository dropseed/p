import os

from .base import BaseType


class Dep(BaseType):
    @classmethod
    def _recognizes_path(cls, path):
        return os.path.basename(path) in ("Gopkg.toml", "Gopkg.lock")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._add_command("install", "dep ensure")
