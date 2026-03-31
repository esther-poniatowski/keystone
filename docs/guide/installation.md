# Installation

## Prerequisites

- Python >= 3.12
- conda (recommended) or pip

## Using pip

The package installs directly from the GitHub repository:

```sh
pip install git+https://github.com/{{ github_user }}/{{ repo_name }}.git
```

## Using conda

The package is available on the `{{ channel_name }}` channel:

```sh
conda install -c {{ channel_name }} {{ package_name }}
```

## From Source

1. Clone the repository:

   ```sh
   git clone https://github.com/{{ github_user }}/{{ repo_name }}.git
   ```

2. Create a dedicated environment and install:

   ```sh
   cd {{ repo_name }}
   conda env create -f environment.yml
   conda activate {{ package_name }}
   ```
