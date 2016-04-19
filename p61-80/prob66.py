
import math
from math import sqrt
from decimal import Decimal, getcontext
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

def convergence_sum(terms):
    '''if we are n(terms) levels deep, then return 1/k(n+1) + k(n):
       else return k(n) + 1/cf(k(n+1)'''
    x = terms[0]

    if len(terms) == 1:
        return x
    else:
        return x + Fraction(1, convergence_sum(terms[1:]))

def c_sum_iterative(terms):
    s = terms.pop()
    for i in range(len(terms)): 
        s = Fraction(1, s) + Fraction(terms.pop(),1)
    return s

def get_term_set(n):
    '''return one period of terms for the square root of n,
       including first estimate convergence term'''
    t = []
    term_sieve = simple_cf(n)
    end = 2 * math.floor(sqrt(n))
    term = next(term_sieve)
    t.append(int(term))

    while int(term) is not end:
        term = next(term_sieve)
        t.append(int(term))
    return t

getcontext().prec = 250
max_x = 0
max_n = 0
limit = 1000

for n in range(2,limit + 1):
    #make sure it can be solved
    if perfect_square(n):
        print("{0} is a perfect square".format(n))
        continue
    #get the FULL period
    period = get_term_set(n)

    #subtract r+1
    l = len(period) - 1

    if l%2: #r odd
        s = convergence_sum(period + period[1:-1])
    else:
        s = convergence_sum(period[:-1])
    x = s.numerator
    y = s.denominator

    if x > max_x:
        print("New maximum at x^2 - {0}y^2 = 1.  x,y= {1}, {2}".format(n, x, y))
        max_x = x
        max_n = n

print("highest was n=", max_n)
print("highest was x=", max_x)