#!/bin/bash

# -------------------------------------------------------------------------- #

# Program Name:     create_ssh_keys-linux.sh
# Version:          3.0.0
# Author:           Phil MAN - phil_man@mac.com
# Created:          2024-03-12
# Modified:         2024-11-25

# Changelist:       Added function to create/read 'project_setup_template'.

# Description:      This program will generate SSH keys and prompt the user
#                   to create an encrypted backup tar file.

# ========================================================================== #
# This section sets variables and gathers user information.
# ========================================================================== #

# -------------------------------------------------------------------------- #

# Define today's date in 'YYYY_MM_DD-HH_MM_SS' format
today=$(date +'%Y_%m_%d-%H_%M_%S')

# -------------------------------------------------------------------------- #

# # Check if required commands are available
# for cmd in zenity openssl ssh-keygen tar chmod; do
#     if ! command -v "$cmd" &> /dev/null; then
#         echo "Error: $cmd is not installed. Exiting."
#         exit 1
#     fi
# done

validate_commands() {
  local required_cmds=("$@")
  for cmd in "${required_cmds[@]}"; do
    if ! command -v "$cmd" &> /dev/null; then
      zenity --error --text="Critical error: $cmd is not installed."
      exit 1
    fi
  done
}
validate_commands "zenity" "openssl" "ssh-keygen" "tar" "chmod"

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
mkdir -p "$ssh_keys_folder"

# -------------------------------------------------------------------------- #

# Define the filename for the ssh_key_creation_log
ssh_key_creation_log="$ssh_keys_folder/$today-ssh_key_creation_log"

# Create ssh_key_creation_log in $ssh_keys_folder and redirect stdout and stderr to it
touch "$ssh_key_creation_log"

# Redirect stdout and stderr to ssh_key_creation_log
exec &> "$ssh_key_creation_log"

# -------------------------------------------------------------------------- #

# # Prompt user to enter their email address
# email_address=$(zenity --entry \
#     --title="Generate SSH Keys" \
#     --text="You are about to generate new SSH keys. \nEnter your email address:")

# # Check if user cancelled the prompt
# if [ $? -ne 0 ]; then
#     zenity --error --text="Operation cancelled. Exiting."
#     exit 1
# fi

# # Check if email address is provided
# if [ -z "$email_address" ]; then
#     zenity --error --text="Email address cannot be empty. Exiting."
#     exit 1
# fi

validate_email() {
    local email="$1"
    local email_regex="^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$"
    if [[ ! "$email" =~ $email_regex ]]; then
        zenity --error --text="Invalid email format. Please try again."
        return 1
    fi
}

email_address=$(zenity --entry \
    --title="Generate SSH Keys" \
    --text="You are about to generate new SSH keys. \nEnter your email address:")

if [ $? -ne 0 ]; then
    zenity --error --text="Operation cancelled. Exiting."
    exit 1
fi

validate_email "$email_address" || exit 1

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
sshkey_path_dsa="$HOME/.ssh/id_dsa-$today"
sshkey_path_ecdsa="$HOME/.ssh/id_ecdsa-$today"
sshkey_path_ed25519="$HOME/.ssh/id_ed25519-$today"
sshkey_path_rsa="$HOME/.ssh/id_rsa-$today"

# Generate SSH keys with today's date suffix and use the password if required
ssh-keygen -t dsa -C "$today - $email_address" -f "$sshkey_path_dsa" -N "$my_password"
ssh-keygen -t ecdsa -b 521 -C "$today - $email_address" -f "$sshkey_path_ecdsa" -N "$my_password"
ssh-keygen -t ed25519 -C "$today - $email_address" -f "$sshkey_path_ed25519" -N "$my_password"
ssh-keygen -t rsa -b 4096 -C "$today - $email_address" -f "$sshkey_path_rsa" -N "$my_password"

# -------------------------------------------------------------------------- #

# Define the filepaths for the tar files
tar_filepath="$ssh_keys_folder/ssh_keys_$today.tar"
encrypted_tar_filename="encrypted_ssh_keys_$today.tar.enc"
encrypted_tar_filepath="$ssh_keys_folder/$encrypted_tar_filename"
decrypted_tar_filename="decrypted_ssh_keys_$today.tar"
decrypted_tar_filepath="$ssh_keys_folder/$decrypted_tar_filename"

# Create a tar file of the private keys
tar -cvf "$tar_filepath" "$sshkey_path_dsa" "$sshkey_path_ecdsa" "$sshkey_path_ed25519" "$sshkey_path_rsa"

# Check if tar command was successful
if [ $? -ne 0 ]; then
    zenity --error --text="Failed to create tar file. Exiting."
    exit 1
fi

# Encrypt the tar file with strong encryption
openssl aes-256-cbc -salt -pbkdf2 -in "$tar_filepath" -out "$encrypted_tar_filepath" -k "$my_password"

# Check if encryption was successful
if [ $? -ne 0 ]; then
    zenity --error --text="Failed to encrypt tar file. Exiting."
    exit 1
fi

# -------------------------------------------------------------------------- #

# Copy public keys generated today to the chosen folder
cp "$sshkey_path_dsa.pub" "$sshkey_path_ecdsa.pub" "$sshkey_path_ed25519.pub" "$sshkey_path_rsa.pub" "$ssh_keys_folder/"

# -------------------------------------------------------------------------- #

# Define the decryption file
decryption_script="$ssh_keys_folder/decrypt.sh"

# Remove the previous decryption script if it exists
rm -f "$decryption_script"

# Generate the decryption script
cat <<EOF > "$decryption_script"
#!/bin/bash

# Change to the directory of the running script
path_to_here="\$(cd "\$(dirname "\${BASH_SOURCE[0]}")" && pwd)" cd "\$path_to_here" || exit

# Prompt user for password
my_password=\$(zenity --password --title="Enter Password" --width=600)

# Check if password is provided
if [ -z "\$my_password" ]; then
    zenity --error --text="Password cannot be empty. \nExiting."
    exit 1
fi

# Decrypt the encrypted file
# openssl aes-256-cbc -d -pbkdf2 -in "$encrypted_tar_filepath" -out "$decrypted_tar_filepath" -k "\$my_password"
openssl aes-256-cbc -d -pbkdf2 -in "$encrypted_tar_filename" -out "$decrypted_tar_filename" -k "\$my_password"

EOF

# Make the decryption script executable
chmod +x "$decryption_script"

# -------------------------------------------------------------------------- #

# Define the extraction script
extraction_script="$ssh_keys_folder/extract.sh"

# Remove the previous extraction script if it exists
rm -f "$extraction_script"

# Generate the extraction script
cat <<EOF > "$extraction_script"
#!/bin/bash

# Change to the directory of the running script
path_to_here="\$(cd "\$(dirname "\${BASH_SOURCE[0]}")" && pwd)" cd "\$path_to_here" || exit

# Extract the ssh keys from the tar file
tar -xvf "$decrypted_tar_filename"

# Remove the tar file
rm -v "$decrypted_tar_filename"
EOF

# Make the extraction script executable
chmod +x "$extraction_script"

# -------------------------------------------------------------------------- #

# Remove the tar file after encryption
rm "$tar_filepath"

# -------------------------------------------------------------------------- #

# Securely clear the password variable from memory
unset my_password

# -------------------------------------------------------------------------- #

# Prompt user to add SSH keys to SSH agent
zenity --question --text="SSH keys generated and encrypted. \nDo you want to add them to the SSH agent?"

# If user chooses to add SSH keys to SSH agent
if [ $? -eq 0 ]; then
    ssh-add "$sshkey_path_dsa" "$sshkey_path_ecdsa" "$sshkey_path_ed25519" "$sshkey_path_rsa"
    zenity --info --text="SSH keys added to SSH agent."
fi

# -------------------------------------------------------------------------- #

zenity --info --text="Script finished."

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
