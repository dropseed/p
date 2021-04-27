import click
import cls
from cls import clevents

cls.project_key = "x"
cls.debug = True

from .groups import Group
from . import __version__


class Pcli(click.Group):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.group = Group()
        ctx_settings = dict(ignore_unknown_options=True)

        for command in self.group.commands.values():
            # add all commands by full name (so db:load is available)
            # but hide if they will be in a group also
            @click.command(
                command.name,
                help=f"Using: {command.cmd}",
                context_settings=ctx_settings,
                hidden=bool(command.group_name),
            )
            @click.argument("cmd_args", nargs=-1, type=click.UNPROCESSED)
            @click.pass_context
            def func(ctx, cmd_args):
                self.group.do_command(ctx.info_name, cmd_args)

            self.add_command(func)

        for group in self.group.subgroups.values():

            @click.group(
                group.name, context_settings=ctx_settings, invoke_without_command=False
            )
            @click.pass_context
            def group_func(ctx):
                ctx.meta["p_group"] = ctx.info_name

            self.add_command(group_func)

            for command in group.commands.values():

                @click.command(
                    command.group_command_name,
                    help=f"Using: {command.cmd}",
                    context_settings=ctx_settings,
                )
                @click.argument("cmd_args", nargs=-1, type=click.UNPROCESSED)
                @click.pass_context
                def func(ctx, cmd_args):
                    # invoke the command by its full name
                    self.group.do_command(
                        f"{ctx.meta['p_group']}:{ctx.info_name}", cmd_args
                    )

                group_func.add_command(func)


@click.group(cls=Pcli, invoke_without_command=True)
@click.option("--version", is_flag=True)
@click.pass_context
def cli(ctx, version):
    if not ctx.invoked_subcommand:
        if version:
            clevents.command("version")
            click.echo(__version__)
        else:
            clevents.command("help")
            click.echo(ctx.get_help())
    else:
        clevents.command(f"custom:")


if __name__ == "__main__":
    cli()
