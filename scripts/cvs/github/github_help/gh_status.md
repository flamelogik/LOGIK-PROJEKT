# gh status Command

The status command prints information about your work on GitHub across all the repositories you're subscribed to, including:

*   Assigned Issues
*   Assigned Pull Requests
*   Review Requests
*   Mentions
*   Repository Activity (new issues/pull requests, comments)

## Usage

```
gh status [flags]
```

## Flags

*   `-e`, `--exclude strings`: Comma separated list of repos to exclude in owner/name format
*   `-o`, `--org string`: Report status within an organization

## Inherited Flags

*   `--help`: Show help for command

## Examples

```bash
$ gh status -e cli/cli -e cli/go-gh # Exclude multiple repositories
$ gh status -o cli # Limit results to a single organization
```

## Learn More

Use `gh <command> <subcommand> --help` for more information about a command.
Read the manual at https://cli.github.com/manual
Learn about exit codes using `gh help exit-codes`
Learn about accessibility experiences using `gh help accessibility`
