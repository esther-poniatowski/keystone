# Getting Started

## Prerequisites

- Python >= 3.12
- conda (recommended) or pip

## Installation

Install {{ package_name }} via pip:

```sh
pip install git+https://github.com/{{ github_user }}/{{ repo_name }}.git
```

Or via conda:

```sh
conda install -c {{ channel_name }} {{ package_name }}
```

Or from source:

```sh
git clone https://github.com/{{ github_user }}/{{ repo_name }}.git
cd {{ repo_name }}
conda env create -f environment.yml
conda activate {{ package_name }}
```

## Quick Start

```sh
{{ package_name }} --help
```

## Next Steps

- [Configuration](configuration.md) -- Configure the package.
- [CLI Reference](cli-reference.md) -- Full list of commands and options.
- [API Reference](../api/index.md) -- Python API documentation.
