# gh auth logout Command

Remove authentication for a GitHub account.

## Usage

```
gh auth logout [flags]
```

## Flags

*   `-h`, `--hostname string`: The hostname of the GitHub instance to log out of
*   `-u`, `--user string`: The account to log out of

## Inherited Flags

*   `--help`: Show help for command

## Examples

```bash
# Select what host and account to log out of via a prompt
gh auth logout

# Log out of a specific host and specific account
gh auth logout --hostname enterprise.internal --user monalisa
```

## Learn More

Use `gh <command> <subcommand> --help` for more information about a command.
Read the manual at https://cli.github.com/manual
Learn about exit codes using `gh help exit-codes`
Learn about accessibility experiences using `gh help accessibility`
