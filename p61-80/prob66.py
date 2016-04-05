
import math
from math import sqrt
from decimal import Decimal
from itertools import takewhile
from fractions import Fraction

def perfect_square(n):
    a = round(sqrt(n))
    return pow(a, 2) == n


def simple_cf(n):
    root = Decimal(n).sqrt()

    while 1:
        a0 = Decimal(math.floor(root))
        yield a0

        root = Decimal(1)/(root - a0)

def cf(terms):
    '''if we are n(terms) levels deep, then return 1/k(n+1) + k(n):
       else return k(n) + 1/cf(k(n+1)'''
    x = terms[0]

    if len(terms) == 1:
        return x
    else:
        return x + Fraction(1, cf(terms[1:]))

terms = [4, 2, 1, 3, 1, 2, 8]
print(cf(terms))
# terms = []
# for n in [19]:
#     if perfect_square(n):
#         print("{0} is a perfect square".format(n))
#         continue
#     period = takewhile(lambda x: x is not 0, simple_cf(n))
#     end = 2 * math.floor(sqrt(n))
#     term = next(period)
#     terms.append(int(term))


#     while int(term) is not end:
#         term = next(period)
#         terms.append(int(term))
 

# print("terms are", terms)
