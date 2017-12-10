def fib1(n):
    if n <= 1:
        return n
    n0, n1 = 0, 1
    for _ in range(n):
        n0, n1 = n1, n0+n1
    return n0


def fib2(n):
    if n <= 1:
        return n
    result = [1, 0, 0, 1]
    matrix = [1, 1, 1, 0]
    while n > 0:
        if n % 2:
            result = mul(matrix, result)
        matrix = mul(matrix, matrix)
        n //= 2
    return result[2]


def mul(a, b):
    return [a[0]*b[0] + a[1]*b[2],
            a[0]*b[1] + a[1]*b[3],
            a[2]*b[0] + a[3]*b[2],
            a[2]*b[1] + a[3]*b[3]]


print(str(fib2(11011))[:32])
