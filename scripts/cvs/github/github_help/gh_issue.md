# gh issue Command

Work with GitHub issues.

## Usage

```
gh issue <command> [flags]
```

## General Commands

*   `create`: Create a new issue
*   `list`: List issues in a repository
*   `status`: Show status of relevant issues

## Targeted Commands

*   `close`: Close issue
*   `comment`: Add a comment to an issue
*   `delete`: Delete issue
*   `develop`: Manage linked branches for an issue
*   `edit`: Edit issues
*   `lock`: Lock issue conversation
*   `pin`: Pin a issue
*   `reopen`: Reopen issue
*   `transfer`: Transfer issue to another repository
*   `unlock`: Unlock issue conversation
*   `unpin`: Unpin a issue
*   `view`: View an issue

## Flags

*   `-R`, `--repo [HOST/]OWNER/REPO`: Select another repository using the `[HOST/]OWNER/REPO` format

## Inherited Flags

*   `--help`: Show help for command

## Arguments

An issue can be supplied as argument in any of the following formats:

*   by number, e.g. "123"; or
*   by URL, e.g. "https://github.com/OWNER/REPO/issues/123".

## Examples

```bash
$ gh issue list
$ gh issue create --label bug
$ gh issue view 123 --web
```

## Learn More

Use `gh <command> <subcommand> --help` for more information about a command.
Read the manual at https://cli.github.com/manual
Learn about exit codes using `gh help exit-codes`
Learn about accessibility experiences using `gh help accessibility`
