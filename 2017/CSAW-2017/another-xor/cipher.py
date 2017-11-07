import hashlib
import sys

class Cipher:

    def xor(s1,s2):
        return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))

    def repeat(s, l):
        return (s*(int(l/len(s))+1))[:l]

key = sys.argv[1]
plaintext = sys.argv[2] + key
print plaintext
plaintext += hashlib.md5(plaintext).hexdigest()
print plaintext
cipher = xor(plaintext, repeat(key, len(plaintext)))
print cipher
print cipher.encode('hex')
