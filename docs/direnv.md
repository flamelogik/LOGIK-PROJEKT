# Environment Variables in VFX Projects

Environment variables are widely used in VFX to manage project-specific settings dynamically. By using these variables, artists and developers can configure paths, software versions, and color settings without hard-coding them into scripts, enhancing flexibility and enabling easy adaptation across different projects or pipelines. Common uses include setting paths for textures, renders, color management (like OCIO configurations), and defining variables that control file versioning and shot-specific configurations.

## Using `direnv` for PROJEKT Environment Variables

[`direnv`](https://direnv.net/) is a tool that automatically loads environment variables from a `.envrc` file when entering a project directory. This is particularly useful in VFX, where each project may require unique configurations. With `direnv`, environment variables specific to a project (such as paths for assets or OCIO configurations) are activated only within that project’s directory, keeping the workspace organized and reducing potential conflicts across projects.

### Installation of `direnv`

#### Rocky Linux 9
1. **Install via DNF**:
   ```bash
   sudo dnf install direnv
2. **Hook direnv into the shell** 
    
    add the following to your shell configuration file (e.g., ~/.bashrc or ~/.zshrc):
    
        eval "$(direnv hook bash)" # or "zsh" if using zsh

#### macOS
**Option 1: Install without Homebrew**

1. Download the latest release from the direnv GitHub releases page.
    - Choose the appropriate binary for macOS, typically named **direnv.darwin-arm64**


    Rename the binary to direnv and make it executable:

        
        mv path/to/downloaded/direnv.darwin-amd64 /usr/local/bin/direnv
        chmod +x /usr/local/bin/direnv
        

**Option 2: Install with Homebrew**

        brew install direnv




Hook into the shell by adding this to your shell configuration file:

        eval "$(direnv hook bash)" # or "zsh" if using zsh
