import os
import platform
import socket
import grp
# import re
import pwd
import subprocess
import sys
from typing import List, Dict, Any


# Independent Functions
def get_current_user() -> Dict[str, Any]:
    """Get current user information."""
    user_info = {}

    try:
        # Basic user info
        user_info['username'] = (
            os.getlogin()
        )
    except:
        user_info['username'] = (
            os.environ.get(
                'USER',
                os.environ.get(
                    'USERNAME',
                    'unknown'
                )
            )
        )

    try:
        # Get user ID
        user_info['uid'] = os.getuid()
        user_info['gid'] = os.getgid()
        user_info['effective_uid'] = os.geteuid()
        user_info['effective_gid'] = os.getegid()

        # Get detailed user info from passwd
        pwd_entry = pwd.getpwuid(os.getuid())
        user_info['real_name'] = pwd_entry.pw_gecos
        user_info['home_directory'] = pwd_entry.pw_dir
        user_info['shell'] = pwd_entry.pw_shell

    except Exception as e:
        user_info['error'] = str(e)

    return user_info


def get_fqdn() -> str:
    """Get the Fully Qualified Domain Name."""
    try:
        return socket.getfqdn()
    except Exception as e:
        return f"Error getting FQDN: {e}"


def get_hostnames() -> Dict[str, Any]:
    """Get various hostname information."""
    hostnames = {}
    try:
        hostnames['hostname'] = socket.gethostname()
        hostnames['fqdn'] = socket.getfqdn()
      
        # Try to get aliases from /etc/hosts or DNS
        try:
            hostname_info = socket.gethostbyname_ex(socket.gethostname())
            hostnames['aliases'] = hostname_info[1] if hostname_info[1] else []
        except:
            hostnames['aliases'] = []
          
    except Exception as e:
        hostnames['error'] = str(e)
  
    return hostnames


def get_ipv4_addresses() -> List[str]:
    """Get all IPv4 addresses for this host."""
    addresses = []
    try:
        # Get hostname and resolve to IP
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        addresses.append(local_ip)
      
        # Try to get external IP by connecting to a remote server
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                s.connect(("8.8.8.8", 80))
                external_ip = s.getsockname()[0]
                if external_ip not in addresses:
                    addresses.append(external_ip)
        except:
            pass
          
        # Get all network interfaces (requires netifaces or similar)
        try:
            import netifaces
            for interface in netifaces.interfaces():
                if netifaces.AF_INET in netifaces.ifaddresses(interface):
                    for addr_info in netifaces.ifaddresses(interface)[netifaces.AF_INET]:
                        ip = addr_info['addr']
                        if ip not in addresses:
                            addresses.append(ip)
        except ImportError:
            # Fallback method using subprocess
            try:
                if platform.system() == "Linux":
                    result = subprocess.run(
                        ['hostname', '-I'],
                        capture_output=True,
                        text=True
                    )
                    if result.returncode == 0:
                        ips = result.stdout.strip().split()
                        for ip in ips:
                            if ip not in addresses:
                                addresses.append(ip)
            except:
                pass
              
    except Exception as e:
        addresses.append(f"Error getting IP: {e}")
  
    return addresses


def get_os_info() -> Dict[str, Any]:
    """Get detailed operating system information."""
    os_info = {}
  
    # Basic OS info
    os_info['system'] = platform.system()
    os_info['node'] = platform.node()
    os_info['release'] = platform.release()
    os_info['version'] = platform.version()
    os_info['machine'] = platform.machine()
    os_info['processor'] = platform.processor()
    os_info['architecture'] = platform.architecture()
    os_info['platform'] = platform.platform()
  
    # Detailed OS info
    try:
        os_info['python_version'] = platform.python_version()
        os_info['python_implementation'] = platform.python_implementation()
    except:
        pass
  
    # Linux-specific information
    if platform.system() == "Linux":
        try:
            # Try to get distribution info
            import distro
            os_info['distribution'] = {
                'id': distro.id(),
                'name': distro.name(),
                'version': distro.version(),
                'codename': distro.codename(),
                'like': distro.like()
            }
        except ImportError:
            # Fallback methods
            try:
                with open('/etc/os-release', 'r') as f:
                    os_release = {}
                    for line in f:
                        if '=' in line:
                            key, value = line.strip().split('=', 1)
                            os_release[key] = value.strip('"')
                    os_info['os_release'] = os_release
            except:
                pass
              
            try:
                with open('/etc/issue', 'r') as f:
                    os_info['issue'] = f.read().strip()
            except:
                pass
      
        # Kernel information
        try:
            os_info['kernel_version'] = platform.uname().release
            result = subprocess.run(
                ['uname', '-a'],
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                os_info['uname_all'] = result.stdout.strip()
        except:
            pass
  
    # Windows-specific information
    elif platform.system() == "Windows":
        try:
            os_info['windows_edition'] = platform.win32_edition()
            os_info['windows_version'] = platform.win32_ver()
        except:
            pass
  
    # macOS-specific information
    elif platform.system() == "Darwin":
        try:
            os_info['mac_version'] = platform.mac_ver()
        except:
            pass
  
    return os_info


def get_group_memberships() -> Dict[str, Any]:
    """Get user's group memberships."""
    group_info = {}
  
    try:
        # Get primary group
        primary_gid = os.getgid()
        primary_group = grp.getgrgid(primary_gid)
        group_info['primary_group'] = {
            'name': primary_group.gr_name,
            'gid': primary_group.gr_gid
        }
      
        # Get all groups
        username = pwd.getpwuid(os.getuid()).pw_name
        groups = []
      
        # Get all groups the user belongs to
        for group in grp.getgrall():
            if username in group.gr_mem or group.gr_gid == primary_gid:
                groups.append({
                    'name': group.gr_name,
                    'gid': group.gr_gid
                })
      
        group_info['all_groups'] = sorted(groups, key=lambda x: x['name'])
        group_info['group_count'] = len(groups)
      
        # Alternative method using os.getgroups()
        try:
            group_ids = os.getgroups()
            group_names = []
            for gid in group_ids:
                try:
                    group_names.append(grp.getgrgid(gid).gr_name)
                except KeyError:
                    group_names.append(f"gid:{gid}")
            group_info['groups_by_id'] = group_names
        except:
            pass
          
    except Exception as e:
        group_info['error'] = str(e)
  
    return group_info


# Dependent Functions (Level 1)
def get_primary_group() -> str:
    """Returns the current user's primary group name using
    get_group_memberships."""
    group_info = get_group_memberships()
    if 'primary_group' in group_info and 'name' in group_info['primary_group']:
        return group_info['primary_group']['name']
    return "(unknown_group - could not retrieve primary group)"


def get_short_hostname() -> str:
    """Returns the short hostname of the machine using get_hostnames."""
    hostnames = get_hostnames()
    return hostnames.get('hostname', '').split('.')[0]


def get_os_name() -> str:
    """Returns the operating system name using get_os_info."""
    os_info = get_os_info()
    return os_info.get('system', 'unknown')


# Dependent Functions (Level 2)
def print_system_info():
    """Print all system information in a formatted way."""
    print("=" * 60)
    print("SYSTEM INFORMATION REPORT")
    print("=" * 60)
  
    # Network Information
    print("\n🌐 NETWORK INFORMATION")
    print("-" * 30)
    hostnames = get_hostnames()
    print(f"FQDN: {get_fqdn()}")
    print(f"Hostname: {hostnames.get('hostname', 'N/A')}")
    if hostnames.get('aliases'):
        print(f"Aliases: {', '.join(hostnames['aliases'])}")
  
    ipv4_addresses = get_ipv4_addresses()
    print(f"IPv4 Addresses: {', '.join(ipv4_addresses)}")
  
    # Operating System Information
    print("\n💻 OPERATING SYSTEM")
    print("-" * 30)
    os_info = get_os_info()
    print(f"System: {os_info.get('system', 'N/A')}")
    print(f"Platform: {os_info.get('platform', 'N/A')}")
    print(f"Release: {os_info.get('release', 'N/A')}")
    print(f"Version: {os_info.get('version', 'N/A')}")
    print(f"Machine: {os_info.get('machine', 'N/A')}")
    print(f"Processor: {os_info.get('processor', 'N/A')}")
    print(f"Architecture: {' '.join(os_info.get('architecture', ['N/A']))}")
  
    if 'distribution' in os_info:
        dist = os_info['distribution']
        print(
            f"Distribution: {dist.get('name', 'N/A')} {dist.get('version', '')}"
        )
        if dist.get('codename'):
            print(f"Codename: {dist['codename']}")
  
    if 'kernel_version' in os_info:
        print(f"Kernel: {os_info['kernel_version']}")
  
    # User Information
    print("\n👤 USER INFORMATION")
    print("-" * 30)
    user_info = get_current_user()
    print(f"Username: {user_info.get('username', 'N/A')}")
    print(f"User ID (UID): {user_info.get('uid', 'N/A')}")
    print(f"Group ID (GID): {user_info.get('gid', 'N/A')}")
    print(f"Real Name: {user_info.get('real_name', 'N/A')}")
    print(f"Home Directory: {user_info.get('home_directory', 'N/A')}")
    print(f"Shell: {user_info.get('shell', 'N/A')}")
  
    # Group Information
    print("\n👥 GROUP MEMBERSHIPS")
    print("-" * 30)
    group_info = get_group_memberships()
  
    if 'primary_group' in group_info:
        pg = group_info['primary_group']
        print(f"Primary Group: {pg['name']} (GID: {pg['gid']})")
  
    if 'all_groups' in group_info:
        print(f"Total Groups: {group_info.get('group_count', 0)}")
        print("All Group Memberships:")
        for group in group_info['all_groups']:
            print(f"  • {group['name']} (GID: {group['gid']})")


# Main Execution Block
def main():
    """Main function to run the system information gatherer."""
    try:
        print_system_info()
    except KeyboardInterrupt:
        print("\n\nScript interrupted by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()


# -------------------------------------------------------------------------- #

# DISCLAIMER:   This file is part of LOGIK-PROJEKT.

#               Copyright © 2025 STRENGTH IN NUMBERS

#               LOGIK-PROJEKT creates directories, files, scripts & tools
#               for use with Autodesk Flame and other software.

#               LOGIK-PROJEKT is free software.

#               You can redistribute it and/or modify it under the terms
#               of the GNU General Public License as published by the
#               Free Software Foundation, either version 3 of the License,
#               or any later version.

#               This program is distributed in the hope that it will be
#               useful, but WITHOUT ANY WARRANTY; without even the
#               implied warranty of MERCHANTABILITY or
#               FITNESS FOR A PARTICULAR PURPOSE.

#               See the GNU General Public License for more details.
#               You should have received a copy of the GNU General
#               Public License along with this program.

#               If not, see <https://www.gnu.org/licenses/gpl-3.0.en.html>.

#               Contact: phil_man@mac.com

# -------------------------------------------------------------------------- #
# C2 A9 32 30 32 35 53 54 52 45 4E 47 54 48 2D 49 4E 2D 4E 55 4D 42 45 52 53 #
# -------------------------------------------------------------------------- #
# Changelog:
# -------------------------------------------------------------------------- #
