# What is the smallest odd composite that cannot be written
# as the sum of a prime and twice a square?

# e.g.
# 9 = 7 + 2×1^2
# 15 = 7 + 2×2^2
#
# for 9, 15, 21, 25...
from math import ceil, sqrt, trunc

def is_prime(x):
    # check short values
    if x in (1,4):
        return False
    if x in (2, 3):
        return True

    #get last value to test for even division into N
    last_value = ceil(sqrt(x))

    for n in range(2, int(last_value) + 1):
        if (x%n == 0):
            return False
    return True

def primes():
    n = 2
    while True:
        if is_prime(n):
            yield n
        if n == 2:
            n += 1
        else:
            n += 2

def twice_a_square():
    n = 1
    while True:
        yield 2 * n**2
        n += 1

def is_twice_a_square(n):
    if n%2 > 0:
        return False
    else:
        n = float(n) / 2.0
        return sqrt(n) == trunc(sqrt(n))

def odd_composite():
    n = 15
    while True:
        if not is_prime(n):
            yield n
        n += 2

def check(x):
    p = primes()
    i = 0
    while i < x:
        i = next(p)
        if
        if is_twice_a_square(x - i):
            print("{0} = {1} + 2 x {2}^2".format(x, i, sqrt((x - i)/2)))
            return True
    print("{0} is the answer".format(x))
    return False

o = odd_composite()
# good = True
# while good:
#     tas = next(o)
#     good = check(tas)

me = check(5777)
