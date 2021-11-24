import click
from click_didyoumean import DYMGroup
import cls_client

from .groups import Group
from . import __version__


cls_client.set_project_key("cls_pk_jlBkK2J8tNL36UfIZFgn8LqO")
cls_client.set_project_slug("p")
cls_client.set_version(__version__)


class Pcli(DYMGroup):
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
            @cls_client.track_command(name=command.name)
            def func(ctx, cmd_args):
                self.group.do_command(ctx.info_name, cmd_args)

            self.add_command(func)

        for group in self.group.subgroups.values():

            @click.group(
                group.name,
                cls=DYMGroup,
                context_settings=ctx_settings,
                invoke_without_command=False,
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


@click.group(cls=Pcli)
@click.version_option(__version__)
@click.pass_context
def cli(ctx):
    pass


if __name__ == "__main__":
    cli()
