


def factor(n):
    factors = []
    inc = [4, 2, 4, 2, 4, 6, 2, 6]

    while n % 2 == 0:
        factors.append(2)
        n /= 2

    while n % 3 == 0:
        factors.append(3)
        n /= 3

    while n % 5 == 0:
        factors.append(5)
        n /= 5

    k = 7
    i = 0

    while k * k <= n:
        
        if n % k == 0:
            n /= k
            factors.append(k)
        else:
            k = k + inc[i]
            i = (i+1) % 8

    factors.append(n)
    return factors