from itertools import cycle
from fractions import Fraction

def k_sieve():
    yield 2
    yield 1
    k = 1
    multipliers = cycle([2,1,1])
    while 1:
        n = next(multipliers)
        if n == 2:
            n = k * n
            k += 1
        yield n

#e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].

def cf(k, terms):
    '''if we are n(terms) levels deep, then return 1/k(n+1) + k(n):
       else return k(n) + 1/cf(k(n+1)'''
    print("called with k,terms=", k,terms)

    if terms == 1:
        return k
    elif terms == 2:
        return k + Fraction(1, next(k_terms))
    else:
        return k + Fraction(1, (cf(next(k_terms), terms - 1)))

term_num = 100
k_terms = k_sieve()
e = cf(Fraction(next(k_terms)), term_num)
print("For", term_num, "terms, e is approximately: ", e)
print("Sum of numerator is",sum(map(int, str(e.numerator))))