# gh auth setup-git Command

This command configures `git` to use GitHub CLI as a credential helper.

## Usage

```
gh auth setup-git [flags]
```

## Flags

*   `-f`, `--force --hostname`: Force setup even if the host is not known. Must be used in conjunction with `--hostname`
*   `-h`, `--hostname string`: The hostname to configure git for

## Inherited Flags

*   `--help`: Show help for command

## Examples

```bash
# Configure git to use GitHub CLI as the credential helper for all authenticated hosts
gh auth setup-git

# Configure git to use GitHub CLI as the credential helper for enterprise.internal host
gh auth setup-git --hostname enterprise.internal
```

## Learn More

Use `gh <command> <subcommand> --help` for more information about a command.
Read the manual at https://cli.github.com/manual
Learn about exit codes using `gh help exit-codes`
Learn about accessibility experiences using `gh help accessibility`
