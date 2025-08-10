# gh auth refresh Command

Expand or fix the permission scopes for stored credentials for active account.

## Usage

```
gh auth refresh [flags]
```

## Flags

*   `-h`, `--hostname string`: The GitHub host to use for authentication
*   `--insecure-storage`: Save authentication credentials in plain text instead of credential store
*   `-r`, `--remove-scopes strings`: Authentication scopes to remove from gh
*   `--reset-scopes`: Reset authentication scopes to the default minimum set of scopes
*   `-s`, `--scopes strings`: Additional authentication scopes for gh to have

## Inherited Flags

*   `--help`: Show help for command

## Examples

```bash
# Open a browser to add write:org and read:public_key scopes
gh auth refresh --scopes write:org,read:public_key

# Open a browser to ensure your authentication credentials have the correct minimum scopes
gh auth refresh

# Open a browser to idempotently remove the delete_repo scope
gh auth refresh --remove-scopes delete_repo

# Open a browser to re-authenticate with the default minimum scopes
gh auth refresh --reset-scopes
```

## Learn More

Use `gh <command> <subcommand> --help` for more information about a command.
Read the manual at https://cli.github.com/manual
Learn about exit codes using `gh help exit-codes`
Learn about accessibility experiences using `gh help accessibility`
