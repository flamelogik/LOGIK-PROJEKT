#!/usr/bin/env python3
# create-ssh-keys.py
# Cross-platform script to generate SSH keys and create an encrypted backup.

import os
import sys
import re
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import platform
import datetime
import tarfile
import shutil
import secrets
import string
import tempfile
import threading
from pathlib import Path


class SSHKeyGenerator:
    def __init__(self):
        """Initialize the SSH Key Generator application."""
        # System information
        self.operating_system = platform.system()
        self.timestamp = datetime.datetime.now().strftime('%Y_%m_%d-%H_%M_%S')

        # Paths
        self.home_dir = str(Path.home())
        self.ssh_dir = os.path.join(self.home_dir, ".ssh")

        # Initialize tk
        self.root = tk.Tk()
        self.root.withdraw()  # Hide the main window
        self.root.title("SSH Key Generator")

        # Sensitive data
        self.email_address = None
        self.password = None

        # File paths
        self.chosen_folder = None
        self.ssh_keys_folder = None
        self.tar_filepath = None
        self.encrypted_tar_filepath = None

    def log_activity(self, message, sensitive=False):
        """Log activity to the log file, with option to mask sensitive data."""
        if hasattr(self, 'log_file') and self.log_file:
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            if sensitive:
                # Mask sensitive data
                message = re.sub(r'password=\S+', 'password=XXXXX', message)
 
            with open(self.log_file, 'a') as f:
                f.write(f"{timestamp}: {message}\n")

    def check_dependencies(self):
        """Check if required dependencies are installed."""
        required_tools = ["ssh-keygen", "openssl"]
        missing = []

        for tool in required_tools:
            try:
                # Use 'where' on Windows, 'which' on Unix-like systems
                if self.operating_system == "Windows":
                    subprocess.run(["where", tool], check=True,
                                  stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                else:
                    subprocess.run(["which", tool], check=True,
                                  stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            except subprocess.SubprocessError:
                missing.append(tool)

        if missing:
            missing_tools = ", ".join(missing)
            messagebox.showerror(
                "Missing Dependencies",
                f"Missing required dependencies: {missing_tools}\n\n"
                f"Please install them before running this script."
            )
            sys.exit(1)

        return True

    def secure_delete(self, file_path):
        """Securely delete a file by overwriting with random data."""
        if not os.path.exists(file_path):
            return
 
        try:
            # Get file size
            file_size = os.path.getsize(file_path)
 
            # Open the file for writing in binary mode
            with open(file_path, 'wb') as f:
                # Overwrite with random data 3 times
                for _ in range(3):
                    f.seek(0)
                    # Write random bytes
                    f.write(os.urandom(file_size))
                    f.flush()
                    os.fsync(f.fileno())
 
            # Finally remove the file
            os.remove(file_path)
            self.log_activity(f"Securely deleted: {file_path}")
        except Exception as e:
            self.log_activity(f"Error during secure delete: {str(e)}")
            # Fallback to regular delete
            try:
                os.remove(file_path)
            except:
                pass

    def validate_email(self, email):
        """Validate email format with comprehensive regex."""
        email_regex = r'^[a-zA-Z0-9]([-._a-zA-Z0-9]*[a-zA-Z0-9])*@[a-zA-Z0-9]([-._a-zA-Z0-9]*[a-zA-Z0-9])*\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, email):
            messagebox.showerror(
                "Invalid Email",
                "Invalid email format. Please ensure:\n"
                "- No special characters except . - _\n"
                "- Valid domain format\n"
                "- At least 2 character domain extension"
            )
            return False
        return True

    def validate_password_strength(self, password):
        """Validate password strength."""
        minimum_length = 12

        if len(password) < minimum_length:
            messagebox.showerror(
                "Weak Password",
                f"Password must be at least {minimum_length} characters long"
            )
            return False
 
        if (not re.search(r'[A-Z]', password) or
            not re.search(r'[a-z]', password) or
            not re.search(r'[0-9]', password) or
            not re.search(r'[^A-Za-z0-9]', password)):
 
            messagebox.showerror(
                "Weak Password",
                "Password must contain:\n"
                "- Uppercase letters\n"
                "- Lowercase letters\n"
                "- Numbers\n"
                "- Special characters"
            )
            return False

        return True

    def get_email_address(self):
        """Get and validate email address from user."""
        while True:
            email = simpledialog.askstring(
                "Generate SSH Keys",
                "Enter your email address:",
                parent=self.root
            )
 
            if email is None:  # User cancelled
                messagebox.showerror(
                    "Operation Cancelled",
                    "Operation cancelled. Exiting."
                )
                sys.exit(1)
     
            if self.validate_email(email):
                self.email_address = email
                self.log_activity(f"Email address provided: {email}")
                break

    def get_password(self):
        """Get and validate password from user."""
        password_match = False

        while not password_match:
            password = simpledialog.askstring(
                "Enter Password",
                "Enter Password (min 12 chars, mixed case, numbers, symbols):",
                show='*',
                parent=self.root
            )
 
            if password is None:  # User cancelled
                messagebox.showerror(
                    "Operation Cancelled",
                    "Operation cancelled. Exiting."
                )
                sys.exit(1)
     
            if not self.validate_password_strength(password):
                continue
     
            confirm_password = simpledialog.askstring(
                "Confirm Password",
                "Confirm Password:",
                show='*',
                parent=self.root
            )
 
            if password == confirm_password:
                password_match = True
                self.password = password
                self.log_activity("Password provided and confirmed", sensitive=True)
            else:
                messagebox.showerror(
                    "Password Mismatch",
                    "Passwords do not match. Please try again."
                )

    def choose_output_folder(self):
        """Prompt user to choose an output folder."""
        initial_dir = os.path.join(self.home_dir, "Documents")

        # Make sure the initial directory exists
        os.makedirs(initial_dir, exist_ok=True)

        self.chosen_folder = filedialog.askdirectory(
            title="Choose Folder to Save New SSH Keys",
            initialdir=initial_dir
        )

        if not self.chosen_folder:  # User cancelled
            messagebox.showerror(
                "Operation Cancelled",
                "Operation cancelled. Exiting."
            )
            sys.exit(1)
 
        # Create the output folder
        self.ssh_keys_folder = os.path.join(self.chosen_folder, f"ssh_keys-{self.timestamp}")
        os.makedirs(self.ssh_keys_folder, exist_ok=True)

        # Set proper permissions (on Unix-like systems)
        if self.operating_system != "Windows":
            os.chmod(self.ssh_keys_folder, 0o700)
 
        # Setup logging
        self.log_file = os.path.join(self.ssh_keys_folder, f"{self.timestamp}-ssh_key_creation_log.txt")

        # Create log file with header
        with open(self.log_file, 'w') as f:
            f.write(f"SSH Key Generation Log - {self.timestamp}\n")
            f.write(f"{'=' * 60}\n")
            f.write(f"Operating System: {self.operating_system}\n")
            f.write(f"Python Version: {sys.version}\n")
            f.write(f"Output Directory: {self.ssh_keys_folder}\n")
            f.write(f"{'=' * 60}\n\n")
 
            # Also capture the script execution command and arguments
            f.write("COMMAND:\n")
            f.write(f"{sys.executable} {' '.join(sys.argv)}\n\n")

        # Set proper permissions for log file (on Unix-like systems)
        if self.operating_system != "Windows":
            os.chmod(self.log_file, 0o600)
 
        # Create a tee process to capture all stdout/stderr and send to file and console
        class Tee:
            def __init__(self, log_file):
                self.log_file = open(log_file, "a")
                self.stdout = sys.stdout
                self.stderr = sys.stderr
     
            def write(self, message):
                self.log_file.write(message)
                self.stdout.write(message)
                self.log_file.flush()
     
            def flush(self):
                self.log_file.flush()
                self.stdout.flush()
     
            def close(self):
                if self.log_file:
                    self.log_file.close()

        # Create the tee for stdout
        self.tee = Tee(self.log_file)
        sys.stdout = self.tee
        sys.stderr = self.tee

        self.log_activity(f"Output folder selected: {self.ssh_keys_folder}")

    def ensure_ssh_directory(self):
        """Ensure ~/.ssh directory exists with proper permissions."""
        os.makedirs(self.ssh_dir, exist_ok=True)

        # Set proper permissions (on Unix-like systems)
        if self.operating_system != "Windows":
            os.chmod(self.ssh_dir, 0o700)
 
        self.log_activity(f"SSH directory ensured: {self.ssh_dir}")

    def generate_ssh_keys(self):
        """Generate SSH keys with enhanced security parameters."""
        # Define SSH key paths
        self.sshkey_path_ed25519 = os.path.join(self.ssh_dir, f"id_ed25519-{self.timestamp}")
        self.sshkey_path_rsa = os.path.join(self.ssh_dir, f"id_rsa-{self.timestamp}")

        # Create temp files for password input
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(f"{self.password}\n{self.password}")
            password_file = temp_file.name

        try:
            # Generate ED25519 key
            self.log_activity("Generating ED25519 key...")
            ed25519_result = subprocess.run([
                "ssh-keygen",
                "-t", "ed25519",
                "-a", "100",
                "-C", f"{self.timestamp} - {self.email_address}",
                "-f", self.sshkey_path_ed25519,
                "-N", self.password
            ], capture_output=True, text=True, check=True)
 
            # Log the full output
            with open(self.log_file, 'a') as f:
                f.write(f"\n{'=' * 60}\n")
                f.write("ED25519 KEY GENERATION\n")
                f.write(f"{'=' * 60}\n")
                f.write(ed25519_result.stdout)
                if ed25519_result.stderr:
                    f.write(ed25519_result.stderr)
                f.write(f"\n{'=' * 60}\n")
 
            # Print to console as well
            print(ed25519_result.stdout)
 
            # Generate RSA key
            self.log_activity("Generating RSA key...")
            rsa_result = subprocess.run([
                "ssh-keygen",
                "-t", "rsa",
                "-b", "4096",
                "-E", "sha512",
                "-a", "100",
                "-C", f"{self.timestamp} - {self.email_address}",
                "-f", self.sshkey_path_rsa,
                "-N", self.password
            ], capture_output=True, text=True, check=True)
 
            # Log the full output
            with open(self.log_file, 'a') as f:
                f.write(f"\n{'=' * 60}\n")
                f.write("RSA KEY GENERATION\n")
                f.write(f"{'=' * 60}\n")
                f.write(rsa_result.stdout)
                if rsa_result.stderr:
                    f.write(rsa_result.stderr)
                f.write(f"\n{'=' * 60}\n")
 
            # Print to console as well
            print(rsa_result.stdout)
 
            # Set proper permissions for keys (on Unix-like systems)
            if self.operating_system != "Windows":
                os.chmod(self.sshkey_path_ed25519, 0o600)
                os.chmod(f"{self.sshkey_path_ed25519}.pub", 0o644)
                os.chmod(self.sshkey_path_rsa, 0o600)
                os.chmod(f"{self.sshkey_path_rsa}.pub", 0o644)
     
            self.log_activity("SSH keys generated successfully")
 
        except subprocess.SubprocessError as e:
            self.log_activity(f"Error generating SSH keys: {str(e)}")
            messagebox.showerror(
                "Key Generation Error",
                f"Failed to generate SSH keys: {str(e)}"
            )
            sys.exit(1)
        finally:
            # Securely delete the temporary password file
            self.secure_delete(password_file)

    def create_encrypted_backup(self):
        """Create a tar file of the private keys and encrypt it."""
        # Define the filepaths for the tar files
        self.tar_filepath = os.path.join(self.ssh_keys_folder, f"ssh_keys_{self.timestamp}.tar")
        self.encrypted_tar_filename = f"encrypted_ssh_keys_{self.timestamp}.tar.enc"
        self.encrypted_tar_filepath = os.path.join(self.ssh_keys_folder, self.encrypted_tar_filename)

        try:
            # Create tar file
            with tarfile.open(self.tar_filepath, "w") as tar:
                tar.add(self.sshkey_path_ed25519, arcname=os.path.basename(self.sshkey_path_ed25519))
                tar.add(self.sshkey_path_rsa, arcname=os.path.basename(self.sshkey_path_rsa))
 
            self.log_activity(f"Created tar archive: {self.tar_filepath}")
 
            # Create temp file for password input
            with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
                temp_file.write(self.password)
                password_file = temp_file.name
 
            # Encrypt the tar file
            encryption_result = subprocess.run([
                "openssl", "enc", "-aes-256-cbc", "-pbkdf2", "-iter", "100000", "-salt",
                "-in", self.tar_filepath,
                "-out", self.encrypted_tar_filepath,
                "-pass", f"file:{password_file}"
            ], capture_output=True, text=True, check=True)
 
            # Log the encryption output
            with open(self.log_file, 'a') as f:
                f.write(f"\n{'=' * 60}\n")
                f.write("ENCRYPTION PROCESS\n")
                f.write(f"{'=' * 60}\n")
                f.write(f"Encrypting {self.tar_filepath} to {self.encrypted_tar_filepath}\n")
                if encryption_result.stdout:
                    f.write(encryption_result.stdout)
                if encryption_result.stderr:
                    f.write(encryption_result.stderr)
                f.write(f"\n{'=' * 60}\n")
 
            self.log_activity(f"Created encrypted archive: {self.encrypted_tar_filepath}")
 
            # Verify encryption was successful
            if not os.path.isfile(self.encrypted_tar_filepath):
                messagebox.showerror(
                    "Encryption Error",
                    "Failed to create encrypted backup. Exiting."
                )
                sys.exit(1)
     
        except Exception as e:
            self.log_activity(f"Error creating encrypted backup: {str(e)}")
            messagebox.showerror(
                "Backup Error",
                f"Failed to create encrypted backup: {str(e)}"
            )
            sys.exit(1)
        finally:
            # Securely delete the temporary password file
            self.secure_delete(password_file)
 
            # Copy public keys to the chosen folder
            shutil.copy2(f"{self.sshkey_path_ed25519}.pub", self.ssh_keys_folder)
            shutil.copy2(f"{self.sshkey_path_rsa}.pub", self.ssh_keys_folder)
 
            # Securely delete the unencrypted tar file
            self.secure_delete(self.tar_filepath)

    def create_decrypt_script(self):
        """Generate a decrypt script for the encrypted backup."""
        decrypt_script_path = os.path.join(self.ssh_keys_folder, "decrypt.py")

        script_content = """#!/usr/bin/env python3
import os
import sys
import subprocess
import datetime
import tkinter as tk
from tkinter import simpledialog, messagebox

# Initialize tkinter
root = tk.Tk()
root.withdraw()

# Get the directory of the running script
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Get the encrypted file path
encrypted_files = [f for f in os.listdir('.') if f.startswith('encrypted_ssh_keys_') and f.endswith('.tar.enc')]
if not encrypted_files:
    messagebox.showerror("Error", "No encrypted SSH key file found.")
    sys.exit(1)

encrypted_file = encrypted_files[0]
timestamp = datetime.datetime.now().strftime('%Y_%m_%d-%H_%M_%S')
decrypted_file = f"decrypted_ssh_keys_{timestamp}.tar"

# Prompt for password
password = simpledialog.askstring("Enter Password", "Enter Password:", show='*', parent=root)
if not password:
    messagebox.showerror("Error", "Password cannot be empty. Exiting.")
    sys.exit(1)

try:
    # Create a temporary file for the password
    import tempfile
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write(password)
        password_file = temp_file.name

    # Decrypt the file
    subprocess.run([
        "openssl", "enc", "-d", "-aes-256-cbc", "-pbkdf2", "-iter", "100000", "-salt",
        "-in", encrypted_file,
        "-out", decrypted_file,
        "-pass", f"file:{password_file}"
    ], check=True)

    messagebox.showinfo("Success", f"File decrypted successfully as {decrypted_file}")

except Exception as e:
    messagebox.showerror("Error", f"Decryption failed: {str(e)}")

finally:
    # Securely delete the password file
    if 'password_file' in locals():
        # Overwrite with random data
        with open(password_file, 'wb') as f:
            f.write(os.urandom(1024))
        # Remove the file
        os.remove(password_file)

    # Unset password variable
    password = None
"""

        with open(decrypt_script_path, 'w') as f:
            f.write(script_content)
 
        # Make the script executable (on Unix-like systems)
        if self.operating_system != "Windows":
            os.chmod(decrypt_script_path, 0o700)
 
        self.log_activity("Created decrypt script")

    def create_extract_script(self):
        """Generate an extract script for the decrypted tar file."""
        extract_script_path = os.path.join(self.ssh_keys_folder, "extract.py")

        script_content = """#!/usr/bin/env python3
import os
import sys
import tarfile
import tkinter as tk
from tkinter import messagebox

# Initialize tkinter
root = tk.Tk()
root.withdraw()

# Get the directory of the running script
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Get the decrypted file path
decrypted_files = [f for f in os.listdir('.') if f.startswith('decrypted_ssh_keys_') and f.endswith('.tar')]
if not decrypted_files:
    messagebox.showerror("Error", "No decrypted SSH key file found. Run decrypt.py first.")
    sys.exit(1)

decrypted_file = decrypted_files[0]

try:
    # Extract the tar file
    with tarfile.open(decrypted_file, 'r') as tar:
        tar.extractall('.')

    # Securely delete the decrypted tar file
    def secure_delete(file_path):
        # Get file size
        file_size = os.path.getsize(file_path)

        # Open the file for writing in binary mode
        with open(file_path, 'wb') as f:
            # Overwrite with random data 3 times
            for _ in range(3):
                f.seek(0)
                # Write random bytes
                f.write(os.urandom(file_size))
                f.flush()
                os.fsync(f.fileno())

        # Finally remove the file
        os.remove(file_path)

    # Delete the tar file securely
    secure_delete(decrypted_file)

    # Get the extracted key files
    ssh_key_files = [f for f in os.listdir('.') if (f.startswith('id_ed25519-') or f.startswith('id_rsa-')) and not f.endswith('.pub')]

    messagebox.showinfo("Success", "SSH keys extracted successfully. The following keys were extracted:\\n" + "\\n".join(ssh_key_files))

except Exception as e:
    messagebox.showerror("Error", f"Extraction failed: {str(e)}")
"""

        with open(extract_script_path, 'w') as f:
            f.write(script_content)
 
        # Make the script executable (on Unix-like systems)
        if self.operating_system != "Windows":
            os.chmod(extract_script_path, 0o700)
 
        self.log_activity("Created extract script")

    def add_keys_to_agent(self):
        """Ask user if they want to add the keys to the SSH agent."""
        if messagebox.askyesno(
            "Add to SSH Agent",
            "SSH keys generated and encrypted.\nDo you want to add them to the SSH agent?"
        ):
            try:
                # Check if ssh-agent is running
                if self.operating_system == "Windows":
                    # Check if ssh-agent service is running on Windows
                    check_agent = subprocess.run(
                        ["sc", "query", "ssh-agent"],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE
                    )
                    agent_running = "RUNNING" in check_agent.stdout.decode()
                else:
                    # Check if ssh-agent is running on Unix-like systems
                    check_agent = subprocess.run(
                        ["ps", "-p", os.environ.get("SSH_AGENT_PID", ""), "-o", "comm="],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE
                    )
                    agent_running = "ssh-agent" in check_agent.stdout.decode()
     
                if not agent_running:
                    messagebox.showwarning(
                        "SSH Agent Not Running",
                        "SSH agent does not appear to be running.\n"
                        "Please start the SSH agent before adding keys."
                    )
                    return
     
                # Add keys to SSH agent
                ed25519_add_result = subprocess.run(
                    ["ssh-add", self.sshkey_path_ed25519],
                    capture_output=True,
                    text=True,
                    check=True
                )
                rsa_add_result = subprocess.run(
                    ["ssh-add", self.sshkey_path_rsa],
                    capture_output=True,
                    text=True,
                    check=True
                )
     
                # Log the output
                with open(self.log_file, 'a') as f:
                    f.write(f"\n{'=' * 60}\n")
                    f.write("ADDING KEYS TO SSH AGENT\n")
                    f.write(f"{'=' * 60}\n")
                    f.write("Adding ED25519 key:\n")
                    f.write(ed25519_add_result.stdout)
                    if ed25519_add_result.stderr:
                        f.write(ed25519_add_result.stderr)
                    f.write("\nAdding RSA key:\n")
                    f.write(rsa_add_result.stdout)
                    if rsa_add_result.stderr:
                        f.write(rsa_add_result.stderr)
                    f.write(f"\n{'=' * 60}\n")
     
                # Print to console
                print(ed25519_add_result.stdout)
                print(rsa_add_result.stdout)
     
                messagebox.showinfo(
                    "Keys Added",
                    "SSH keys successfully added to SSH agent."
                )
                self.log_activity("SSH keys added to agent")
     
            except subprocess.SubprocessError as e:
                messagebox.showwarning(
                    "SSH Agent Error",
                    f"Failed to add SSH keys to SSH agent.\n"
                    f"Error: {str(e)}\n"
                    f"You can add them manually later using ssh-add."
                )
                self.log_activity(f"Error adding keys to agent: {str(e)}")
        else:
            messagebox.showinfo(
                "Information",
                "SSH keys were not added to SSH agent.\n"
                "You can add them manually later using ssh-add."
            )
            self.log_activity("User chose not to add keys to agent")

    def cleanup(self):
        """Clean up sensitive information."""
        # Clear sensitive variables
        self.password = None

        # Restore stdout and stderr if they were redirected
        if hasattr(self, 'tee'):
            sys.stdout = sys.__stdout__
            sys.stderr = sys.__stderr__
            self.tee.close()

        # Close Tkinter root window
        self.root.destroy()

    def run(self):
        """Run the full process."""
        try:
            # Check dependencies
            self.check_dependencies()
 
            # Step 1: Choose output folder
            self.choose_output_folder()
 
            # Step 2: Get email address
            self.get_email_address()
 
            # Step 3: Get password
            self.get_password()
 
            # Step 4: Ensure SSH directory exists
            self.ensure_ssh_directory()
 
            # Step 5: Generate SSH keys
            self.generate_ssh_keys()
 
            # Step 6: Create encrypted backup
            self.create_encrypted_backup()
 
            # Step 7: Create helper scripts
            self.create_decrypt_script()
            self.create_extract_script()
 
            # Step 8: Ask to add keys to SSH agent
            self.add_keys_to_agent()
 
            # Final success message
            messagebox.showinfo(
                "Success",
                f"Script finished successfully.\n\n"
                f"Keys were generated in: {self.ssh_keys_folder}\n\n"
                f"Encrypted backup created: {self.encrypted_tar_filename}\n\n"
                f"Use decrypt.py and extract.py scripts to restore keys when needed."
            )
 
        except Exception as e:
            self.log_activity(f"Unhandled error: {str(e)}")
            messagebox.showerror(
                "Error",
                f"An unexpected error occurred: {str(e)}"
            )
        finally:
            # Final cleanup
            self.cleanup()


if __name__ == "__main__":
    generator = SSHKeyGenerator()
    generator.run()

# -------------------------------------------------------------------------- #
# 53 54 52 45 4E 47 54 48 2D 49 4E 2D 4E 55 4D 42 45 52 53 C2 A9 32 30 32 35 #
# -------------------------------------------------------------------------- #
# Changelist:
# -------------------------------------------------------------------------- #
# version:               1.0.0
# modified:              2025-05-20 - 10:30:00
# comments:              Initial Python conversion from bash script
# -------------------------------------------------------------------------- #