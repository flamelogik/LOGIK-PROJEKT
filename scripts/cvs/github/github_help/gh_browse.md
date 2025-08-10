# gh browse Command

Transition from the terminal to the web browser to view and interact with:

- Issues
- Pull requests
- Repository content
- Repository home page
- Repository settings

## Usage

```
gh browse [<number> | <path> | <commit-sha>] [flags]
```

## Flags

*   `-b`, `--branch string`: Select another branch by passing in the branch name
*   `-c`, `--commit string[="last"]`: Select another commit by passing in the commit SHA, default is the last commit
*   `-n`, `--no-browser`: Print destination URL instead of opening the browser
*   `-p`, `--projects`: Open repository projects
*   `-r`, `--releases`: Open repository releases
*   `-R`, `--repo [HOST/]OWNER/REPO`: Select another repository using the [HOST/]OWNER/REPO format
*   `-s`, `--settings`: Open repository settings
*   `-w`, `--wiki`: Open repository wiki

## Inherited Flags

*   `--help`: Show help for command

## Arguments

A browser location can be specified using arguments in the following format:

*   by number for issue or pull request, e.g. "123"; or
*   by path for opening folders and files, e.g. "cmd/gh/main.go"; or
*   by commit SHA

## Examples

```bash
# Open the home page of the current repository
gh browse

# Open the script directory of the current repository
gh browse script/

# Open issue or pull request 217
gh browse 217

# Open commit page
gh browse 77507cd94ccafcf568f8560cfecde965fcfa63

# Open repository settings
gh browse --settings

# Open main.go at line 312
gh browse main.go:312

# Open main.go with the repository at head of bug-fix branch
gh browse main.go --branch bug-fix

# Open main.go with the repository at commit 775007cd
gh browse main.go --commit=77507cd94ccafcf568f8560cfecde965fcfa63
```

## Environment Variables

To configure a web browser other than the default, use the BROWSER environment variable.

## Learn More

Use `gh <command> <subcommand> --help` for more information about a command.
Read the manual at https://cli.github.com/manual
Learn about exit codes using `gh help exit-codes`
Learn about accessibility experiences using `gh help accessibility`
