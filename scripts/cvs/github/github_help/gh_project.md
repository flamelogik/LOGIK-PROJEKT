# gh project Command

Work with GitHub Projects.

## Usage

```
gh project <command> [flags]
```

## Available Commands

*   `close`: Close a project
*   `copy`: Copy a project
*   `create`: Create a project
*   `delete`: Delete a project
*   `edit`: Edit a project
*   `field-create`: Create a field in a project
*   `field-delete`: Delete a field in a project
*   `field-list`: List the fields in a project
*   `item-add`: Add a pull request or an issue to a project
*   `item-archive`: Archive an item in a project
*   `item-create`: Create a draft issue item in a project
*   `item-delete`: Delete an item from a project by ID
*   `item-edit`: Edit an item in a project
*   `item-list`: List the items in a project
*   `link`: Link a project to a repository or a team
*   `list`: List the projects for an owner
*   `mark-template`: Mark a project as a template
*   `unlink`: Unlink a project from a repository or a team
*   `view`: View a project

## Inherited Flags

*   `--help`: Show help for command

## Examples

```bash
$ gh project create --owner monalisa --title "Roadmap"
$ gh project view 1 --owner cli --web
$ gh project field-list 1 --owner cli
$ gh project item-list 1 --owner cli
```

## Learn More

Use `gh <command> <subcommand> --help` for more information about a command.
Read the manual at https://cli.github.com/manual
Learn about exit codes using `gh help exit-codes`
Learn about accessibility experiences using `gh help accessibility`
