#!/usr/bin/python2

import sys
import random

key = sys.argv[1]
flag = 'TWCTF{AAAAAAAAAAAAAA}'

assert len(key) == 13
assert max([ord(char) for char in key]) < 128
assert max([ord(char) for char in flag]) < 128

message = flag + "|" + key
print("M: " + message)

encrypted = chr(random.randint(0, 128))
print(encrypted)

for i in range(0, len(message)):
  encrypted += chr((ord(message[i]) + ord(key[i % len(key)]) + ord(encrypted[i])) % 128)
  print(str(i) + ": " + encrypted)

print(encrypted)
print(len(encrypted))
print(encrypted.encode('hex'))
