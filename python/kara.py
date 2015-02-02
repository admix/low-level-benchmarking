def kmult(x, y):
    if min(x, y) < 10:
        return x * y

    m = half_ceil(degree(max(x, y)))

    x1, x0 = decompose(x, m)
    y1, y0 = decompose(y, m)

    z2 = kmult(x1, y1)
    z0 = kmult(x0, y0)
    z1 = kmult((x1 + x0), (y1 + y0)) - z2 - z0

    if z1 == 67:
        print z1
    xy = z2 * 10**(2*m)  +  z1 * 10**m  +  z0

    return xy


def decompose(x, m):
    return x // 10 ** m, x % 10 ** m

def degree(x):
    return len(str(x))

def half_ceil(n):
    return n // 2 + (n & 1)

print kmult(8436939677358274975644341226884162349535836199962392872868456892,3864264464372346883776335161325428226997417338413342945574123327)
