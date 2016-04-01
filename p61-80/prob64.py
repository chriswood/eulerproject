
import math
from math import sqrt
import decimal
from decimal import Decimal, getcontext
from itertools import takewhile
getcontext().prec = 250

def perfect_square(n):
    a = round(sqrt(n))
    return pow(a, 2) == n


def simple_cf(n):
    '''continued fraction representation.
        given an integer n, if the square root is even return
        else return its period.'''
    root = Decimal(n).sqrt()

    while 1:
        a0 = Decimal(math.floor(root))
        yield a0

        root = Decimal(1)/(root - a0)


limit = 10000
total = 0
for n in range(1, limit + 1):
    if perfect_square(n):
        print("{0} is a perfect square".format(n))
        continue
    period = takewhile(lambda x: x is not 0, simple_cf(n))
    end = 2 * math.floor(sqrt(n))
    term = next(period)
    p_len = 0

    while int(term) is not end:
        term = next(period)
        p_len += 1
    print("{0}: {1}".format(n, p_len))
    if p_len % 2 == 1:
        total += 1
    if p_len > 300:
        print("WHOOOOOOOOOOOOOOOOAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        sys.exit()

print("_______________________")
print("total is", total)