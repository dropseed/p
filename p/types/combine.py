import os

from .base import BaseType
from ..run import run


class Combine(BaseType):
    @classmethod
    def _recognizes_path(cls, path):
        return os.path.basename(path) == "combine.yml"

    def work(self):
        run("combine work")
