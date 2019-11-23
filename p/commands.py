from functools import total_ordering

from .run import run


@total_ordering
class Command:
    def __init__(self, name, cmd, cmd_type, preset):
        self.name = name
        self.cmd = cmd
        self.cmd_type = cmd_type
        self.preset = preset

        if ":" in self.name:
            self.group_name, self.group_command_name = self.name.split(":", 1)
        else:
            self.group_name = ""
            self.group_command_name = self.name

    def __str__(self):
        return f"{self.name} <- {self.cmd_type._path}"

    # @property
    # def base_command_name(self):
    #     return self.name.split("--")[0]

    # @property
    # def phase(self):
    #     parts = self.name.split("--")
    #     phase = parts[1] if len(parts) > 1 else None
    #     if phase in ("pre", "post"):
    #         return phase
    #     return None

    def run(self, cmd_args):
        if isinstance(self.cmd, str):
            run(self.cmd, cmd_args)
        elif isinstance(self.cmd, list):
            [run(x, cmd_args) for x in self.cmd]
        # else:
        #     self.cmd()

    def __eq__(self, other):
        return (self.name, self.cmd, self.cmd_type) == (
            other.name,
            other.cmd,
            other.cmd_type,
        )

    def __lt__(self, other):
        # if self.phase == other.phase:
        return self.name < other.name

        # phase_order = {"pre": 0, None: 1, "post": 2}
        # return phase_order[self.phase] < phase_order[other.phase]
