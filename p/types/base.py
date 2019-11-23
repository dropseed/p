from ..commands import Command


class BaseType:
    def __init__(self, path):
        self._path = path
        self._available_commands = {}
        self._add_commands()

    def _add_commands(self):
        raise NotImplementedError()

    def _add_command(self, name, run, preset=True):
        self._available_commands[name] = Command(name, run, self, preset)
