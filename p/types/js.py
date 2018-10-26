import os
import json

from .base import BaseType
from ..run import run


class Npm(BaseType):
    @classmethod
    def _recognizes_path(cls, path):
        return os.path.basename(path) == "package.json"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # only add work attr if we can detect a script
        package = json.load(
            open(os.path.join(os.path.dirname(self._path), "package.json"))
        )
        scripts = package.get("scripts", {})
        if "start" in scripts:
            self.work = lambda: run(scripts["start"])

    def setup(self):
        run("npm install")


class Yarn(Npm):
    @classmethod
    def _recognizes_path(cls, path):
        return os.path.basename(path) == "yarn.lock"

    def setup(self):
        run("yarn install")
