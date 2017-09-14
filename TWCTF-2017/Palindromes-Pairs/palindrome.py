from netcat import Netcat
import itertools

nc = Netcat('ppc1.chal.ctf.westerns.tokyo', 8765)

nc.read_until(' -----')
print(nc.buff)
p = nc.buff.split('\n')
char_list = p[3].split(' ')
cnt = 0

for k in itertools.permutations(char_list, 2):
    string = ''.join(k)
    if string == string[::-1]:
        cnt += 1

for k in range(len(char_list)):
    s = char_list[k] + char_list[k]
    if s == s[::-1]:
        cnt += 1

print("count: " + str(cnt))
nc.write(str(cnt) + "\r\n")


print(nc.read())
data = nc.read()
data = data.split('\n')
char_list = data[2].split(' ')
while 1:
    cnt = 0

    for k in itertools.permutations(char_list, 2):
        string = ''.join(k)
        if string == string[::-1]:
            cnt += 1

    for k in range(len(char_list)):
        s = char_list[k] + char_list[k]
        if s == s[::-1]:
            cnt += 1

    print("count: " + str(cnt))
    nc.write(str(cnt) + "\r\n")
    
    print(nc.read())
    data = nc.read()
    print(data)
    data = data.split('\n')
    char_list = data[2].split(' ')

