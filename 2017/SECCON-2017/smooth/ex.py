def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
        gcd = b
    return gcd, x, y

def decrypt(p, q, e, ct):
    n = p * q
    phi = (p - 1) * (q - 1)
    gcd, a, b = egcd(e, phi)
    d = a
    pt = pow(ct, d, n)
    return hex(pt)[2:-1].decode("hex")

def is_prime(q):
    q = abs(q)
    if q == 2: return True
    if q < 2 or q&1 == 0: return False
    return pow(2, q-1, q) == 1


def small_prime(modulus):
    i = 2 
    while True:
        if is_prime(i):
            print "i=", i
            if modulus % i == 0:
                return i, modulus/i
        else:
            pass
        i += 1

print("start")

f = open("modulus", "r")
n = f.read().encode("hex")
f.close()

n = '0x'+n[2:]
e = 65537

p, q = small_prime(eval(n))

print "p=", str(p)
print "q=", str(q)
