import sys

key = "TWCTF{hogeho}"  # len = 13
flag = 'TWCTF{AAAAAAAAAAAAAA}'  # len = 19
message = flag + "|" + key  # len = 35
decrypted = ""

code = sys.argv[1]
encrypted = code.decode('hex')
print(encrypted)
key = ""

for i in range(0, len(encrypted)-1):
#  ord(message[i] + ord(key[i % 13]) = ord(encrypted[i]) - ord(encrypted[i+1])
    print("ord: " + str(ord(encrypted[i+1])) + ", " + str(ord(encrypted[i])))
    print(ord(encrypted[i+1]) - ord(encrypted[i]))
