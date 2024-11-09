
import os
import base64
import zlib
import json

def decompress_diff(string):
    decode = base64.urlsafe_b64decode(string)
    decompress = zlib.decompress(decode)
    x = json.loads(decompress)['n']
    return x

def strip_direnv_from_dictionary(dic,strip):
    dic = {k: v for k, v in dic.items() if not k.startswith(strip)}
    return dic

def main():
    string = os.environ['DIRENV_DIFF']


    partytime_env = decompress_diff(string)

    for k,v in partytime_env.items():
        print(f"{k}: {v}")