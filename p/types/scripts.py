import os

from .base import BaseType


class Scripts(BaseType):
    @classmethod
    def _recognizes_path(cls, path):
        return os.path.basename(path) in ("scripts", "script", "bin")

    def _add_commands(self):
        for s in os.listdir(self._path):
            p = os.path.join(self._path, s)
            if (
                os.path.isfile(p)
                and not os.path.splitext(s)[1]
                and os.access(p, os.X_OK)
            ):
                # just sets it as a string, which will be "run" automatically
                self._add_command(s, p, preset=False)
