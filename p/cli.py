import click

from .core import discover_commands, do_command
from . import __version__


class Pcli(click.Group):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.discovered_commands = discover_commands()

        for name, subcommands in self.discovered_commands.items():
            help = ", ".join([x.cmd for x in subcommands])
            help = "Using: " + help

            @click.command(name, help=help)
            @click.pass_context
            def func(ctx):
                do_command(ctx.info_name, self.discovered_commands)
                # exit(0 if result else 1)

            self.add_command(func)


@click.group(cls=Pcli, invoke_without_command=True)
@click.option("--version", is_flag=True)
@click.option("--list", is_flag=True)
@click.pass_context
def cli(ctx, version, list):
    if not ctx.invoked_subcommand:
        if version:
            click.echo(__version__)
        elif list:
            for cmd, subcommands in ctx.command.discovered_commands.items():
                click.echo(cmd)
                for subcommand in subcommands:
                    click.echo(f"  {subcommand}")
        else:
            click.echo(ctx.get_help())


if __name__ == "__main__":
    cli()
