#!/bin/bash

# -------------------------------------------------------------------------- #

# Program Name:     create_new_ssh_keys.sh
# Version:          2.0.0
# Language:         bash script
# Flame Version:    2025.x
# Author:           Phil MAN - phil_man@mac.com
# Modified by:      Assistant
# Toolset:          MAN_MADE_MEKANYZMS: LOGIK-PROJEKT
# Created:          2024-03-12
# Modified:         2024-10-15

# -------------------------------------------------------------------------- #

# Description:      This program creates SSH keys, an encrypted backup file,
#                   and generates decryption and extraction scripts.

# Installation:     Copy the script to your desired location.
#                   Make it executable with chmod +x.

# Changelist:       The full changelist is at the end of this document.

# -------------------------------------------------------------------------- #

# Detect the operating system
if [[ "$OSTYPE" == "darwin"* ]]; then
    OS="macOS"
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    OS="Linux"
else
    echo "Unsupported operating system"
    exit 1
fi

# -------------------------------------------------------------------------- #

# Function to show dialog boxes
show_dialog() {
    if [ "$OS" = "macOS" ]; then
        osascript -e "display dialog \"$1\" default answer \"$2\" buttons {\"OK\", \"Cancel\"} default button \"OK\"" -e "text returned of result"
    elif [ "$OS" = "Linux" ]; then
        zenity --entry --title="$3" --text="$1" --entry-text="$2"
    fi
}

# -------------------------------------------------------------------------- #

# Function to show alerts
show_alert() {
    if [ "$OS" = "macOS" ]; then
        osascript -e "display alert \"$1\" message \"$2\""
    elif [ "$OS" = "Linux" ]; then
        zenity --info --title="$1" --text="$2"
    fi
}

# -------------------------------------------------------------------------- #

# Function to show error messages
show_error() {
    if [ "$OS" = "macOS" ]; then
        osascript -e "display alert \"Error\" message \"$1\" as critical"
    elif [ "$OS" = "Linux" ]; then
        zenity --error --text="$1"
    fi
}

# -------------------------------------------------------------------------- #

# Function to prompt for folder selection
choose_folder() {
    if [ "$OS" = "macOS" ]; then
        osascript -e 'tell application "Finder" to set folderPath to choose folder with prompt "Choose Folder to Save New SSH Keys"' -e 'POSIX path of folderPath'
    elif [ "$OS" = "Linux" ]; then
        zenity --file-selection --directory --title="Choose Folder to Save New SSH Keys"
    fi
}

# -------------------------------------------------------------------------- #

# Define today's date in 'YYYY-MM-DD' format
today=$(date +'%Y-%m-%d')

# -------------------------------------------------------------------------- #

# Prompt user to choose a folder
chosen_folder=$(choose_folder)

# Check if user cancelled the folder selection
if [ -z "$chosen_folder" ]; then
    show_error "Operation cancelled. Exiting."
    exit 1
fi

# Create an enclosing folder
ssh_keys_folder="$chosen_folder/ssh_keys-$today"
mkdir -p "$ssh_keys_folder"

# -------------------------------------------------------------------------- #

# Define the filename for the ssh_key_creation_log
ssh_key_creation_log="$ssh_keys_folder/$today-ssh_key_creation_log"

# Create ssh_key_creation_log in $ssh_keys_folder and redirect stdout and stderr to it
touch "$ssh_key_creation_log"
exec &> "$ssh_key_creation_log"

# Prompt user to enter their email address
email_address=$(show_dialog "You are about to generate new SSH keys.\n\nEnter your email address:" "" "Generate SSH Keys")

# Check if user cancelled the prompt or if email is empty
if [ -z "$email_address" ]; then
    show_error "Email address cannot be empty. Exiting."
    exit 1
fi

# -------------------------------------------------------------------------- #

# Prompt user to enter the password securely
password_match=0
while [ "$password_match" -eq 0 ]; do
    my_password=$(show_dialog "Enter Password:" "" "Enter Password")
    confirm_password=$(show_dialog "Confirm Password:" "" "Confirm Password")
    
    if [ "$my_password" = "$confirm_password" ]; then
        password_match=1
    else
        show_error "Passwords do not match. Please try again."
    fi
done

# -------------------------------------------------------------------------- #

# Ensure ~/.ssh directory exists
mkdir -p ~/.ssh

# Define SSH key paths
sshkey_path_ecdsa="~/.ssh/id_ecdsa-$today"
sshkey_path_ed25519="~/.ssh/id_ed25519-$today"
sshkey_path_rsa="~/.ssh/id_rsa-$today"

# Generate SSH keys with today's date suffix and use the password if required
ssh-keygen -t ecdsa -b 521 -C "$today - $email_address" -f ~/.ssh/id_ecdsa-$today -N "$my_password"
ssh-keygen -t ed25519 -C "$today - $email_address" -f ~/.ssh/id_ed25519-$today -N "$my_password"
ssh-keygen -t rsa -b 4096 -C "$today - $email_address" -f ~/.ssh/id_rsa-$today -N "$my_password"

# -------------------------------------------------------------------------- #

# Define the filepaths for the tar files
tar_filepath="$ssh_keys_folder/ssh_keys_$today.tar"
encrypted_tar_filepath="$ssh_keys_folder/encrypted_ssh_keys_$today.tar.enc"
decrypted_tar_filepath="$ssh_keys_folder/decrypted_ssh_keys_$today.tar"

# Define the filenames for the tar files
encrypted_tar_file="$(basename "$encrypted_tar_filepath")"
decrypted_tar_file="$(basename "$decrypted_tar_filepath")"

# Create a tar file of the private keys
tar -cvf "$tar_filepath" ~/.ssh/id_*-$today

# Check if tar command was successful
if [ $? -ne 0 ]; then
    show_error "Failed to create tar file. Exiting."
    exit 1
fi

# -------------------------------------------------------------------------- #

# Encrypt the tar file with strong encryption
if [ "$OS" = "macOS" ]; then
    openssl enc -aes-256-cbc -salt -in "$tar_filepath" -out "$encrypted_tar_filepath" -k "$my_password"
elif [ "$OS" = "Linux" ]; then
    openssl enc -aes-256-cbc -salt -pbkdf2 -in "$tar_filepath" -out "$encrypted_tar_filepath" -k "$my_password"
fi

# Check if encryption was successful
if [ $? -ne 0 ]; then
    show_error "Failed to encrypt tar file. Exiting."
    exit 1
fi

# -------------------------------------------------------------------------- #

# Copy public keys generated today to the chosen folder
cp ~/.ssh/id_*-$today.pub "$ssh_keys_folder/"

# -------------------------------------------------------------------------- #

# Create decrypt_linux.sh
cat << EOF > "$ssh_keys_folder/decrypt_linux.sh"
#!/bin/bash

# Get the directory of this script
path_to_here="$(dirname "$0")"

# Change directory to path_to_here
cd "$path_to_here" || exit

# Prompt for password
password=\$(zenity --password --title="Enter Decryption Password")

# Decrypt the file
openssl enc -d -aes-256-cbc -pbkdf2 -in "$encrypted_tar_file" -out "$decrypted_tar_file" -k "\$password"

# Check if decryption was successful
if [ \$? -eq 0 ]; then
    zenity --info --text="Decryption successful. Decrypted file: $decrypted_tar_file"
else
    zenity --error --text="Decryption failed."
fi
EOF

# -------------------------------------------------------------------------- #

# Create decrypt_macos.sh
cat << EOF > "$ssh_keys_folder/decrypt_macos.sh"
#!/bin/bash

# Get the directory of this script
path_to_here="$(dirname "$0")"

# Change directory to path_to_here
cd "$path_to_here" || exit

# Prompt for password
password=\$(osascript -e 'text returned of (display dialog "Enter Decryption Password:" default answer "" with hidden answer)')

# Decrypt the file
openssl enc -d -aes-256-cbc -in "$encrypted_tar_file" -out "$decrypted_tar_file" -k "\$password"

# Check if decryption was successful
if [ \$? -eq 0 ]; then
    osascript -e 'display alert "Success" message "Decryption successful. Decrypted file: $decrypted_tar_file"'
else
    osascript -e 'display alert "Error" message "Decryption failed." as critical'
fi
EOF

# -------------------------------------------------------------------------- #

# Create decrypt_windows.ps1
cat << EOF > "$ssh_keys_folder/decrypt_windows.ps1"
# Get the directory of this script
\$path_to_here = Split-Path -Parent \$MyInvocation.MyCommand.Definition

# Change directory to path_to_here
Set-Location -Path \$path_to_here

# Prompt for password
\$password = Read-Host "Enter Decryption Password" -AsSecureString
\$password = [Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToBSTR(\$password))

# Decrypt the file
\$encryptedFile = "$encrypted_tar_file"
\$decryptedFile = "$decrypted_tar_file"

try {
    \$key = [System.Text.Encoding]::UTF8.GetBytes(\$password)
    \$content = Get-Content \$encryptedFile -Raw -AsByteStream
    \$decrypted = [System.Security.Cryptography.AesManaged]::Create().CreateDecryptor(\$key[0..31], \$key[0..15]).TransformFinalBlock(\$content, 0, \$content.Length)
    [System.IO.File]::WriteAllBytes(\$decryptedFile, \$decrypted)
    [System.Windows.Forms.MessageBox]::Show("Decryption successful. Decrypted file: \$decryptedFile", "Success", [System.Windows.Forms.MessageBoxButtons]::OK, [System.Windows.Forms.MessageBoxIcon]::Information)
}
catch {
    [System.Windows.Forms.MessageBox]::Show("Decryption failed: \$_", "Error", [System.Windows.Forms.MessageBoxButtons]::OK, [System.Windows.Forms.MessageBoxIcon]::Error)
}
EOF

# -------------------------------------------------------------------------- #


# Create extract_linux.sh
cat << EOF > "$ssh_keys_folder/extract_linux.sh"
#!/bin/bash

# Get the directory of this script
path_to_here="$(dirname "$0")"

# Change directory to path_to_here
cd "$path_to_here" || exit

# Extract the ssh keys from the tar file
tar -xvf "$decrypted_tar_file"

# Remove the decrypted tar file
rm -v "$decrypted_tar_file"

zenity --info --text="Extraction complete. The decrypted tar file has been removed."
EOF

# -------------------------------------------------------------------------- #

# Create extract_macos.sh
cat << EOF > "$ssh_keys_folder/extract_macos.sh"
#!/bin/bash

# Get the directory of this script
path_to_here="$(dirname "$0")"

# Change directory to path_to_here
cd "$path_to_here" || exit

# Extract the ssh keys from the tar file
tar -xvf "$decrypted_tar_file"

# Remove the decrypted tar file
rm -v "$decrypted_tar_file"

osascript -e 'display alert "Extraction Complete" message "The decrypted tar file has been removed."'
EOF

# -------------------------------------------------------------------------- #

# Create extract_windows.ps1
cat << EOF > "$ssh_keys_folder/extract_windows.ps1"
# Get the directory of this script
\$path_to_here = Split-Path -Parent \$MyInvocation.MyCommand.Definition

# Change directory to path_to_here
Set-Location -Path \$path_to_here

# Extract the ssh keys from the tar file
\$decryptedFile = "$decrypted_tar_file"
\$extractPath = Split-Path \$decryptedFile -Parent

try {
    tar -xvf \$decryptedFile -C \$extractPath

    # Remove the decrypted tar file
    Remove-Item \$decryptedFile -Force

    [System.Windows.Forms.MessageBox]::Show("Extraction complete. The decrypted tar file has been removed.", "Success", [System.Windows.Forms.MessageBoxButtons]::OK, [System.Windows.Forms.MessageBoxIcon]::Information)
}
catch {
    [System.Windows.Forms.MessageBox]::Show("Extraction failed: \$_", "Error", [System.Windows.Forms.MessageBoxButtons]::OK, [System.Windows.Forms.MessageBoxIcon]::Error)
}
EOF

# -------------------------------------------------------------------------- #

# Make all scripts executable
chmod +x "$ssh_keys_folder"/*.sh

# -------------------------------------------------------------------------- #

# Remove the tar file after encryption
rm "$ssh_keys_folder/ssh_keys_$today.tar"

# -------------------------------------------------------------------------- #

# Securely clear the password variable from memory
unset my_password

# -------------------------------------------------------------------------- #

# Prompt user to add SSH keys to SSH agent
if [ "$OS" = "macOS" ]; then
    add_to_agent=$(osascript -e 'button returned of (display dialog "SSH keys generated and encrypted. Do you want to add them to the SSH agent?" buttons {"Yes", "No"} default button "Yes")')
elif [ "$OS" = "Linux" ]; then
    zenity --question --text="SSH keys generated and encrypted. Do you want to add them to the SSH agent?"
    add_to_agent=$?
fi

# -------------------------------------------------------------------------- #

# If user chooses to add SSH keys to SSH agent
if [ "$add_to_agent" = "Yes" ] || [ "$add_to_agent" -eq 0 ]; then
    ssh-add ~/.ssh/id_*-$today
    show_alert "Success" "SSH keys added to SSH agent."
fi

# -------------------------------------------------------------------------- #

show_alert "Finished" "Script finished. Decryption and extraction scripts have been created in $ssh_keys_folder for Linux, macOS, and Windows."

# ========================================================================== #
# C2 A9 32 30 32 34 2D 4D 41 4E 2D 4D 41 44 45 2D 4D 45 4B 41 4E 59 5A 4D 53 #
# ========================================================================== #
# version:               2.0.0
# modified:              2024-10-15 - 10:47:35
# comments:              Added decrypt and extract scripts for all 3 major OSes.
# -------------------------------------------------------------------------- #
