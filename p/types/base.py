from ..commands import Command


class BaseType:
    def __init__(self, path):
        self._path = path

    def _available_commands(self):
        commands = []

        for name in dir(self):
            value = getattr(self, name)
            if not name.startswith("_") and (callable(value) or isinstance(value, str)):
                namespaced_name = f'{name}--{self._namespace}'
                commands.append(Command(namespaced_name, value, self))

        return commands

    @property
    def _namespace(self):
        return self.__class__.__name__.lower()
