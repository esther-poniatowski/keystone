<!--
TODO: Replace all placeholders of the form `{{ ... }}` with project-specific values.

- `{{ repo_name }}`          : Repository name
- `{{ github_user }}`        : GitHub username of the project owner
- `{{ package_name }}`       : Python package name
- `{{ channel_name }}`       : Conda channel name
- `{{ contact@example.com }}`: Contact email address

TODO: Review and adapt all descriptive content to reflect the specific details of the project (e.g.,
project description, feature list, variable names, file paths, command-line examples, documentation
links).
-->
# {{ repo_name }}

[![Label](https://url.to/badge.svg)](https://url.to/target)

Project Description (2-3 sentences)

**Project Status**: Active Development

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Documentation](#documentation)
- [Support](#support)
- [Contributing](#contributing)
- [Acknowledgments](#acknowledgments)
- [License](#license)

## Overview

---

## Features

- [X] **Feature 1:** Description.
- [ ] **Feature 2:** Description.

---

## Installation

To install the package and its dependencies, use one of the following methods:

### Using Pip Installs Packages

Install the package from the GitHub repository URL via `pip`:

```bash
pip install git+https://github.com/{{ github_user }}/{{ repo_name }}.git
```

### Using Conda

Install the package from the private channel {{ channel_name }}:

```bash
conda install {{ package_name }} -c {{ channel_name }}
```

### From Source

1. Clone the repository:

      ```bash
      git clone https://github.com/{{ github_user }}/{{ repo_name }}.git
      ```

2. Create a dedicated virtual environment:

      ```bash
      cd {{ repo_name }}
      conda env create -f environment.yml
      ```

---

## Usage

### Command Line Interface (CLI)

To display the list of available commands and options:

```sh
{{ package_name }} --help
```

### Programmatic Usage

To use the package programmatically in Python:

```python
import {{ package_name }}
```

---

## Configuration

### Environment Variables

|Variable|Description|Default|Required|
|---|---|---|---|
|`VAR_1`|Description 1|None|Yes|
|`VAR_2`|Description 2|`false`|No|

### Configuration File

Configuration options are specified in YAML files located in the `config/` directory.

The canonical configuration schema is provided in [`config/default.yaml`](config/default.yaml).

```yaml
var_1: value1
var_2: value2
```

---

## Documentation

- [User Guide](https://{{ github_user }}.github.io/{{ repo_name }}/guide/)
- [API Documentation](https://{{ github_user }}.github.io/{{ repo_name }}/api/)

> [!NOTE]
> Documentation can also be browsed locally from the [`docs/`](docs/) directory.

## Support

**Issues**: [GitHub Issues](https://github.com/{{ github_user }}/{{ repo_name }}/issues)

**Email**: `{{ contact@example.com }}`

---

## Contributing

Please refer to the [contribution guidelines](CONTRIBUTING.md).

---

## Acknowledgments

### Authors & Contributors

**Author**: @{{ github_user }}

**Contact**: `{{ contact@example.com }}`

For academic use, please cite using the GitHub "Cite this repository" feature to
generate a citation in various formats.

Alternatively, refer to the [citation metadata](CITATION.cff).

### Third-Party Dependencies

- **[Library A](link)** - Purpose
- **[Library B](link)** - Purpose

---

## License

This project is licensed under the terms of the [GNU General Public License v3.0](LICENSE).
