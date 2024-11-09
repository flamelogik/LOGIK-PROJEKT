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

# Changelist:       Modified for macOS compatibility

# -------------------------------------------------------------------------- #

# Description:      This program will generate SSH keys and create an encrypted backup tar file.

# Installation:     Copy the script to your desired location and make it executable with chmod +x.

# -------------------------------------------------------------------------- #

# ========================================================================== #
# C2 A9 2D 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 5F 4D 41 54 45 52 49 61 4C #
# ========================================================================== #

# Define today's date in 'YYYY-MM-DD' format
today=$(date +'%Y-%m-%d')

# Prompt user to choose a folder using AppleScript
chosen_folder=$(osascript -e 'tell application "Finder" to set folderPath to choose folder with prompt "Choose Folder to Save New SSH Keys"' -e 'POSIX path of folderPath')

# Check if user cancelled the folder selection
if [ -z "$chosen_folder" ]; then
    osascript -e 'display alert "Operation cancelled" message "Exiting." as critical'
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
email_address=$(osascript -e 'text returned of (display dialog "You are about to generate new SSH keys.\n\nEnter your email address:" default answer "")')

# Check if user cancelled the prompt or if email is empty
if [ -z "$email_address" ]; then
    osascript -e 'display alert "Error" message "Email address cannot be empty. Exiting." as critical'
    exit 1
fi

# Prompt user to enter the password securely
password_match=0
while [ "$password_match" -eq 0 ]; do
    my_password=$(osascript -e 'text returned of (display dialog "Enter Password:" default answer "" with hidden answer)')
    confirm_password=$(osascript -e 'text returned of (display dialog "Confirm Password:" default answer "" with hidden answer)')
    
    if [ "$my_password" = "$confirm_password" ]; then
        password_match=1
    else
        osascript -e 'display alert "Error" message "Passwords do not match. Please try again." as critical'
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
    osascript -e 'display alert "Error" message "Failed to create tar file. Exiting." as critical'
    exit 1
fi

# Encrypt the tar file with strong encryption (modified for macOS OpenSSL)
openssl enc -aes-256-cbc -salt -in "$tar_filepath" -out "$encrypted_tar_filepath" -k "$my_password"

# Check if encryption was successful
if [ $? -ne 0 ]; then
    osascript -e 'display alert "Error" message "Failed to encrypt tar file. Exiting." as critical'
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

# Prompt user for password
my_password=\$(osascript -e 'text returned of (display dialog "Enter Password:" default answer "" with hidden answer)')

# Check if password is provided
if [ -z "\$my_password" ]; then
    osascript -e 'display alert "Error" message "Password cannot be empty. Exiting." as critical'
    exit 1
fi

# Decrypt the encrypted file
openssl enc -d -aes-256-cbc -in "$encrypted_tar_file" -out "$decrypted_tar_file" -k "\$my_password"

# Check if decryption was successful
if [ \$? -eq 0 ]; then
    osascript -e 'display alert "Success" message "Decrypted file: $decrypted_tar_file"'
else
    osascript -e 'display alert "Error" message "Decryption failed." as critical'
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
add_to_agent=$(osascript -e 'button returned of (display dialog "SSH keys generated and encrypted. Do you want to add them to the SSH agent?" buttons {"Yes", "No"} default button "Yes")')

# If user chooses to add SSH keys to SSH agent
if [ "$add_to_agent" = "Yes" ]; then
    ssh-add ~/.ssh/id_*-$today
    osascript -e 'display alert "Success" message "SSH keys added to SSH agent."'
fi

osascript -e 'display alert "Finished" message "Script finished."'

# ========================================================================== #
# C2 A9 2D 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 5F 4D 41 54 45 52 49 61 4C #
# ========================================================================== ## version:               2.0.0
# modified:              2024-10-15 - 10:47:35
# comments:              Added decrypt and extract scripts for all 3 major OSes.
# -------------------------------------------------------------------------- #
