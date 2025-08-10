# gh repo Command

Work with GitHub repositories.

## Usage

```
gh repo <command> [flags]
```

## General Commands

*   `create`: Create a new repository
*   `list`: List repositories owned by user or organization

## Targeted Commands

*   `archive`: Archive a repository
*   `autolink`: Manage autolink references
*   `clone`: Clone a repository locally
*   `delete`: Delete a repository
*   `deploy-key`: Manage deploy keys in a repository
*   `edit`: Edit repository settings
*   `fork`: Create a fork of a repository
*   `gitignore`: List and view available repository gitignore templates
*   `license`: Explore repository licenses
*   `rename`: Rename a repository
*   `set-default`: Configure default repository for this directory
*   `sync`: Sync a repository
*   `unarchive`: Unarchive a repository
*   `view`: View a repository

## Flags

*   `-R`, `--repo [HOST/]OWNER/REPO`: Select another repository using the `[HOST/]OWNER/REPO` format

## Inherited Flags

*   `--help`: Show help for command

## Arguments

A repository can be supplied as an argument in any of the following formats:

*   "OWNER/REPO"
*   by URL, e.g. "https://github.com/OWNER/REPO"

## Examples

```bash
$ gh repo create
$ gh repo clone cli/cli
$ gh repo view --web
```

## Learn More

Use `gh <command> <subcommand> --help` for more information about a command.
Read the manual at https://cli.github.com/manual
Learn about exit codes using `gh help exit-codes`
Learn about accessibility experiences using `gh help accessibility`
