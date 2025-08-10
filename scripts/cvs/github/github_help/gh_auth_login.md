# gh auth login Command

Authenticate with a GitHub host.

## Usage

```
gh auth login [flags]
```

## Flags

*   `-p`, `--git-protocol string`: The protocol to use for git operations on this host: `{ssh|https}`
*   `-h`, `--hostname string`: The hostname of the GitHub instance to authenticate with
*   `--insecure-storage`: Save authentication credentials in plain text instead of credential store
*   `-s`, `--scopes strings`: Additional authentication scopes to request
*   `--skip-ssh-key`: Skip generate/upload SSH key prompt
*   `-w`, `--web`: Open a browser to authenticate
*   `--with-token`: Read token from standard input

## Inherited Flags

*   `--help`: Show help for command

## Examples

```bash
# Start interactive setup
gh auth login

# Authenticate against <github.com> by reading the token from a file
gh auth login --with-token < mytoken.txt

# Authenticate with specific host
gh auth login --hostname enterprise.internal
```

## Learn More

Use `gh <command> <subcommand> --help` for more information about a command.
Read the manual at https://cli.github.com/manual
Learn about exit codes using `gh help exit-codes`
Learn about accessibility experiences using `gh help accessibility`
