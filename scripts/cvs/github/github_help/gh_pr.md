# gh pr Command

Work with GitHub pull requests.

## Usage

```
gh pr <command> [flags]
```

## General Commands

*   `create`: Create a pull request
*   `list`: List pull requests in a repository
*   `status`: Show status of relevant pull requests

## Targeted Commands

*   `checkout`: Check out a pull request in git
*   `checks`: Show CI status for a single pull request
*   `close`: Close a pull request
*   `comment`: Add a comment to a pull request
*   `diff`: View changes in a pull request
*   `edit`: Edit a pull request
*   `lock`: Lock pull request conversation
*   `merge`: Merge a pull request
*   `ready`: Mark a pull request as ready for review
*   `reopen`: Reopen a pull request
*   `review`: Add a review to a pull request
*   `unlock`: Unlock pull request conversation
*   `update-branch`: Update a pull request branch
*   `view`: View a pull request

## Flags

*   `-R`, `--repo [HOST/]OWNER/REPO`: Select another repository using the `[HOST/]OWNER/REPO` format

## Inherited Flags

*   `--help`: Show help for command

## Arguments

A pull request can be supplied as argument in any of the following formats:

*   by number, e.g. "123";
*   by URL, e.g. "https://github.com/OWNER/REPO/pull/123"; or
*   by the name of its head branch, eg. "patch-1" or "OWNER:patch-1".

## Examples

```bash
$ gh pr checkout 353
$ gh pr create --fill
$ gh pr view --web
```

## Learn More

Use `gh <command> <subcommand> --help` for more information about a command.
Read the manual at https://cli.github.com/manual
Learn about exit codes using `gh help exit-codes`
Learn about accessibility experiences using `gh help accessibility`
