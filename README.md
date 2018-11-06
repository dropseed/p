# p

The goal of *p* is to make it easier for you to work on projects -- regardless
of language, layout, or tools. Context switching sucks, and p aims to make it
easier to jump into a new (or old) project by providing commands you only need
to learn once. If you personally decide to use p, you should be able to spend
more time doing the work you set out to do, and less time (re-)familiarizing
yourself with a project every time you sit down.

It does this by providing a basic set of commands that adapt to the project
you're working on. So, when it's time to work on something, you only need to
remember `p setup` to get things installed~~, and `p work` to get going~~. It is a
simple abstraction layer that makes it easier to jump into a project without
needing to remember or dig for the specific steps to get up and running so that
you can actually...do work.

P is not a project requirement or dependency, it is tool that *you* can choose
to make your own life easier (or the lives of your coworkers and contributors).
Nothing in your project should depend on p, but rather conform to p-friendly
standards which are usable with or without p itself.

Beyond that, p does its best to make additional project commands available by
looking in common places. Lots of people use Makefiles, language-specific things
like `package.json` "scripts", or event just a "scripts" directory. P will
automatically look in the typical places and then make anything it finds
available as a p command:
```sh
```

## Scripts

The behavior of each command can be overridden in a handful of different ways.
One of the most universal is to have a `scripts` directory in your project, with
executable scripts written in any language. P will automatically detect and add
these scripts as commands, and anybody not using p you can easily run them
manually (`./scripts/test`).

## Makefile

Another common universal pattern is to use a `Makefile`. If there is a Makefile
in your project, p will automatically parse `.PHONY` and make those commands
available via p too. So if you have a `make test`, it will also be available to
p users via `p test`.

## Specific languages and tools

P is also capable of adapting to common practices in the most popular languages
and tools. In javascript, for example, `package.json` has a nice `scripts` entry
where most project-commands live. P detects those and makes them available
automatically, in addition to changing the behavior of `p setup` to do things
like `npm install`.

# Git hooks

P also provides automatically installation of git hooks, if you use commands
named `pre-commit` or `post-merge`.

# Chaining scripts together

By default, the first match found for a command (ex. `test`) will be used. If
you want to chain together multiple scripts, you can namespace them like
`test-anothertest`. You can further specify *when* they are run by using the
special `-pre-` and `-post-` separators (ex. `test-pre-something`).So the order
of scripts will be:

- `{command}--pre`
- `{command}--pre--{anything}` - sorted alphabetically
- `{command}`
- `{command}--{anything}` - sorted alphabetically
- `{command}--post`
- `{command}--post--{anything}` - sorted alphabetically

# Inspired by

- [Dropseed's](https://github.com/dropseed) project-cli (private)
- [Flint Hills Design's](https://github.com/flinthillsdesign) fhd-cli (private)
- https://github.com/github/scripts-to-rule-them-all
- https://github.com/bkeepers/strappydoo
