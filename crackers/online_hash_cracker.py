###################################################
#                                                 #
#    Name       : Online Hash Cracker (HASH++)    #
#    Created by : MomboteQ                        #
#    Version    : 1.0                             #
#                                                 #
###################################################


from colorama import Fore, Style, init
import urllib3
import urllib
import re


def online_crack(hash):
    init()

    if len(hash) == 32:
        hash_type = 'MD5'

    elif len(hash) == 40:
        hash_type = 'SHA-1'

    elif len(hash) == 64:
        hash_type = 'SHA-256'

    elif len(hash) == 96:
        hash_type = 'SHA-384'

    elif len(hash) == 128:
        hash_type = 'SHA-512'

    else:
        hash_type = None

    if hash_type != None:
        print(f'\n[{Fore.LIGHTGREEN_EX}✓{Style.RESET_ALL}] Detected hash type : {Fore.LIGHTBLUE_EX + hash_type + Style.RESET_ALL}')

        http = urllib3.PoolManager()

        try:
            response = http.request('GET', f'https://hashtoolkit.com/decrypt-hash/?hash={hash}')

        except:
            print(f'[{Fore.LIGHTRED_EX}✗{Style.RESET_ALL}] Check your internet connection!\n')
            return

        try:
            decrypted = urllib.parse.unquote(re.search(r'/generate-hash/\?text=(.*?)"', response.data.decode()).group(1))

            print(f'[{Fore.LIGHTGREEN_EX}✓{Style.RESET_ALL}] {hash} : {Fore.LIGHTGREEN_EX + decrypted + Style.RESET_ALL}\n')

        except:
            print(f'[{Fore.LIGHTRED_EX}✗{Style.RESET_ALL}] {hash} : {Fore.LIGHTRED_EX}This hash was not found in the database!{Style.RESET_ALL}\n')

    else:
        print(f'\n[{Fore.LIGHTRED_EX}✗{Style.RESET_ALL}] This hash type is not supported.\n')