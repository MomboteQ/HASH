############################################
#                                          #
#    Name       : Hash Creator (HASH++)    #
#    Created by : MomboteQ                 #
#    Version    : 1.0                      #
#                                          #
############################################

from colorama import Fore, Style, init
import hashlib


def hash_creator(hashing_method, text):
    init()

    if hashing_method == 'md5':
        hashed = hashlib.md5(text.encode()).hexdigest()
        hashing_method = 'MD5'

    elif hashing_method == 'sha-1' or hashing_method == 'sha1':
        hashed = hashlib.sha1(text.encode()).hexdigest()
        hashing_method = 'SHA-1'

    elif hashing_method == 'sha-256' or hashing_method == 'sha256':
        hashed = hashlib.sha256(text.encode()).hexdigest()
        hashing_method = 'SHA-256'

    elif hashing_method == 'sha-384' or hashing_method == 'sha384':
        hashed = hashlib.sha384(text.encode()).hexdigest()
        hashing_method = 'SHA-384'

    elif hashing_method == 'sha-512' or hashing_method == 'sha512':
        hashed = hashlib.sha512(text.encode()).hexdigest()
        hashing_method = 'SHA-512'

    else:
        print(f'\n[{Fore.LIGHTRED_EX}✗{Style.RESET_ALL}] This hash type is not supported.\n')
        return

    print(f'\n[{Fore.LIGHTGREEN_EX}✓{Style.RESET_ALL}] {Fore.LIGHTBLUE_EX + hashing_method + Style.RESET_ALL} : {text} : {Fore.LIGHTGREEN_EX + hashed + Style.RESET_ALL}\n')