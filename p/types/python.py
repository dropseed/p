import os

from .base import BaseType


class Pipenv(BaseType):
    @classmethod
    def _recognizes_path(cls, path):
        return os.path.basename(path) == "Pipfile.lock"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.install = "pipenv sync --dev"
