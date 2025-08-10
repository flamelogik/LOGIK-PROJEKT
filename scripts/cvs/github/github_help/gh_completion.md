# gh completion Command

Generate shell completion scripts for GitHub CLI commands.

## Usage

```
gh completion -s <shell>
```

## Flags

*   `-s`, `--shell string`: Shell type: `{bash|zsh|fish|powershell}`

## Inherited Flags

*   `--help`: Show help for command

## Examples

```bash
### bash

First, ensure that you install `bash-completion` using your package manager.

After, add this to your `~/.bash_profile`:

	eval "$(gh completion -s bash)"

### zsh

Generate a `_gh` completion script and put it somewhere in your `$fpath`:

	gh completion -s zsh > /usr/local/share/zsh/site-functions/_gh

Ensure that the following is present in your `~/.zshrc`:

	autoload -U compinit
	compinit -i

Zsh version 5.7 or later is recommended.

### fish

Generate a `gh.fish` completion script:

	gh completion -s fish > ~/.config/fish/completions/gh.fish

### PowerShell

Open your profile script with:

	mkdir -Path (Split-Path -Parent $profile) -ErrorAction SilentlyContinue
	notepad $profile

Add the line and save the file:

	Invoke-Expression -Command $(gh completion -s powershell | Out-String)
```

## Learn More

Use `gh <command> <subcommand> --help` for more information about a command.
Read the manual at https://cli.github.com/manual
Learn about exit codes using `gh help exit-codes`
Learn about accessibility experiences using `gh help accessibility`
