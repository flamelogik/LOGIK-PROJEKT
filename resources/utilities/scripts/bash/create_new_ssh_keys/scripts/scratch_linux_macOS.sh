#!/bin/bash

# -------------------------------------------------------------------------- #

# Program Name:     create_new_ssh_keys.sh
# Version:          2.0.0
# Language:         bash script
# Flame Version:    2025.x
# Author:           Phil MAN - phil_man@mac.com
# Modified by:      Assistant
# Toolset:          MAN_MADE_MATERIAL
# Created:          2024-03-12
# Modified:         2024-10-15

# Changelist:       Modified for cross-platform compatibility (Linux and macOS)

# -------------------------------------------------------------------------- #

# Description:      This program will generate SSH keys and create an encrypted backup tar file.

# Installation:     Copy the script to your desired location and make it executable with chmod +x.

# -------------------------------------------------------------------------- #

# ========================================================================== #
# C2 A9 2D 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 5F 4D 41 54 45 52 49 61 4C #
# ========================================================================== #

# Detect the operating system
if [[ "$OSTYPE" == "darwin"* ]]; then
    OS="macOS"
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    OS="Linux"
else
    echo "Unsupported operating system"
    exit 1
fi

# Function to show dialog boxes
show_dialog() {
    if [ "$OS" = "macOS" ]; then
        osascript -e "display dialog \"$1\" default answer \"$2\" buttons {\"OK\", \"Cancel\"} default button \"OK\"" -e "text returned of result"
    elif [ "$OS" = "Linux" ]; then
        zenity --entry --title="$3" --text="$1" --entry-text="$2"
    fi
}

# Function to show alerts
show_alert() {
    if [ "$OS" = "macOS" ]; then
        osascript -e "display alert \"$1\" message \"$2\""
    elif [ "$OS" = "Linux" ]; then
        zenity --info --title="$1" --text="$2"
    fi
}

# Function to show error messages
show_error() {
    if [ "$OS" = "macOS" ]; then
        osascript -e "display alert \"Error\" message \"$1\" as critical"
    elif [ "$OS" = "Linux" ]; then
        zenity --error --text="$1"
    fi
}

# Function to prompt for folder selection
choose_folder() {
    if [ "$OS" = "macOS" ]; then
        osascript -e 'tell application "Finder" to set folderPath to choose folder with prompt "Choose Folder to Save New SSH Keys"' -e 'POSIX path of folderPath'
    elif [ "$OS" = "Linux" ]; then
        zenity --file-selection --directory --title="Choose Folder to Save New SSH Keys"
    fi
}

# Define today's date in 'YYYY-MM-DD' format
today=$(date +'%Y-%m-%d')

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

# Copy public keys generated today to the chosen folder
cp ~/.ssh/id_*-$today.pub "$ssh_keys_folder/"

# Define the decryption script
decryption_script="$ssh_keys_folder/decrypt.sh"

# Remove the previous decryption script if it exists
rm -f "$decryption_script"

# Generate the decryption script
cat << EOF > "$decryption_script"
#!/bin/bash

# Detect the operating system
if [[ "\$OSTYPE" == "darwin"* ]]; then
    OS="macOS"
elif [[ "\$OSTYPE" == "linux-gnu"* ]]; then
    OS="Linux"
else
    echo "Unsupported operating system"
    exit 1
fi

# Function to show dialog boxes
show_dialog() {
    if [ "\$OS" = "macOS" ]; then
        osascript -e "display dialog \"\$1\" default answer \"\$2\" buttons {\"OK\", \"Cancel\"} default button \"OK\"" -e "text returned of result"
    elif [ "\$OS" = "Linux" ]; then
        zenity --entry --title="\$3" --text="\$1" --entry-text="\$2"
    fi
}

# Function to show alerts
show_alert() {
    if [ "\$OS" = "macOS" ]; then
        osascript -e "display alert \"\$1\" message \"\$2\""
    elif [ "\$OS" = "Linux" ]; then
        zenity --info --title="\$1" --text="\$2"
    fi
}

# Function to show error messages
show_error() {
    if [ "\$OS" = "macOS" ]; then
        osascript -e "display alert \"Error\" message \"\$1\" as critical"
    elif [ "\$OS" = "Linux" ]; then
        zenity --error --text="\$1"
    fi
}

# Prompt user for password
my_password=\$(show_dialog "Enter Password:" "" "Enter Password")

# Check if password is provided
if [ -z "\$my_password" ]; then
    show_error "Password cannot be empty. Exiting."
    exit 1
fi

# Decrypt the encrypted file
if [ "\$OS" = "macOS" ]; then
    openssl enc -d -aes-256-cbc -in "$encrypted_tar_file" -out "$decrypted_tar_file" -k "\$my_password"
elif [ "\$OS" = "Linux" ]; then
    openssl enc -d -aes-256-cbc -pbkdf2 -in "$encrypted_tar_file" -out "$decrypted_tar_file" -k "\$my_password"
fi

# Check if decryption was successful
if [ \$? -eq 0 ]; then
    show_alert "Success" "Decrypted file: $decrypted_tar_file"
else
    show_error "Decryption failed."
fi
EOF

# Make the decryption script executable
chmod +x "$decryption_script"

# Define the extraction script
extraction_script="$ssh_keys_folder/extract.sh"

# Remove the previous extraction script if it exists
rm -f "$extraction_script"

# Generate the extraction script
cat << EOF > "$extraction_script"
#!/bin/bash

# Extract the ssh keys from the tar file
tar -xvf "$decrypted_tar_file"

# Remove the tar file
rm -v "$decrypted_tar_file"
EOF

# Make the extraction script executable
chmod +x "$extraction_script"

# Remove the tar file after encryption
rm "$ssh_keys_folder/ssh_keys_$today.tar"

# Securely clear the password variable from memory
unset my_password

# Prompt user to add SSH keys to SSH agent
if [ "$OS" = "macOS" ]; then
    add_to_agent=$(osascript -e 'button returned of (display dialog "SSH keys generated and encrypted. Do you want to add them to the SSH agent?" buttons {"Yes", "No"} default button "Yes")')
elif [ "$OS" = "Linux" ]; then
    zenity --question --text="SSH keys generated and encrypted. Do you want to add them to the SSH agent?"
    add_to_agent=$?
fi

# If user chooses to add SSH keys to SSH agent
if [ "$add_to_agent" = "Yes" ] || [ "$add_to_agent" -eq 0 ]; then
    ssh-add ~/.ssh/id_*-$today
    show_alert "Success" "SSH keys added to SSH agent."
fi

show_alert "Finished" "Script finished."

# ========================================================================== #
# C2 A9 2D 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 5F 4D 41 54 45 52 49 61 4C #
# ========================================================================== ## version:               2.0.0
# modified:              2024-10-15 - 10:47:35
# comments:              Added decrypt and extract scripts for all 3 major OSes.
# -------------------------------------------------------------------------- #
