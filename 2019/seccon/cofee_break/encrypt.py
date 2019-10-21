import sys
from Crypto.Cipher import AES
import base64


def encrypt(key, text):
    s = ''
    for i in range(len(text)):
        s += chr((((ord(text[i]) - 0x20) + (ord(key[i % len(key)]) - 0x20)) % (0x7e - 0x20 + 1)) + 0x20)
    return s


def decrypt(key, s, n):
    text = ''
    for i in range(len(s)):
        tmp = (0x7e - 0x20 + 1) * n + s[i] - 0x20 - ord(key[i % len(key)]) + 0x20 + 0x20
        if tmp > 127:
            text += chr(tmp - 95)
        else:
            text += chr((0x7e - 0x20 + 1) * n + s[i] - 0x20 - ord(key[i % len(key)]) + 0x20 + 0x20)
    return text



key1 = "SECCON"
key2 = "seccon2019"
text = sys.argv[1]

print("--- enc ---")
enc1 = encrypt(key1, text)
cipher = AES.new(key2 + chr(0x00) * (16 - (len(key2) % 16)), AES.MODE_ECB)
p = 16 - (len(enc1) % 16)
enc2 = cipher.encrypt(enc1 + chr(p) * p)
print(base64.b64encode(enc2).decode('ascii'))


print("--- dec ---")
cipher_text = base64.b64decode(sys.argv[1])
cipher_text = cipher.decrypt(cipher_text)
cipher_text = cipher_text
c = decrypt(key1, cipher_text, 1)
print(c)

