# Command-Line Conventions

<!-- Shared conventions of the command-line interfaces of the tools built from this template. -->

The tools of the workspace name their options after the role that each option plays, and resolve
their root, their configuration and their paths in one way, so that every tool behaves predictably. A
tool keeps a name of its own only for a concept that belongs to its domain, and that name must not
reuse a name reserved below. Each rule below states the principle that selects it.

## Reserved Options

| Option | Role |
| --- | --- |
| `-r`, `--root PATH` | Folder from which the tool finds its configuration file and resolves the paths written in that file. |
| `-c`, `--config PATH` | Configuration file of the tool. |
| `-o`, `--output PATH` | One output file. Without it, a text output goes to the standard output. |
| `--output-dir PATH` | Folder that receives several output files. |
| `--format {text,json,sarif}` | Format of a report. A tool offers the formats it can write; no tool offers a standalone `--json`. |
| `--dry-run` | Show what the command would change, write nothing, and exit with status 0. |
| `--check` | Write nothing, and exit with status 1 when something would change, for a check in continuous integration. |
| `--force` | Allow the command to overwrite or delete a file that it cannot regenerate. |
| `--yes` | Answer yes to every confirmation. |
| `-v`, `--version` | Print the version of the tool. |
| `--verbose` / `-q`, `--quiet` | Raise or lower the amount of output. `--verbose` has no short form. |

## Exit Statuses

| Status | Meaning |
| --- | --- |
| 0 | The command succeeded. |
| 1 | A check or a validation found a problem, or the researcher declined a confirmation. |
| 2 | The command line or the configuration is wrong. |
| 3 | The environment prevented the command: an unreachable service, a missing prerequisite, a held lock. |

A tool may give a status above 3 to a failure of its own, such as a held lock or an internal error,
and its documentation lists each such status.

*Principle.* A script must tell a command to correct (status 2) from an environment to repair
before a new attempt (status 3). A declined confirmation leaves the requested action undone, so a
command chained after it with `&&` must not run.

## Root

A tool that works on a project resolves its root in this order, and stops at the first answer:

1. the option `--root`;
2. the environment variable `<TOOL>_ROOT`, such as `KTISMA_ROOT`;
3. the nearest ancestor of the current folder that holds the configuration file of the tool, in
   `config/tools/` or at its own level;
4. the current folder.

A tool that stacks one configuration file per folder, such as Ktisma, takes the outermost ancestor at
step 3 instead, and its documentation says so. A tool without a configuration file skips step 3.

*Principle.* An explicit value overrides an implicit one, and an environment variable serves editors
and continuous integration without a change of command. The search of step 3 lets a command run
from any subfolder of a project, as Git and pytest do.

## Configuration File

- **Name.** The configuration file of a tool is named after the tool: `<tool>.yml` for a file in YAML,
  `<tool>.toml` for a file in TOML. The name carries no leading dot, and the files of a tool that
  stacks one file per folder carry the same name.
- **Place.** Without `--config`, the tool reads `config/tools/<tool>.<ext>` below the root, or
  `<tool>.<ext>` at the root. When both exist, the tool stops with an error that names both.
- **Absence.** Without any configuration file, the tool runs on its built-in defaults. A file named by
  `--config` and absent is an error.

*Principle.* One name per tool makes the file recognizable in any listing. An error on two
competing files fails fast, where a silent precedence would apply a file that the researcher does
not expect.

## File Formats

A file whose format is defined by a tool or by the workspace declares that format in the key
`_schema`, as its first key:

```yaml
_schema: ktisma:configuration@2
```

- **Identifier.** The value has the form `<owner>:<type>@<major>`. The owner names the tool or the
  workspace that the file serves. The type of the configuration file of a tool is `configuration`.
- **Version.** The major number rises only when a file that was valid becomes invalid or is read
  differently.
- **Reading.** A tool compares the whole value with the identifiers that it supports. It stops with
  status 2 when the key is absent or holds another value, and the message names the expected value.
  A tool that stacks one file per folder requires the key in the outermost file only.
- **Scope.** A format fixed by an outside standard keeps its own marker, such as the `version` of
  SARIF, or `$schema` in a JSON Schema document. A field that distinguishes the variants of one
  format, such as `kind`, is kept beside `_schema`.

*Principle.* The identifier states the format from the content of the file, so a reader identifies
the file wherever it sits, and a tool rejects the file of another tool by its type.

## Paths

- A path given on the command line is relative to the current folder.
- A path written in a configuration file is relative to the root.

*Principle.* A shell completes a path from the current folder, so a path typed on the command line
must be read from there. A path written in a configuration file must not depend on the place of that
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
configuration file therefore loses its former name in the same change, and every consumer is updated in
the same session. A consumer that pins an earlier release keeps the former name until its pin is
raised.
