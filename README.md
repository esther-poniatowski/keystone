# ProjectTemplate

## Set up

To work on this project, follow the steps below:

### Initialize a local copy

1. Navigate to the local directory where the root folder of the repository should reside.
  
2. Copy the URL of the project in the "Code" section of the main page.<br>
   Format: ```git@github.com:<owner-name>/<repository-name>.git```
  
3. Clone the repository:
```
git clone <repository-url>
```

### Set Up the Commit Template

1. Navigate inside the repository directory:
```
cd <repository-name>
```
   
2. Register the file to use as the commit template:
```
git config commit.template .github/commit-template.txt
```
   
3. Verify the configuration:
```
git config --get commit.template
```





