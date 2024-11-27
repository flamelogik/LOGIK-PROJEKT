# -------------------------------------------------------------------------- #
# Program Name:     create_ssh_keys-windows.ps1
# Version:          1.1
# Author:           Phil MAN - phil_man@mac.com
# Created:          2024-03-12
# Modified:         2024-03-12

# Changelist:       Added function to create/read 'project_setup_template'.

# Description:      This program will generate SSH keys and prompt the user
#                   to create an encrypted backup zip file.
# -------------------------------------------------------------------------- #

# Define today's date in 'YYYY-MM-DD' format
$today = Get-Date -Format 'yyyy-MM-dd'

# -------------------------------------------------------------------------- #

# Check if required commands are available
$requiredCommands = @('openssl', 'ssh-keygen', '7z')
foreach ($cmd in $requiredCommands) {
    if (-not (Get-Command $cmd -ErrorAction SilentlyContinue)) {
        Write-Host "Error: $cmd is not installed. Exiting."
        exit 1
    }
}

# -------------------------------------------------------------------------- #

# Prompt user to choose a folder using PowerShell
Add-Type -AssemblyName System.Windows.Forms
$folderBrowser = New-Object System.Windows.Forms.FolderBrowserDialog
$folderBrowser.Description = "Choose Folder to Save New SSH Keys"
$folderBrowser.ShowDialog() | Out-Null
$chosen_folder = $folderBrowser.SelectedPath

# Check if user cancelled the folder selection
if (-not $chosen_folder) {
    [System.Windows.Forms.MessageBox]::Show("Operation cancelled. Exiting.", "Error", [System.Windows.Forms.MessageBoxButtons]::OK, [System.Windows.Forms.MessageBoxIcon]::Error)
    exit 1
}

# Create an enclosing folder
$ssh_keys_folder = Join-Path -Path $chosen_folder -ChildPath "ssh_keys-$today"
New-Item -ItemType Directory -Path $ssh_keys_folder -Force | Out-Null

# -------------------------------------------------------------------------- #

# Define the filename for the ssh_key_creation_log
$ssh_key_creation_log = Join-Path -Path $ssh_keys_folder -ChildPath "$today-ssh_key_creation_log.txt"

# Create ssh_key_creation_log in $ssh_keys_folder and redirect stdout and stderr to it
New-Item -ItemType File -Path $ssh_key_creation_log -Force | Out-Null
Start-Transcript -Path $ssh_key_creation_log

# -------------------------------------------------------------------------- #

# Prompt user to enter their email address
$email_address = [Microsoft.VisualBasic.Interaction]::InputBox("You are about to generate new SSH keys. Enter your email address:", "Generate SSH Keys")

# Check if user cancelled the prompt
if (-not $email_address) {
    [System.Windows.Forms.MessageBox]::Show("Operation cancelled. Exiting.", "Error", [System.Windows.Forms.MessageBoxButtons]::OK, [System.Windows.Forms.MessageBoxIcon]::Error)
    exit 1
}

# Check if email address is provided
if ([string]::IsNullOrWhiteSpace($email_address)) {
    [System.Windows.Forms.MessageBox]::Show("Email address cannot be empty. Exiting.", "Error", [System.Windows.Forms.MessageBoxButtons]::OK, [System.Windows.Forms.MessageBoxIcon]::Error)
    exit 1
}

# -------------------------------------------------------------------------- #

# Prompt user to enter the password securely
$password_match = $false
while (-not $password_match) {
    $my_password = Read-Host "Enter Password" -AsSecureString
    $confirm_password = Read-Host "Confirm Password" -AsSecureString
    
    if ([Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToBSTR($my_password)) -eq [Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToBSTR($confirm_password))) {
        $password_match = $true
    } else {
        [System.Windows.Forms.MessageBox]::Show("Passwords do not match. Please try again.", "Error", [System.Windows.Forms.MessageBoxButtons]::OK, [System.Windows.Forms.MessageBoxIcon]::Error)
    }
}

# Convert secure string to plain text for use with ssh-keygen and 7z
$plain_password = [Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToBSTR($my_password))

# -------------------------------------------------------------------------- #

# Ensure ~/.ssh directory exists
$ssh_dir = "$HOME\.ssh"
if (-not (Test-Path -Path $ssh_dir)) {
    New-Item -ItemType Directory -Path $ssh_dir -Force | Out-Null
}

# Define SSH key paths
$sshkey_path_dsa = "$ssh_dir\id_dsa-$today"
$sshkey_path_ecdsa = "$ssh_dir\id_ecdsa-$today"
$sshkey_path_ed25519 = "$ssh_dir\id_ed25519-$today"
$sshkey_path_rsa = "$ssh_dir\id_rsa-$today"

# Generate SSH keys with today's date suffix and use the password if required
ssh-keygen -t dsa -C "$today - $email_address" -f $sshkey_path_dsa -N $plain_password
ssh-keygen -t ecdsa -b 521 -C "$today - $email_address" -f $sshkey_path_ecdsa -N $plain_password
ssh-keygen -t ed25519 -C "$today - $email_address" -f $sshkey_path_ed25519 -N $plain_password
ssh-keygen -t rsa -b 4096 -C "$today - $email_address" -f $sshkey_path_rsa -N $plain_password

# -------------------------------------------------------------------------- #

# Define the filepaths for the zip files
$zip_filepath = Join-Path -Path $ssh_keys_folder -ChildPath "ssh_keys_$today.zip"
$encrypted_zip_filepath = Join-Path -Path $ssh_keys_folder -ChildPath "encrypted_ssh_keys_$today.zip"
$decrypted_zip_filepath = Join-Path -Path $ssh_keys_folder -ChildPath "decrypted_ssh_keys_$today.zip"

# Create a zip file of the private keys
Compress-Archive -Path $sshkey_path_dsa, $sshkey_path_ecdsa, $sshkey_path_ed25519, $sshkey_path_rsa -DestinationPath $zip_filepath

# Check if zip command was successful
if ($LASTEXITCODE -ne 0) {
    [System.Windows.Forms.MessageBox]::Show("Failed to create zip file. Exiting.", "Error", [System.Windows.Forms.MessageBoxButtons]::OK, [System.Windows.Forms.MessageBoxIcon]::Error)
    exit 1
}

# Encrypt the zip file with strong encryption using 7-Zip
& 7z a -tzip -p$plain_password $encrypted_zip_filepath $zip_filepath

# Check if encryption was successful
if ($LASTEXITCODE -ne 0) {
    [System.Windows.Forms.MessageBox]::Show("Failed to encrypt zip file. Exiting.", "Error", [System.Windows.Forms.MessageBoxButtons]::OK, [System.Windows.Forms.MessageBoxIcon]::Error)
    exit 1
}

# -------------------------------------------------------------------------- #

# Copy public keys generated today to the chosen folder
Copy-Item -Path "$sshkey_path_dsa.pub" -Destination $ssh_keys_folder
Copy-Item -Path "$sshkey_path_ecdsa.pub" -Destination $ssh_keys_folder
Copy-Item -Path "$sshkey_path_ed25519.pub" -Destination $ssh_keys_folder
Copy-Item -Path "$sshkey_path_rsa.pub" -Destination $ssh_keys_folder

# -------------------------------------------------------------------------- #

# Define the decryption file
$decryption_script = Join-Path -Path $ssh_keys_folder -ChildPath "decrypt.ps1"

# Remove the previous decryption script if it exists
Remove-Item -Path $decryption_script -Force -ErrorAction SilentlyContinue

# Generate the decryption script
@"
# Decrypt.ps1

# Prompt user for password
\$my_password = Read-Host "Enter Password" -AsSecureString

# Check if password is provided
if (-not \$my_password) {
    [System.Windows.Forms.MessageBox]::Show("Password cannot be empty. Exiting.", "Error", [System.Windows.Forms.MessageBoxButtons]::OK, [System.Windows.Forms.MessageBoxIcon]::Error)
    exit 1
}

# Convert secure string to plain text
\$plain_password = [Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToBSTR(\$my_password))

# Decrypt the encrypted file using 7-Zip
& 7z x -p\$plain_password -o"$ssh_keys_folder" "$encrypted_zip_filepath"

# Check if decryption was successful
if (\$LASTEXITCODE -ne 0) {
    [System.Windows.Forms.MessageBox]::Show("Failed to decrypt zip file. Exiting.", "Error", [System.Windows.Forms.MessageBoxButtons]::OK, [System.Windows.Forms.MessageBoxIcon]::Error)
    exit 1
}

# Securely clear the password variable from memory
\$plain_password = \$null
[System.Runtime.InteropServices.Marshal]::ZeroFreeBSTR([System.Runtime.InteropServices.Marshal]::SecureStringToBSTR(\$my_password))

# Inform the user that decryption was successful
[System.Windows.Forms.MessageBox]::Show("Decryption successful.", "Info", [System.Windows.Forms.MessageBoxButtons]::OK, [System.Windows.Forms.MessageBoxIcon]::Information)
"@ | Set-Content -Path $decryption_script

# -------------------------------------------------------------------------- #

# Define the extraction script
$extraction_script = Join-Path -Path $ssh_keys_folder -ChildPath "extract.ps1"

# Remove the previous extraction script if it exists
Remove-Item -Path $extraction_script -Force -ErrorAction SilentlyContinue

# Generate the extraction script
@"
# Extract.ps1

# Extract the ssh keys from the zip file
Expand-Archive -Path "$decrypted_zip_filepath" -DestinationPath "$ssh_keys_folder"

# Check if extraction was successful
if (\$LASTEXITCODE -ne 0) {
    [System.Windows.Forms.MessageBox]::Show("Failed to extract zip file. Exiting.", "Error", [System.Windows.Forms.MessageBoxButtons]::OK, [System.Windows.Forms.MessageBoxIcon]::Error)
    exit 1
}

# Remove the zip file
Remove-Item -Path "$decrypted_zip_filepath" -Force

# Inform the user that extraction was successful
[System.Windows.Forms.MessageBox]::Show("Extraction successful.", "Info", [System.Windows.Forms.MessageBoxButtons]::OK, [System.Windows.Forms.MessageBoxIcon]::Information)
"@ | Set-Content -Path $extraction_script

# -------------------------------------------------------------------------- #

# Remove the zip file after encryption
Remove-Item -Path $zip_filepath -Force

# -------------------------------------------------------------------------- #

# Securely clear the password variable from memory
$plain_password = $null
[System.Runtime.InteropServices.Marshal]::ZeroFreeBSTR([System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($my_password))

# -------------------------------------------------------------------------- #

# Prompt user to add SSH keys to SSH agent
$add_keys = [System.Windows.Forms.MessageBox]::Show("SSH keys generated and encrypted. Do you want to add them to the SSH agent?", "Add SSH Keys", [System.Windows.Forms.MessageBoxButtons]::YesNo, [System.Windows.Forms.MessageBoxIcon]::Question)

# If user chooses to add SSH keys to SSH agent
if ($add_keys -eq [System.Windows.Forms.DialogResult]::Yes) {
    ssh-add $sshkey_path_dsa $sshkey_path_ecdsa $sshkey_path_ed25519 $sshkey_path_rsa
    [System.Windows.Forms.MessageBox]::Show("SSH keys added to SSH agent.", "Info", [System.Windows.Forms.MessageBoxButtons]::OK, [System.Windows.Forms.MessageBoxIcon]::Information)
}

# -------------------------------------------------------------------------- #

[System.Windows.Forms.MessageBox]::Show("Script finished.", "Info", [System.Windows.Forms.MessageBoxButtons]::OK, [System.Windows.Forms.MessageBoxIcon]::Information)

# ========================================================================== #
# C2 A9 32 30 32 34 2D 4D 41 4E 2D 4D 41 44 45 2D 4D 45 4B 41 4E 59 5A 4D 53 #
# ========================================================================== #

# Changelist:

# -------------------------------------------------------------------------- #
# version:               1.0.0
# modified:              2024-03-10 - 10:20:24
# comments:              Initial commit
# -------------------------------------------------------------------------- #
# version:               2.0.0
# modified:              2024-10-15 - 10:47:35
# comments:              Added decrypt/extract scripts for all 3 major OSes.
# -------------------------------------------------------------------------- #
# version:               3.0.0
# modified:              2024-11-25 - 09:34:35
# comments:              Split monolithic script into OS specific versions
# -------------------------------------------------------------------------- #
