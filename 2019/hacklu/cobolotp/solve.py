import string

f = open('./out', 'rb')
d = f.read()

'''
flags = []
for k in range(0xff):
    key = [0xc0, 0xbe, 0x72, 0xf1, 0x02, 0, 0, 0]
    for i in range(42):
        key.append(k)

    print(key)
    index = 0
    flag = ''
    for c in d:
        val = chr(ord(c) ^ key[index])
        # print("{} xor {} = {}".format(hex(c), hex(key[index]), val))
        flag += val
        index += 1

    flags.append(flag)


i = 0
for f in flags:
    print("{}: {}".format(hex(i), f))
    tmp = raw_input()
    i += 1

'''
key = [0xc0, 0xbe, 0x72, 0xf1, 0x02, 0, 0, 0]
for i in range(42):
    key.append(0x37)

index = 0
flag = ''
for c in d:
    val = chr(ord(c) ^ key[index])
    # print("{} xor {} = {}".format(hex(c), hex(key[index]), val))
    flag += val
    index += 1

print(flag)


un = d[5:8]
for i in range(0xff):
    for j in range(0xff):
        for k in range(0xff):
            a = chr(ord(un[0]) ^ i) 
            b = chr(ord(un[1]) ^ j) 
            c = chr(ord(un[2]) ^ k)
            if a in string.ascii_letters and b in string.ascii_letters and c in string.ascii_letters:
                print(flag[:5] + a + b + c + flag[9:])
