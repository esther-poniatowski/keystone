# Command-Line Conventions

<!-- Shared conventions of the command-line interfaces of the tools built from this template. -->

The tools of the workspace name their options after the role that each option plays, and resolve
their root, their settings and their paths in one way, so that every tool behaves predictably. A
tool keeps a name of its own only for a concept that belongs to its domain, and that name must not
reuse a name reserved below. Each rule below states the principle that selects it.

## Reserved Options

| Option | Role |
| --- | --- |
| `-r`, `--root PATH` | Folder from which the tool finds its settings file and resolves the paths written in that file. |
| `-c`, `--config PATH` | Settings file of the tool. |
| `-o`, `--output PATH` | One output file. Without it, a text output goes to the standard output. |
| `--output-dir PATH` | Folder that receives several output files. |
| `--format {text,json,sarif}` | Format of a report. A tool offers the formats it can write; no tool offers a standalone `--json`. |
| `--dry-run` | Show what the command would change, write nothing, and exit with status 0. |
| `--check` | Write nothing, and exit with status 1 when something would change, for a check in continuous integration. |
| `--force` | Allow the command to overwrite or delete a file that it cannot regenerate. |
| `--yes` | Answer yes to every confirmation. |
| `-v`, `--version` | Print the version of the tool. |
| `--verbose` / `-q`, `--quiet` | Raise or lower the amount of output. `--verbose` has no short form. |

The exit status is 0 on success, 1 when a check or a validation finds a problem, and 2 on a usage
or configuration error.

## Root

A tool that works on a project resolves its root in this order, and stops at the first answer:

1. the option `--root`;
2. the environment variable `<TOOL>_ROOT`, such as `KTISMA_ROOT`;
3. the nearest ancestor of the current folder that holds the settings file of the tool, in
   `config/tools/` or at its own level;
4. the current folder.

A tool that stacks one settings file per folder, such as Ktisma, takes the outermost ancestor at
step 3 instead, and its documentation says so. A tool without a settings file skips step 3.

*Principle.* An explicit value overrides an implicit one, and an environment variable serves editors
and continuous integration without a change of command. The search of step 3 lets a command run
from any subfolder of a project, as Git and pytest do.

## Settings File

- **Name.** The settings file of a tool is named after the tool: `<tool>.yml` for a file in YAML,
  `<tool>.toml` for a file in TOML. The name carries no leading dot, and the files of a tool that
  stacks one file per folder carry the same name.
- **Place.** Without `--config`, the tool reads `config/tools/<tool>.<ext>` below the root, or
  `<tool>.<ext>` at the root. When both exist, the tool stops with an error that names both.
- **Absence.** Without any settings file, the tool runs on its built-in defaults. A file named by
  `--config` and absent is an error.

*Principle.* One name per tool makes the file recognizable in any listing. An error on two
competing files fails fast, where a silent precedence would apply a file that the researcher does
not expect.

## Paths

- A path given on the command line is relative to the current folder.
- A path written in a settings file is relative to the root.

*Principle.* A shell completes a path from the current folder, so a path typed on the command line
must be read from there. A path written in a settings file must not depend on the place of that
file, so that the file moves between the root and `config/tools/` without an edit.

## Writing Files

- A command overwrites, without `--force`, the files that it derives and can regenerate, such as a
  built document or a generated index.
- A command does not overwrite or delete a file that it cannot regenerate, such as a source, a file
  written by the researcher, or a scaffolded file that the researcher may have edited. Without
  `--force`, it stops with an error that names the file.
- A command that deletes or changes files outside its outputs asks for a confirmation on a
  terminal. `--yes` answers the confirmation. Without a terminal and without `--yes`, the command
  stops with an error.

*Principle.* Regenerating a derived file loses nothing, whereas overwriting any other file may lose
work. A command run by a script must never wait for an answer that no one will give.

## Renaming an Option

The tools serve consumers that the researcher controls. A renamed option, environment variable or
settings file therefore loses its former name in the same change, and every consumer is updated in
the same session. A consumer that pins an earlier release keeps the former name until its pin is
raised.
