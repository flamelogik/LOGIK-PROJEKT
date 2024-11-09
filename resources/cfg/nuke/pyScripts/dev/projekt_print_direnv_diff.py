import base64
import zlib
import json
import os

def decompress_diff(string):
    decode = base64.urlsafe_b64decode(string)
    decompress = zlib.decompress(decode)
    x = json.loads(decompress)['n']
    return x

def strip_direnv_from_dictionary(dic,strip):
    dic = {k: v for k, v in dic.items() if not k.startswith(strip)}
    return dic

#####################################################################3

def main():
    direnv_diff_str = os.environ.get('DIRENV_DIFF')
    if direnv_diff_str:
        direnv_vars = decompress_diff(direnv_diff_str)

        for k, v in direnv_vars.items():
            print(f"{k}: {v}")
    else:
        print("DIRENV_DIFF environment variable not found.")
