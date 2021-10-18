# p

P makes it easier to jump between projects and get work done.
It gathers up all of the available commands/scripts in a repo,
and aliases them to `p <name>`.

**P is not a project requirement or dependency -- it is a personal
tool.** Nothing in your project should depend on p, but rather conform
to p-friendly standards which are usable with or without p itself.
This means that if you use p,
you get the best experience possible.
And for the contributors who don't use p,
at least they get a well-documented and well-maintained developer experience.

If you *personally* start using it,
you'll probably find that `p` is the first thing you run after `cd <project>` to get your bearings and start doing work.

[But... why?](#why)

## Install or update

Don't add it to a project. Add it to your machine, system-wide or user-wide.

```sh
# System-wide or user-wide, not per project
$ pip3 install -U p
```

## What it looks like

```text
$ cd project
$ p
  Usage: p [OPTIONS] COMMAND [ARGS]...

  Options:
  --version
  --help     Show this message and exit.

  Commands:
  compile-assets  Using: npm run compile-assets
  install         Using: ./scripts/install
  load-fixtures   Using: ./scripts/load-fixtures
  pre-commit      Using: ./scripts/pre-commit
  test            Using: ./scripts/test
```

## Supported tools and workflows

Note that p really only supports stuff that we use at [Dropseed](https://www.dropseed.dev/).
**So this list is intentionally short.**
If you use p day-to-day and would like to see support for something not listed here,
[just let us know](https://github.com/dropseed/p/issues)!

### Executable scripts

P will automatically find executable scripts in `./scripts` or `./bin`.

They should have no extension (don't need ".sh") and should be executable (`chmod +x ./scripts/thing`).

The filename will be added as a command so that they can simply be run by doing `p {script-name}`.


For example, this structure:

```text
$ tree scripts/
scripts/
├── compile-assets
├── load-fixtures
├── pre-commit
├── setup
├── start-postgres
├── test
└── work
```

Will result in:

```text
$ p
  Usage: p [OPTIONS] COMMAND [ARGS]...

  Options:
    --version
    --help     Show this message and exit.

  Commands:
    compile-assets  Using: ./scripts/compile-assets
    load-fixtures   Using: ./scripts/load-fixtures
    pre-commit      Using: ./scripts/pre-commit
    setup           Using: ./scripts/setup
    start-postgres  Using: ./scripts/start-postgres
    test            Using: ./scripts/test
    work            Using: ./scripts/work
```

### Makefile

If there is a `Makefile` in your project,
p will automatically parse `.PHONY` and make those commands available via p.
So if you have `make test`,
it will also be available to p users via `p test`.

### package.json scripts

Entries in your `package.json` "scripts" will automatically be mapped to p commands.

For example:

```js
{
  "scripts": {
    "start": "react-scripts start"
  }
}
```

Would result in:

```text
Usage: p [OPTIONS] COMMAND [ARGS]...

Options:
  --version
  --help     Show this message and exit.

Commands:
  start    Using: npm run start
```

## Git hooks

P also provides automatic installation of [git hooks](#using-git-hooks).

For example, if you have a command named `pre-commit`, running `p
install` or `p {git-hook-name}` will prompt you to install
it into your local `.githooks` for the repo.

Then when you run `git commit`,
your `p pre-commit` will be run automatically.

An example of a `pre-commit` script:
```sh
#!/bin/sh -e
black pullapprove --check --exclude migrations
```

## Grouping (advanced)

To make the p help more user friendly you can group and hide commands from the top-level.
This works automatically by using a `:` in your command name.

For example, if you have commands like `db:load` and `db:reset`, you'll get a `db` group.
You can run `p db` to see the subcommands in db, and run `p db load` to run a subcommand.

```text
$ p
  Usage: p [OPTIONS] COMMAND [ARGS]...

  Options:
    --version
    --help     Show this message and exit.

  Commands:
    db

$ p db load
```

(You can also invoke the grouped commands directly as `p db:load`.)

---

## Why

### Context switching sucks

It can often take several minutes just to figure out how to *start* working on
something.

Every project is different, but damn near every project comes with a set of
development commands or scripts to run common actions. And if it doesn’t, then
it probably should.
Different languages, people, and tools accomplish this in different ways. Some
projects use the good ol’ `Makefile`, while others use `package.json` “scripts”,
bash scripts, `rake`, `fabric`, and so on and so on…

P was built to make it easier to jump between projects,
and to save some keystrokes in the meantime.

### Improving developer experience

Ideally, p will “just work”.
But if not,
it is often in your project’s best interest to design a developer experience that *would* work if someone were using p.
That is – script out some of the most commonly used actions for your project (`install`, `test`, `deploy`, etc.),
and put them in a uniform place where contributors can easily figure out how to use them.
Now even the people who don't use p at least have a shot at getting up and running on their own.

### The search for a universal experience

For a long time I've been in search of the perfect development task manager to use on every project.
But that proved to be difficult as the repos got smaller,
more self-contained,
and spread across languages and dependency systems.

Using a Makefile is the closest thing to what I'm looking for.
Most people have `make`.
But there's a lot of things I just can't stand about it
(it's just ugly, and I can't help but think that it feels like some kind of *hack*).

I've settled on the idea of using a "scripts" folder with one-off files for each task.
Usually just bash scripts,
but can easily be a small Python script or something else.
These work basically everywhere,
and it's not hard to tell someone to do `./scripts/test`.

But even the "scripts" pattern doesn't make sense *on every project*.
Some frameworks/projects already come with a solution,
like pre-existing `package.json` "scripts".
Do we really want to create make `scripts/test` that just runs `npm run test`?
Seems dumb.
"I guess we'll use npm scripts on this project..."

So, every project inevitably ends up being a little bit different.
But for those of us that have to constantly jump around between those projects,
p smooths out the rough edges in our day-to-day,
and enables us to make per-project decisions about the developer experience
(and reminds us to even be thinking about that in the first place).

### Bonus: git hooks

Git hooks can be a super useful,
but confusing process to use.
The [gist](https://www.atlassian.com/git/tutorials/git-hooks#local-hooks) is that they generally aren't shared or set up for each user of a project automatically.
There are some tools like [pre-commit](https://pre-commit.com/) or [husky](https://github.com/typicode/husky) that really go the extra mile in creating a system for git hooks,
but a lot of our projects don't really warrant that and,
again,
it felt strange to now have a project dependency in that process...
Do we install that thing per-project even if the project doesn't use that language otherwise?
If we install it on our machines outside the project,
is that now a requirement that can't be required?
Is it even possible to run the hook/linter/formatter without that tool?

Anyway, p embraces git's (implied) attitude about hooks: they're optional.

If a user has p,
then we'll take an extra step to install the git hook for them and put things in place.
It's a nice-to-have.

If you don't have p, then at least you can still run your linters/formatters manually if you want (i.e. `npm run pre-commit`).

And if you need to *require* that those checks are run,
no matter who (or what) commits to the project?
Then set them up in CI.
You don't need anything special to do this --
just run your script/command as a step like a non-p user would.

It's not fancy,
and it works for us.

## Inspired by
- [Dropseed’s](https://github.com/dropseed) project-cli (private)
- [Flint Hills Design’s](https://github.com/flinthillsdesign) fhd-cli (private)
- [https://github.com/github/scripts-to-rule-them-all](https://github.com/github/scripts-to-rule-them-all)
- [https://github.com/bkeepers/strappydoo](https://github.com/bkeepers/strappydoo)
- having too many projects
