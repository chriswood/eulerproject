
import math
from math import sqrt
import decimal
from decimal import Decimal
from itertools import takewhile


def perfect_square(n):
    a = round(sqrt(n))
    return pow(a, 2) == n


def simple_cf(n):
    '''continued fraction representation.
        given an integer n, if the square root is even return
        else return its period.'''
    root = Decimal(n).sqrt()
    print("root:",root)
    while 1:
        a0, a1 = divmod(root, 1)
        yield (a0, root)
        if a1.is_zero():
            return
        root = 1/(root - a0)


limit = 13
total = 0
#for n in range(1, limit + 1):
for n in [23]:
    if perfect_square(n):
        print("{0} is a perfect square".format(n))
        continue
    period = takewhile(lambda x: x[0] > 0, simple_cf(n))
    for i in range(9):
        print("period is", next(period))
