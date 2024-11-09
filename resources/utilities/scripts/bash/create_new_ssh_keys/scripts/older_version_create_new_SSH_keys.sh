#!/bin/bash

# -------------------------------------------------------------------------- #

# Program Name:     create_new_ssh_keys.sh
# Version:          2.0.0
# Language:         bash script
# Flame Version:    2025.x
# Author:           Phil MAN - phil_man@mac.com
# Toolset:          MAN_MADE_MATERIAL
# Created:          2024-03-12
# Modified:         2024-10-15
# Modifier:         Phil MAN - phil_man@mac.com

# Changelist:       Added function to create/read 'project_setup_template'.

# -------------------------------------------------------------------------- #

# Description:      This program will generate SSH keys and prompt the user
#                   to create an encrypted backup tar file.

# Installation:     Copy the 'FLAME-DEPLOYMENT' repo to your home directory,

# -------------------------------------------------------------------------- #

# ========================================================================== #
# C2 A9 2D 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 5F 4D 41 54 45 52 49 61 4C #
# ========================================================================== #

# ========================================================================== #
# This section sets variables and gathers user information.
# ========================================================================== #

# -------------------------------------------------------------------------- #

# Define today's date in 'YYYY-MM-DD' format
today=$(date +'%Y-%m-%d')
# today="$(date +'%Y-%m-%d')-TEST8"

# -------------------------------------------------------------------------- #

# Prompt user to choose a folder using Zenity
chosen_folder=$(zenity --file-selection \
    --directory \
    --title="Choose Folder to Save New SSH Keys")

# Check if user cancelled the folder selection
if [ $? -ne 0 ]; then
    zenity --error --text="Operation cancelled. Exiting."
    exit 1
fi

# Create an enclosing folder
ssh_keys_folder="$chosen_folder/ssh_keys-$today"
mkdir -p $ssh_keys_folder

# -------------------------------------------------------------------------- #

# Define the filename for the ssh_key_creation_log
ssh_key_creation_log="$ssh_keys_folder/$today-ssh_key_creation_log"

# Create ssh_key_creation_log in $ssh_keys_folder and redirect stdout and stderr to it
touch "$ssh_key_creation_log"

# Redirect stdout and stderr to ssh_key_creation_log
exec &> "$ssh_key_creation_log"

# -------------------------------------------------------------------------- #

# Prompt user to enter their email address
email_address=$(zenity --entry \
    --title="Generate SSH Keys" \
    --text="You are about to generate new SSH keys. \n
Enter your email address:")

# Check if user cancelled the prompt
if [ $? -ne 0 ]; then
    zenity --error --text="Operation cancelled. Exiting."
    exit 1
fi

# Check if email address is provided
if [ -z "$email_address" ]; then
    zenity --error --text="Email address cannot be empty. Exiting."
    exit 1
fi

# -------------------------------------------------------------------------- #

# Prompt user to enter the password securely
password_match=0
while [ "$password_match" -eq 0 ]; do
    my_password=$(zenity --password \
        --title="Enter Password" \
        --width=600)
    
    confirm_password=$(zenity --password \
        --title="Confirm Password" \
        --width=600)
    
    if [ "$my_password" = "$confirm_password" ]; then
        password_match=1
    else
        zenity --error --text="Passwords do not match. Please try again."
    fi
done

# -------------------------------------------------------------------------- #

# Ensure ~/.ssh directory exists
mkdir -p ~/.ssh

# Define SSH key paths
sshkey_path_dsa="~/.ssh/id_dsa-$today"
sshkey_path_ecdsa="~/.ssh/id_ecdsa-$today"
sshkey_path_ed25519="~/.ssh/id_ed25519-$today"
sshkey_path_rsa="~/.ssh/id_rsa-$today"

# Define SSH key names
sshkey_dsa="id_dsa-$today"
sshkey_ecdsa="id_ecdsa-$today"
sshkey_ed25519="id_ed25519-$today"
sshkey_rsa="id_rsa-$today"

# Generate SSH keys with today's date suffix and use the password if required
ssh-keygen -t dsa -C "$today - $email_address" \
           -f ~/.ssh/id_dsa-$today -N "$my_password"

ssh-keygen -t ecdsa -b 521 -C "$today - $email_address" \
           -f ~/.ssh/id_ecdsa-$today -N "$my_password"

ssh-keygen -t ed25519 -C "$today - $email_address" \
           -f ~/.ssh/id_ed25519-$today -N "$my_password"

ssh-keygen -t rsa -b 4096 -C "$today - $email_address" \
           -f ~/.ssh/id_rsa-$today -N "$my_password"

# -------------------------------------------------------------------------- #

# Define the filepaths for the tar files
tar_filepath="$ssh_keys_folder/ssh_keys_$today.tar"
encrypted_tar_filepath="$ssh_keys_folder/encrypted_ssh_keys_$today.tar.enc"
decrypted_tar_filepath="$ssh_keys_folder/decrypted_ssh_keys_$today.tar"

# Define the filenames for the tar files
encrypted_tar_file="$(basename "$encrypted_tar_filepath")"
decrypted_tar_file="$(basename "$decrypted_tar_filepath")"

# -------------------------------------------------------------------------- #

# Create a tar file of the private keys
tar -cvf "$tar_filepath" \
    ~/.ssh/id_*-$today

# Check if tar command was successful
if [ $? -ne 0 ]; then
    zenity --error --text="Failed to create tar file. Exiting."
    exit 1
fi

# Encrypt the tar file with strong encryption
openssl aes-256-cbc -salt \
    -pbkdf2 \
    -in "$tar_filepath" \
    -out "$encrypted_tar_filepath" \
    -k "$my_password"

# Check if encryption was successful
if [ $? -ne 0 ]; then
    zenity --error --text="Failed to encrypt tar file. Exiting."
    exit 1
fi

# -------------------------------------------------------------------------- #

# Copy public keys generated today to the chosen folder
cp ~/.ssh/id_*-$today.pub "$ssh_keys_folder/"

# -------------------------------------------------------------------------- #

# Define the decryption file
decryption_script="$ssh_keys_folder/decrypt.sh"

# Remove the previous decryption script if it exists
rm -f "$decryption_script"

# -------------------------------------------------------------------------- #

# Generate the decryption script
echo '#!/bin/bash' > "$decryption_script"

echo '' >> "$decryption_script"

echo '' >> "$decryption_script"

echo '# Prompt user for password' >> "$decryption_script"

echo 'my_password=$(zenity --password \' >> "$decryption_script"

echo '    --title="Enter Password" \' >> "$decryption_script"

echo '    --width=600)' >> "$decryption_script"

echo '' >> "$decryption_script"

# -------------------------------------------------------------------------- #

echo '# Check if password is provided' >> "$decryption_script"

echo 'if [ -z "$my_password" ]; then' >> "$decryption_script"

echo '    zenity --error --text="Password cannot be empty. \nExiting."' \
        >> "$decryption_script"

echo '    exit 1' >> "$decryption_script"

echo 'fi' >> "$decryption_script"

echo '' >> "$decryption_script"

# -------------------------------------------------------------------------- #

echo '# Decrypt the encrypted file' >> "$decryption_script"

echo 'openssl aes-256-cbc -d \' >> "$decryption_script"

echo '    -pbkdf2 \' >> "$decryption_script"

echo "    -in \"$encrypted_tar_file\" \\" >> "$decryption_script"

echo "    -out \"$decrypted_tar_file\" \\" >> "$decryption_script"

echo '    -k "$my_password"' >> "$decryption_script"

echo '' >> "$decryption_script"

# -------------------------------------------------------------------------- #

# echo '# Check if decryption was successful' >> "$decryption_script"

# echo 'if [ $? -eq 0 ]; then' >> "$decryption_script"

# echo "    zenity --info --text=\"Decrypted file: \"$decrypted_tar_file\"\"" \
#     >> "$decryption_script"

# echo 'else' >> "$decryption_script"

# echo '    zenity --error --text="Decryption failed." \' >> "$decryption_script"

# echo 'fi' >> "$decryption_script"

# echo '' >> "$decryption_script"

# -------------------------------------------------------------------------- #

# echo '# Extract the ssh keys from the tar file' >> "$decryption_script"

# echo "tar -xvf \"$decrypted_tar_file\"" >> "$decryption_script"

# echo '# Remove the tar file' >> "$decryption_script"

# echo "rm -v \"$decrypted_tar_file\"" >> "$decryption_script"

# -------------------------------------------------------------------------- #

# Make the decryption script executable
chmod +x "$decryption_script"

# -------------------------------------------------------------------------- #

# Define the extraction script
extraction_script="$ssh_keys_folder/extract.sh"

# Remove the previous extraction script if it exists
rm -f "$extraction_script"

# -------------------------------------------------------------------------- #

# Generate the extraction script
echo '#!/bin/bash' > "$extraction_script"

echo '' >> "$extraction_script"

echo '' >> "$extraction_script"

echo '# Extract the ssh keys from the tar file' >> "$extraction_script"

echo "tar -xvf \"$decrypted_tar_file\"" >> "$extraction_script"

echo '# Remove the tar file' >> "$extraction_script"

echo "rm -v \"$decrypted_tar_file\"" >> "$extraction_script"

# -------------------------------------------------------------------------- #

# Make the extraction script executable
chmod +x "$extraction_script"

# -------------------------------------------------------------------------- #

# Remove the tar file after encryption
rm "$ssh_keys_folder/ssh_keys_$today.tar"

# -------------------------------------------------------------------------- #

# Securely clear the password variable from memory
unset my_password

# -------------------------------------------------------------------------- #

# Prompt user to add SSH keys to SSH agent
zenity --question --text="SSH keys generated and encrypted. \n
Do you want to add them to the SSH agent?"

# If user chooses to add SSH keys to SSH agent
if [ $? -eq 0 ]; then
    ssh-add ~/.ssh/id_*-$today
    zenity --info --text="SSH keys added to SSH agent."
fi

# -------------------------------------------------------------------------- #

zenity --info --text="Script finished."

# ========================================================================== #
# C2 A9 2D 32 30 32 34 2D 4D 41 4E 5F 4D 41 44 45 5F 4D 41 54 45 52 49 61 4C #
# ========================================================================== #
# version:               2.0.0
# modified:              2024-10-15 - 10:47:35
# comments:              Added decrypt and extract scripts for all 3 major OSes.
# -------------------------------------------------------------------------- #
