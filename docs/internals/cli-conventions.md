# Command-Line Conventions

<!-- Shared conventions of the command-line interfaces of the tools built from this template. -->

The tools of the workspace name their options after the role that each option plays, so that an
option behaves the same way in every tool. A tool keeps a name of its own only for a concept that
belongs to its domain, and that name must not reuse a name reserved below.

## Reserved Options

| Option | Role |
| --- | --- |
| `--root PATH` | Folder from which the tool finds its settings file and resolves every relative path. |
| `--config PATH` | Settings file of the tool, relative to the root. |
| `--output PATH` | One output file. Without it, a text output goes to the standard output. |
| `--output-dir PATH` | Folder that receives several output files. |
| `--format {text,json,sarif}` | Format of a report. A tool offers the formats it can write; no tool offers a standalone `--json`. |
| `--dry-run` | Show what the command would change, write nothing, and exit with status 0. |
| `--check` | Write nothing, and exit with status 1 when something would change, for a check in continuous integration. |
| `--force` | Overwrite existing files. |
| `--yes` | Skip a confirmation prompt. |
| `-v`, `--verbose` / `-q`, `--quiet` | Raise or lower the amount of output. |

## Root and Settings File

- **Root.** Without `--root`, the tool takes the nearest ancestor of the current folder that holds
  its settings file, and otherwise the current folder. A tool that stacks one settings file per
  folder, such as Ktisma, takes the outermost ancestor instead, and its documentation says so.
- **Environment variable.** The variable `<TOOL>_ROOT`, such as `KTISMA_ROOT`, sets the root when
  the option is absent. The option takes precedence over the variable.
- **Settings file.** Without `--config`, the tool looks for its file in `config/tools/` below the
  root, then at the root itself: `config/tools/<file>`, then `<file>`. A project keeps the settings
  of its tools in `config/tools/`, so that they do not crowd its root.

## Renaming an Option

A renamed option keeps its former name for one release, as a hidden alias. The alias prints a
warning that names the new option, and the documentation of the tool lists only the new name. The
same applies to a renamed environment variable: the tool reads the former variable when the new one
is absent, and warns.
