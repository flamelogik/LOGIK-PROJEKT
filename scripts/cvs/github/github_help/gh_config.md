# gh config Command

Display or change configuration settings for gh.

## Usage

```
gh config <command> [flags]
```

## Current Respected Settings

*   `git_protocol`: the protocol to use for git clone and push operations `{https | ssh}` (default `https`)
*   `editor`: the text editor program to use for authoring text
*   `prompt`: toggle interactive prompting in the terminal `{enabled | disabled}` (default `enabled`)
*   `prefer_editor_prompt`: toggle preference for editor-based interactive prompting in the terminal `{enabled | disabled}` (default `disabled`)
*   `pager`: the terminal pager program to send standard output to
*   `http_unix_socket`: the path to a Unix socket through which to make an HTTP connection
*   `browser`: the web browser to use for opening URLs
*   `color_labels`: whether to display labels using their RGB hex color codes in terminals that support truecolor `{enabled | disabled}` (default `disabled`)
*   `accessible_colors`: whether customizable, 4-bit accessible colors should be used `{enabled | disabled}` (default `disabled`)
*   `accessible_prompter`: whether an accessible prompter should be used `{enabled | disabled}` (default `disabled`)
*   `spinner`: whether to use a animated spinner as a progress indicator `{enabled | disabled}` (default `enabled`)

## Available Commands

*   `clear-cache`: Clear the cli cache
*   `get`: Print the value of a given configuration key
*   `list`: Print a list of configuration keys and values
*   `set`: Update configuration with a value for the given key

## Inherited Flags

*   `--help`: Show help for command

## Learn More

Use `gh <command> <subcommand> --help` for more information about a command.
Read the manual at https://cli.github.com/manual
Learn about exit codes using `gh help exit-codes`
Learn about accessibility experiences using `gh help accessibility`
