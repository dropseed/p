import os

from .base import BaseType
from ..run import run


class Pipenv(BaseType):
    @classmethod
    def _recognizes_path(cls, path):
        return os.path.basename(path) == "Pipfile.lock"

    def setup(self):
        run("pipenv sync --dev")
