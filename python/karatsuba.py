from math import ceil

memory = [[0,0,0,0,0,0,0,0,0,0],
          [0,1,2,3,4,5,6,7,8,9],
          [0,2,4,6,8,10,12,14,16,18],
          [0,3,6,9,12,15,18,21,24,27],
          [0,4,8,12,16,20,24,28,32,36],
          [0,5,10,15,20,25,30,35,40,45],
          [0,6,12,18,24,30,36,42,48,54],
          [0,7,14,21,28,35,42,49,56,63],
          [0,8,16,24,32,40,48,56,64,72],
          [0,9,18,27,36,45,54,63,72,81],
          [0,10,20,30,40,50,60,70,80,90]]

def karatsuba(x, y):
    """ Recursive multiplication using karatsuba
    x = 10^n/2 * a + b
    y = 10^n/2 * c + d
    x * y = 10^n * ac + 10^(n/2) (ad+bc) + bd
    where (ad+bc) = (a+b)(c+d) - ac - bd
    """
    str_x, str_y = str(x), str(y)
    n = max(len(str_x), len(str_y))
    if n <= 1:
        # Just for fun to not use any multiplications haha
        return memory[x][y]

    # str_x = prepend_zeros(str_x, n)
    # str_y = prepend_zeros(str_y, n)
    n_2 = n / 2

    a, b = int(str_x[:n_2] or 0), int(str_x[n_2:] or 0)
    c, d = int(str_y[:n_2] or 0), int(str_y[n_2:] or 0)

    one = a * d + b * c

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_bc = karatsuba((a + b), (c + d)) - ac - bd
    if ad_bc == 105:
        print ad_bc
    # for supporting edge case where n is not a multiple of 2
    n_2 = int(ceil(n / 2.0))
    n = n if n % 2 == 0 else n + 1
    return (10**(n) * ac)  + (10**n_2 * ad_bc) + bd

print karatsuba('1685287499328328297814655639278583667919355849391453456921116729', '7114192848577754587969744626558571536728983167954552999895348492')
