# p

P is a command line tool that gathers up all of the available commands/scripts
for a project, and aliases them to `p <name>`. Running `p` by itself will list
out all of the known commands. If you personally start using p, you'll probably
find that `p` is the first thing you run after `cd <project>` to get your
bearings and start doing work.

[Read more here.](https://p.dropseed.io)

## Example

```sh
$ cd project
$ p
Usage: p [OPTIONS] COMMAND [ARGS]...

Options:
--version
--list
--help     Show this message and exit.

Commands:
compile-assets  Using: ./scripts/compile-assets
install         Using: yarn install && pipenv sync --dev
load-fixtures   Using: ./scripts/load-fixtures
pre-commit      Using: ./scripts/pre-commit
test            Using: ./scripts/test
work            Using: combine work
```

## Why?

- Context switching sucks.
- New contributors don't always know where to start.
- To help remind us that developer experience is important, and to take the time
  to add commands/scripts to your project to make life easier for you and your contributors.

## Install it for yourself

```sh
# system-wide or user-wide, not per project
$ pip3 install git+https://github.com/dropseed/p.git#egg=p
```
