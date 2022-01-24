########################################################
#                                                      #
#    Name       : Brute Force Hash Cracker (HASH++)    #
#    Created by : MomboteQ                             #
#    Version    : 1.0                                  #
#                                                      #
########################################################


from multiprocessing import cpu_count, Queue, Process
from string import ascii_letters, digits, punctuation
from itertools import product, islice
from hashlib import md5, sha1, sha256, sha384, sha512
from functools import cache
from colorama import Fore, Style, init
from threading import Thread


class Brute:
    def __init__(self):
        self.charset = ascii_letters + digits + punctuation + ' '
        self.processes = cpu_count() + 1

    
    def run(self, params):
        start, end, length = params
        
        for candidate in islice(product(self.charset, repeat = length), start, end):
            candidate = ''.join(candidate)

            if self.function(candidate) == self.hash:
                return candidate

        return None


    def fun(self, f, q_in, q_out):
        while True:
            try:
                i, x = q_in.get()
                
                if i is None or self.found:
                    break

                res = f(x)
                q_out.put((i, res))

                if res:
                    break

            except KeyboardInterrupt:
                break


    def parmap(self, f, X):
        q_in = Queue(1)
        q_out = Queue()

        proc = [Process(target = self.fun, args = (f, q_in, q_out)) for _ in range(self.processes)]

        for p in proc:
            p.daemon = True
            p.start()


        sent = [q_in.put((i, x)) for i, x in enumerate(X)]
        [q_in.put((None, None)) for _ in range(self.processes)]
        res = [q_out.get() for _ in range(len(sent))]

        [p.join() for p in proc]

        return [x for i, x in sorted(res)]


    def brute(self, hash, function):
        self.found = False
        self.hash = hash
        self.function = function

        length = 0

        while True:
            length += 1
            nb_candidates = len(self.charset) ** length
            step = nb_candidates // self.processes
            params = [(pos, pos + step, length) for pos in range(0, nb_candidates, step)]


            for i in range(self.processes):
                for res in self.parmap(self.run, params):
                    if res:
                        return res


def md5_cracker(candidate):
    return md5(candidate.encode()).hexdigest()


def sha1_cracker(candidate):
    return sha1(candidate.encode()).hexdigest()


def sha256_cracker(candidate):
    return sha256(candidate.encode()).hexdigest()


def sha384_cracker(candidate):
    return sha384(candidate.encode()).hexdigest()


def sha512_cracker(candidate):
    return sha512(candidate.encode()).hexdigest()


def brute_cracker(hash):
    init()

    if len(hash) == 32:
        print(f'\n[{Fore.LIGHTGREEN_EX}✓{Style.RESET_ALL}] Detected hash type :{Fore.LIGHTBLUE_EX} MD5 {Style.RESET_ALL}')
        print(f'[{Fore.LIGHTBLUE_EX}i{Style.RESET_ALL}] Cracking...', end = '\r')
        
        brute = Brute()
        decrypted = brute.brute(hash, md5_cracker)

        print(f'[{Fore.LIGHTGREEN_EX}✓{Style.RESET_ALL}] {hash} : {Fore.LIGHTGREEN_EX + decrypted + Style.RESET_ALL}\n')

    elif len(hash) == 40:
        print(f'\n[{Fore.LIGHTGREEN_EX}✓{Style.RESET_ALL}] Detected hash type :{Fore.LIGHTBLUE_EX} SHA-1 {Style.RESET_ALL}')
        print(f'[{Fore.LIGHTBLUE_EX}i{Style.RESET_ALL}] Cracking...', end = '\r')

        brute = Brute()
        decrypted = brute.brute(hash, sha1_cracker)

        print(f'[{Fore.LIGHTGREEN_EX}✓{Style.RESET_ALL}] {hash} : {Fore.LIGHTGREEN_EX + decrypted + Style.RESET_ALL}\n')

    elif len(hash) == 64:
        print(f'\n[{Fore.LIGHTGREEN_EX}✓{Style.RESET_ALL}] Detected hash type :{Fore.LIGHTBLUE_EX} SHA-256 {Style.RESET_ALL}')
        print(f'[{Fore.LIGHTBLUE_EX}i{Style.RESET_ALL}] Cracking...', end = '\r')

        brute = Brute()
        decrypted = brute.brute(hash, sha256_cracker)

        print(f'[{Fore.LIGHTGREEN_EX}✓{Style.RESET_ALL}] {hash} : {Fore.LIGHTGREEN_EX + decrypted + Style.RESET_ALL}\n')

    elif len(hash) == 96:
        print(f'\n[{Fore.LIGHTGREEN_EX}✓{Style.RESET_ALL}] Detected hash type :{Fore.LIGHTBLUE_EX} SHA-384 {Style.RESET_ALL}')
        print(f'[{Fore.LIGHTBLUE_EX}i{Style.RESET_ALL}] Cracking...', end = '\r')

        brute = Brute()
        decrypted = brute.brute(hash, sha384_cracker)

        print(f'[{Fore.LIGHTGREEN_EX}✓{Style.RESET_ALL}] {hash} : {Fore.LIGHTGREEN_EX + decrypted + Style.RESET_ALL}\n')

    elif len(hash) == 128:
        print(f'\n[{Fore.LIGHTGREEN_EX}✓{Style.RESET_ALL}] Detected hash type :{Fore.LIGHTBLUE_EX} SHA-512 {Style.RESET_ALL}')
        print(f'[{Fore.LIGHTBLUE_EX}i{Style.RESET_ALL}] Cracking...', end = '\r')

        brute = Brute()
        decrypted = brute.brute(hash, sha512_cracker)

        print(f'[{Fore.LIGHTGREEN_EX}✓{Style.RESET_ALL}] {hash} : {Fore.LIGHTGREEN_EX + decrypted + Style.RESET_ALL}\n')

    else:
        print(f'\n[{Fore.LIGHTRED_EX}✗{Style.RESET_ALL}] This hash type is not supported.\n')