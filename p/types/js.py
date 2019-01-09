import os
import json

from .base import BaseType


class Npm(BaseType):
    @classmethod
    def _recognizes_path(cls, path):
        return os.path.basename(path) == "package.json"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.install = "npm install"

        package = json.load(
            open(os.path.join(os.path.dirname(self._path), "package.json"))
        )

        for k in package.get("scripts", {}).keys():
            setattr(self, k, f"npm run {k}")


class Yarn(Npm):
    @classmethod
    def _recognizes_path(cls, path):
        return os.path.basename(path) == "yarn.lock"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.install = "yarn install"

    @property
    def _namespace(self):
        # overwrite the commands from Npm class
        return "npm"
