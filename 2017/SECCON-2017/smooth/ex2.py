import fractions


# n = open('modulus', 'r').read().encode('hex')
n = 149767527975084886970446073530848114556615616489502613024958495602726912268566044330103850191720149622479290535294679429142532379851252608925587476670908668848275349192719279981470382501117310509432417895412013324758865071052169170753552224766744798369054498758364258656141800253652826603727552918575175830897
# n = hex(n)
print "n=", n

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
        gcd = b
    return gcd, x, y


def ex_egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


def modinv(a, m):
    g, x, y = ex_egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def decrypt(p, q, e, ct):
    n = p * q
    phi = (p - 1) * (q - 1)
    gcd, a, b = egcd(e, phi)
    d = a
    pt = pow(ct, d, n)
    return hex(pt)[2:-1]


def isqrt(n):
    x = n
    y = (x + n // x) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x


def fermat(n):
    x = isqrt(n) + 1
    y = isqrt(x * x - n)

    while True:
        w = x * x - n - y * y
        if w == 0:
            break
        elif w > 0:
            y += 1
        else:
            x += 1
        return x+y, x-y


def prime_decomposition(n):
    print("prime")
    i = 2
    table = []
    while i * i <= n:
        while n % i == 0:
            print(table)
            n /= i
            table.append(i)
        i += 1
    if n > 1:
        table.append(n)
    return table


def is_prime(n):
    i = 2
    while i * i <=n:
        if n % i == 0:
            return False
        i += 1
    return True


print('start')

t = prime_decomposition(n)

print(t)

e = 65537

# p, q = fermat(eval(n))

# print "p=", str(p)
# print "q=", str(q)
