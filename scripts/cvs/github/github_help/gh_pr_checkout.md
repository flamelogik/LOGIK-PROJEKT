# gh pr checkout Command (Alias: gh co)

Check out a pull request in git

## Usage

```
gh pr checkout [<number> | <url> | <branch>] [flags]
```

## Flags

*   `-b`, `--branch string`: Local branch name to use (default `[the name of the head branch]`)
*   `--detach`: Checkout PR with a detached HEAD
*   `-f`, `--force`: Reset the existing local branch to the latest state of the pull request
*   `--recurse-submodules`: Update all submodules after checkout

## Inherited Flags

*   `--help`: Show help for command
*   `-R`, `--repo [HOST/]OWNER/REPO`: Select another repository using the `[HOST/]OWNER/REPO` format

## Examples

```bash
# Interactively select a PR from the 10 most recent to check out
gh pr checkout

# Checkout a specific PR
gh pr checkout 32
gh pr checkout https://github.com/OWNER/REPO/pull/32
gh pr checkout feature
```

## Learn More

Use `gh <command> <subcommand> --help` for more information about a command.
Read the manual at https://cli.github.com/manual
Learn about exit codes using `gh help exit-codes`
Learn about accessibility experiences using `gh help accessibility`
