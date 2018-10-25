import os
import json

from .base import BaseType
from ..run import run


class Npm(BaseType):
    @classmethod
    def recognizes_path(cls, path):
        return os.path.basename(path) == "package.json"

    def setup(self):
        run("npm install")

    def work(self):
        package = json.load(open(os.path.join(os.path.dirname(self.path), "package.json")))
        scripts = package.get("scripts", {})
        if "start" in scripts:
            run(scripts["start"])


class Yarn(Npm):
    @classmethod
    def recognizes_path(cls, path):
        return os.path.basename(path) == "yarn.lock"

    def setup(self):
        run("yarn install")
