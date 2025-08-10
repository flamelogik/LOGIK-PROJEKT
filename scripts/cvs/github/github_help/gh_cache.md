# gh cache Command

Work with GitHub Actions caches.

## Usage

```
gh cache <command> [flags]
```

## Available Commands

*   `delete`: Delete GitHub Actions caches
*   `list`: List GitHub Actions caches

## Flags

*   `-R`, `--repo [HOST/]OWNER/REPO`: Select another repository using the `[HOST/]OWNER/REPO` format

## Inherited Flags

*   `--help`: Show help for command

## Examples

```bash
$ gh cache list
$ gh cache delete --all
```

## Learn More

Use `gh <command> <subcommand> --help` for more information about a command.
Read the manual at https://cli.github.com/manual
Learn about exit codes using `gh help exit-codes`
Learn about accessibility experiences using `gh help accessibility`
