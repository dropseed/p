from ..commands import Command


class BaseType:
    def __init__(self, path):
        self._path = path
        self._available_commands = {}

    def _add_command(self, name, run, inferred=True):
        namespaced_name = f"{name}--{self._namespace}"
        self._available_commands[namespaced_name] = Command(namespaced_name, run, self, inferred)

    @property
    def _namespace(self):
        return self.__class__.__name__.lower()
