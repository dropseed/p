import os

from .base import BaseType


class Carthage(BaseType):
    @classmethod
    def _recognizes_path(cls, path):
        return os.path.basename(path) in ("Cartfile", "Cartfile.resolved")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.install = "carthage update"
