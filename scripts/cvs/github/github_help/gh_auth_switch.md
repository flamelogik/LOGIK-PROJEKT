# gh auth switch Command

Switch the active account for a GitHub host.

## Usage

```
gh auth switch [flags]
```

## Flags

*   `-h`, `--hostname string`: The hostname of the GitHub instance to switch account for
*   `-u`, `--user string`: The account to switch to

## Inherited Flags

*   `--help`: Show help for command

## Examples

```bash
# Select what host and account to switch to via a prompt
gh auth switch

# Switch the active account on a specific host to a specific user
gh auth switch --hostname enterprise.internal --user monalisa
```

## Learn More

Use `gh <command> <subcommand> --help` for more information about a command.
Read the manual at https://cli.github.com/manual
Learn about exit codes using `gh help exit-codes`
Learn about accessibility experiences using `gh help accessibility`
