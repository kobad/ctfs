import os
from Crypto.Cipher import AES

def crc32(crc, data):
  crc = 0xFFFFFFFF ^ crc
  for c in data:
    crc = crc ^ ord(c)
    for i in range(8):
      crc = (crc >> 1) ^ (0xEDB88320 * (crc & 1))
  return 0xFFFFFFFF ^ crc

def dec(crc, data):
  crc = 0xFFFFFFFF ^ crc
  for c in data:
    crc = crc ^ ord(c)
    for i in range(8):
      crc = (crc >> 1) ^ (0xEDB88320 * (crc & 1))
  return 0xFFFFFFFF ^ crc


crc = 0xb09bc54f
crc2 = 0x474c2650
print(hex(dec(crc2, "TSG")))


exit()

key = b""

crc = 0
for i in range(int("1" * 1000)):
  con = crc ^ 0xFFFFFFFF
  if con == 0xb09bc54f:
      print("i: ", con)
      break
  crc = crc32(crc, "TSG")
assert(crc == 0xb09bc54f)
key += crc.to_bytes(4, byteorder='big')

print('end')
exit()

crc = 0
for i in range(int("1" * 10000)):
  crc = crc32(crc, "is")
key += crc.to_bytes(4, byteorder='big')

crc = 0
for i in range(int("1" * 10000)):
  crc = crc32(crc, "here")
key += crc.to_bytes(4, byteorder='big')

crc = 0
for i in range(int("1" * 10000)):
  crc = crc32(crc, "at")
key += crc.to_bytes(4, byteorder='big')

crc = 0
for i in range(int("1" * 10000)):
  crc = crc32(crc, "SECCON")
key += crc.to_bytes(4, byteorder='big')

crc = 0
for i in range(int("1" * 10000)):
  crc = crc32(crc, "CTF!")
key += crc.to_bytes(4, byteorder='big')

flag = os.environ['FLAG']
assert(len(flag) == 32)

aes = AES.new(key, AES.MODE_ECB)
encoded = aes.encrypt(flag)
assert(encoded.hex() == '79833173d435b6c5d8aa08f790d6b0dc8c4ef525823d4ebdb0b4a8f2090ac81e')
