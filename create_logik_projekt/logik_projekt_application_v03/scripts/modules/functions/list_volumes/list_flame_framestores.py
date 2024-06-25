# import subprocess

# def list_framestores():
#     try:
#         # Execute wiretap_print_tree and capture its output
#         command = ["/opt/Autodesk/wiretap/tools/current/wiretap_print_tree", "-h", "127.0.0.1"]
#         output = subprocess.check_output(command, universal_newlines=True)

#         # Extract framestores using regex and remove the prefix
#         import re
#         framestores = [framestore.replace('/volumes/', '') for framestore in re.findall(r'/volumes/[^ ]*', output)]

#         return framestores
#     except subprocess.CalledProcessError:
#         return None

# # Example usage
# if __name__ == "__main__":
#     framestore_list = list_framestores()
#     if framestore_list:
#         for framestore in framestore_list:
#             print(framestore)
#     else:
#         print("Error executing wiretap_print_tree.")
















# import subprocess
# import re

# def list_framestores():
#     try:
#         # Execute wiretap_print_tree and capture its output
#         command = ["/opt/Autodesk/wiretap/tools/current/wiretap_print_tree", "-h", "127.0.0.1"]
#         output = subprocess.check_output(command, universal_newlines=True)

#         # Extract framestores using regex and remove the prefix
#         framestores = [re.sub(r'^/volumes/', '', framestore.strip()) for framestore in re.findall(r'/volumes/[^ ]*', output)]

#         return framestores
#     except subprocess.CalledProcessError:
#         return None

# # Example usage
# if __name__ == "__main__":
#     framestore_list = list_framestores()
#     if framestore_list:
#         for framestore in framestore_list:
#             print(framestore)
#     else:
#         print("Error executing wiretap_print_tree.")
















import subprocess
import re

def list_framestores():
    try:
        # Execute wiretap_print_tree and capture its output
        command = ["/opt/Autodesk/wiretap/tools/current/wiretap_print_tree", "-h", "127.0.0.1"]
        output = subprocess.check_output(command, universal_newlines=True)

        # Extract framestores using regex and remove the prefix
        framestores = [re.sub(r'^/volumes/', '', framestore.strip()) for framestore in re.findall(r'/volumes/[^ ]*', output)]

        return framestores
    except subprocess.CalledProcessError:
        return None
