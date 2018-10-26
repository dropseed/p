import click

from .core import discover_commands, do_command
from . import __version__


class Pcli(click.Group):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # builtins = (
        #     "setup",
        #     "work",
        #     "test",
        #     "deploy",
        # )

        for name in discover_commands().keys():

            @click.command(name)
            @click.pass_context
            def func(ctx):
                do_command(ctx.info_name)
                # exit(0 if result else 1)

            self.add_command(func)

        # if os.path.exists(CONFIG_FILENAME):
        #     config = yaml.safe_load(open(CONFIG_FILENAME))
        #     commands = config.get("commands", {})
        #     for name, cmd in commands.items():
        #         @click.command(name)
        #         @click.pass_context
        #         def func(ctx):
        #             do(ctx.info_name)
        #
        #         self.add_command(func)


@click.group(cls=Pcli, invoke_without_command=True)
@click.option("--version", is_flag=True)
@click.pass_context
def cli(ctx, version):
    if not ctx.invoked_subcommand:
        if version:
            click.echo(__version__)
        else:
            click.echo(ctx.get_help())


# @cli.command()
# def foo():
#     print('ok')
#     print(discover_commands())


if __name__ == "__main__":
    cli()
