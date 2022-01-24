################################
#                              #
#    Name       : HASH++       #
#    Created by : MomboteQ     #
#    Version    : 1.0          #
#                              #
################################


from colorama import Fore, Style, init
from textwrap import dedent
from os import name, system
from getpass import getuser

from crackers.online_hash_cracker import online_crack
from crackers.brute_hash_cracker import brute_cracker

from creators.hash_creator import hash_creator

def clear():
    if name == 'nt':
        system('cls')

    else:
        system('clear')


def logo():
    print(dedent(f'''
    {Fore.LIGHTRED_EX} _    _           _____ _    _ {Fore.LIGHTYELLOW_EX}   _     _       {Fore.LIGHTBLUE_EX}||
    {Fore.LIGHTRED_EX}| |  | |   /\    / ____| |  | |{Fore.LIGHTYELLOW_EX} _| |_ _| |_     {Fore.LIGHTBLUE_EX}||    {Fore.LIGHTMAGENTA_EX}Name        {Fore.LIGHTGREEN_EX}:  {Fore.LIGHTYELLOW_EX}HASH++
    {Fore.LIGHTRED_EX}| |__| |  /  \  | (___ | |__| |{Fore.LIGHTYELLOW_EX}|_   _|_   _|    {Fore.LIGHTBLUE_EX}||    {Fore.LIGHTMAGENTA_EX}Version     {Fore.LIGHTGREEN_EX}:  {Fore.LIGHTYELLOW_EX}1.0
    {Fore.LIGHTRED_EX}|  __  | / /\ \  \___ \|  __  |{Fore.LIGHTYELLOW_EX}  |_|   |_|      {Fore.LIGHTBLUE_EX}||    {Fore.LIGHTMAGENTA_EX}Created by  {Fore.LIGHTGREEN_EX}:  {Fore.LIGHTYELLOW_EX}MomboteQ
    {Fore.LIGHTRED_EX}| |  | |/ ____ \ ____) | |  | |                 {Fore.LIGHTBLUE_EX}||    {Fore.LIGHTMAGENTA_EX}Website     {Fore.LIGHTGREEN_EX}:  {Fore.LIGHTYELLOW_EX}https://MomboteQ.github.io
    {Fore.LIGHTRED_EX}|_|  |_/_/    \_\_____/|_|  |_|                 {Fore.LIGHTBLUE_EX}||{Style.RESET_ALL}


    [{Fore.LIGHTYELLOW_EX}!{Style.RESET_ALL}] This tool is for educational purposes only!
    [{Fore.LIGHTBLUE_EX}i{Style.RESET_ALL}] Type {Fore.LIGHTBLUE_EX}help{Style.RESET_ALL} to get all commands.
    '''))


# Commands

def commands():
    command = input(f'{Fore.LIGHTRED_EX}{getuser()}{Fore.LIGHTYELLOW_EX}@{Fore.LIGHTRED_EX}HASH++{Style.RESET_ALL} >> ')
    command = command.strip().split(' ')

    if command == ['']:
        print(f'\n[{Fore.LIGHTRED_EX}✗{Style.RESET_ALL}] Enter command! Type {Fore.LIGHTBLUE_EX}help{Style.RESET_ALL} to get all commands.\n')

    else:
        handlers = {
            'crack': crack,
            'create': create,
            'help': help,
            'exit': exitTool
        }

        handler = handlers.get(command[0], None)

        if handler:
            handler(command[1:])

        else:
            print(f'\n[{Fore.LIGHTRED_EX}✗{Style.RESET_ALL}] Invalid command! Type {Fore.LIGHTBLUE_EX}help{Style.RESET_ALL} to get all commands.\n')


def crack(args):
    try:
        cracking_method = args[0].lower()

        try:
            hash_to_crack = args[1]

            if cracking_method == 'online':
                online_crack(hash_to_crack)

            elif cracking_method == 'brute':
                brute_cracker(hash_to_crack)

            else:
                print(f'\n[{Fore.LIGHTRED_EX}✗{Style.RESET_ALL}] Unknown cracking method!\n')

        except IndexError as e:
            print(f'\n[{Fore.LIGHTRED_EX}✗{Style.RESET_ALL}] Enter hash to crack!\n')


    except IndexError as e:
        print(f'\n[{Fore.LIGHTRED_EX}✗{Style.RESET_ALL}] Enter cracking method!\n')
    


def create(args):
    hash_creator(args[0].lower(), ' '.join(word for word in args[1:len(args)]))


def help(args):
    print(dedent(f'''
    {Fore.LIGHTMAGENTA_EX}Hash cracking:{Style.RESET_ALL}
    {Fore.LIGHTYELLOW_EX}crack online{Fore.LIGHTBLUE_EX} [HASH]{Style.RESET_ALL} - {Fore.LIGHTGREEN_EX}Cracks the hash using online datbase.
    {Fore.LIGHTYELLOW_EX}crack brute{Fore.LIGHTBLUE_EX} [HASH]{Style.RESET_ALL} - {Fore.LIGHTGREEN_EX}Cracks the hash using brute force.
    Supported hashes:{Fore.LIGHTBLUE_EX} MD5{Fore.LIGHTGREEN_EX}, {Fore.LIGHTBLUE_EX}SHA-1{Fore.LIGHTGREEN_EX}, {Fore.LIGHTBLUE_EX}SHA-256{Fore.LIGHTGREEN_EX}, {Fore.LIGHTBLUE_EX}SHA-384{Fore.LIGHTGREEN_EX}, {Fore.LIGHTBLUE_EX}SHA-512{Fore.LIGHTGREEN_EX}.{Style.RESET_ALL}

    {Fore.LIGHTMAGENTA_EX}Hash creating:{Style.RESET_ALL}
    {Fore.LIGHTYELLOW_EX}create hash{Fore.LIGHTBLUE_EX} [HASHING METHOD] [TEXT TO HASHING]{Style.RESET_ALL} - {Fore.LIGHTGREEN_EX}Hashes the entered text with the chosen hashing method.
    Supported hashing methods:{Fore.LIGHTBLUE_EX} MD5{Fore.LIGHTGREEN_EX}, {Fore.LIGHTBLUE_EX}SHA-1{Fore.LIGHTGREEN_EX}, {Fore.LIGHTBLUE_EX}SHA-256{Fore.LIGHTGREEN_EX}, {Fore.LIGHTBLUE_EX}SHA-384{Fore.LIGHTGREEN_EX}, {Fore.LIGHTBLUE_EX}SHA-512{Fore.LIGHTGREEN_EX}.{Style.RESET_ALL}

    {Fore.LIGHTMAGENTA_EX}Other commands:{Style.RESET_ALL}
    {Fore.LIGHTYELLOW_EX}help{Style.RESET_ALL} - {Fore.LIGHTGREEN_EX}Shows all commands with their description.{Style.RESET_ALL}
    {Fore.LIGHTYELLOW_EX}exit{Style.RESET_ALL} - {Fore.LIGHTGREEN_EX}Exits this tool.{Style.RESET_ALL}
    '''))


def exitTool(args):
    exit()

if __name__ == '__main__':
    init()
    
    clear()
    logo()

    while True:
        commands()