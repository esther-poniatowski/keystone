
# Contributing

> [!IMPORTANT]
> To contribute effectively, please conform to those guidelines and use the provided templates.

### Sumbitting Issues

To submit a new issue:

1. In the repository page, navigate to the "Issues" tab and click on "New Issue".
2. Select and fill the issue template.
3. Add relevant labels, assignees, and milestone if applicable.

### Using the Commit Message Template

1. Navigate inside the repository directory:
```
cd <repository-name>
```
   
2. Edit the commit template (`.gitmessage`) to specify the author name.

3. Configure `git` to use this file as a commite template:
```
git config commit.template .gitmessage
```
   
4. Verify the configuration:
```
git config --get commit.template
```

> [!NOTE]
> To write a commit message with this template, adhere to the following format:
>
> - Capitalize the subject, do not add a period at the end
> - Limit the subject line to 50 characters
> - Use the imperative mood in the subject line
> - Separate subject from body with a blank line
> - Wrap the body at 72 characters per line
> - Use the body to explain what and why (not how)
> - Add references to issues or other commits using [GitHub keywords](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/using-keywords-in-issues-and-pull-requests)


## Installation

> [!TIP]
> To set up this project on a local machine, follow the steps below:

### Initialize a local copy of the repository

1. Navigate to the local directory where the root folder of the repository should reside.```
  
2. Clone the repository:

   ```sh
   git clone git@github.com:<owner-name>/<repository-name>.git
   ```

### Create a virtual environment

1. Create an dedicated conda environment containing all the dependencies:
```
conda env create -f environment.yml
```

2. Register the package in "editable mode":
```
conda activate <env-name>
pip install -e /src/<package-name>
```