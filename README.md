# p

## The problem

Every project is different, but damn near every project comes with a set of
development commands or scripts to run common actions. And if it doesn't, then
it probably should.

Different languages, people, and tools accomplish this in different ways. Some
projects use the good ol' `Makefile`, while others use `package.json` "scripts",
bash scripts, `rake`, `fabric`, and so on and so on...

It can often take several minutes just to figure out how to *start* working on
something.

## The solution

The goal of *p* is to make it easier for you to work on projects -- regardless
of language, layout, or tools. Context switching sucks, and p makes it easier to
jump into a new (or old) project by providing a simple command that you only
need to learn once. If you personally decide to use p, you should be able to
spend more time doing the work you set out to do, and less time
(re-)familiarizing yourself with a project every time you sit down.

It does this by providing the `p` command. Running `p` will show you which
commands are available for the project you are on.

For example:
```sh
$ cd project
$ p
Usage: p [OPTIONS] COMMAND [ARGS]...

Options:
  --version
  --list
  --help     Show this message and exit.

Commands:
  mypy        Using: ./scripts/mypy
  pre-commit  Using: ./scripts/pre-commit
  setup       Using: pipenv sync --dev
  test        Using: ./scripts/test
```

It does this by discovering scripts and commands that already exist within the
project, and by adding automatically generated commands for known package
managers or tools.

**P is not a project requirement or dependency.** it is tool that *you* can choose
to make your own life easier (or the lives of your p-using coworkers and
contributors). Nothing in your project should depend on p, but rather conform to
p-friendly standards which are usable with or without p itself.

Ideally, p will "just work". But if not, it is often in your project's best
interest to design a developer experience that *would* work if someone were
using p. That is -- script out some of the most commonly used actions for your
project (`install`, `test`, `deploy`, etc.), and put them in a uniform place
where contributors can easily figure out how to use them. P is simply a small
abstraction layer to make it even easier yet for people that use it.

## Put commands where p can find them

### `./scripts` or `./bin`

P will automatically find executable scripts (with no file extension) in
`./scripts` or `./bin`. The filename will be added as a command so that they can
simply be run by doing `p {script_name}`.

```sh
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

Will result in
```sh
$ p
Usage: p [OPTIONS] COMMAND [ARGS]...

Options:
  --version
  --list
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

If there is a `Makefile` in your project, p will automatically parse `.PHONY`
and make those commands available via p too. So if you have a `make test`, it
will also be available to p users via `p test`.

## `package.json` scripts

TODO write something

## Automatic commands

P will automatically generate commands for known package managers. These can be
overridden by providing your own script of the same name in one of the
recognized locations. So, for example, if you want contributors to use something
more specific than a regular `yarn install`, just add an "install" script to
`package.json`.

Currently supported:
- `package.json`
  - `npm install` as `p install`
- `yarn.lock`
  - `yarn install` as `p install`
- `.terraform` or `terraform.tfstate`
  - `terraform init` as `p install`
  - `terraform apply` as `p deploy`
- `Pipfile.lock`
  - `pipenv sync --dev` as `p install`
- `combine.yml`
  - `combine work` as `p work`
- `Cartfile` or `Cartfile.resolved`
  - `carthage update` as `p install`


## Git hooks

P also provides automatically installation of git hooks, if you use commands
named `pre-commit` or `post-merge`. On `p install` or `p {git_hook_name}` it will prompt you to install it into your local `.githooks`.

## Chaining scripts together (advanced)

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

## Inspired by

- [Dropseed's](https://github.com/dropseed) project-cli (private)
- [Flint Hills Design's](https://github.com/flinthillsdesign) fhd-cli (private)
- https://github.com/github/scripts-to-rule-them-all
- https://github.com/bkeepers/strappydoo
- having too many projects
