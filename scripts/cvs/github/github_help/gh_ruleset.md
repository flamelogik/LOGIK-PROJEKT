# gh ruleset Command

Repository rulesets are a way to define a set of rules that apply to a repository.
These commands allow you to view information about them.

## Usage

```
gh ruleset <command> [flags]
```

## Aliases

*   `gh rs`

## Available Commands

*   `check`: View rules that would apply to a given branch
*   `list`: List rulesets for a repository or organization
*   `view`: View information about a ruleset

## Flags

*   `-R`, `--repo [HOST/]OWNER/REPO`: Select another repository using the `[HOST/]OWNER/REPO` format

## Inherited Flags

*   `--help`: Show help for command

## Examples

```bash
$ gh ruleset list
$ gh ruleset view --repo OWNER/REPO --web
$ gh ruleset check branch-name
```

## Learn More

Use `gh <command> <subcommand> --help` for more information about a command.
Read the manual at https://cli.github.com/manual
Learn about exit codes using `gh help exit-codes`
Learn about accessibility experiences using `gh help accessibility`
