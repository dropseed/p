from ..commands import Command


class BaseType:
    def __init__(self, path):
        self._path = path

    def _available_commands(self):
        commands = []

        for name in dir(self):
            value = getattr(self, name)
            if not name.startswith("_") and (callable(value) or isinstance(value, str)):
                commands.append(Command(name, value, self))

        return commands
