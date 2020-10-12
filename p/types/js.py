import os
import json

from .base import BaseType


class NpmScripts(BaseType):
    @classmethod
    def _recognizes_path(cls, path):
        return os.path.basename(path) == "package.json"

    def _add_commands(self):
        package = json.load(
            open(os.path.join(os.path.dirname(self._path), "package.json"))
        )

        for k in package.get("scripts", {}).keys():
            self._add_command(k, f"npm run {k}", preset=False)
