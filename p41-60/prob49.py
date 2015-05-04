# What 3 4 digit numbers are ...
#    permutations of each other
#    prime
#    arithmetic sequence
#
# 1487, 4817, 8147

#for each 4 digit prime number...
import math
from math import sqrt, ceil
from itertools import combinations

def is_prime(N):
    if N in (1, 4):
        return False
    if N in (2, 3):
        return True

    last_value = math.ceil(sqrt(N))

    for n in range(2, int(last_value) + 1):
        if (N%n == 0):
            return False
    return True

def is_combo(i, j):
    s1 = str(i)
    s2 = str(j)
    return set(s1) == set(s2)

c = combinations('1234567890', 4)

possibles = [int("".join(perm)) for perm in c
    if perm[0] != '0' and is_prime(int("".join(perm)))]

for term in filter(is_prime, range(1000, 10000)):
    print("checking ", term)
    for n in range(1000, 10000):
        y1 = term + n
        if y1 > 10000:
            continue
        if is_prime(y1) and is_combo(term, y1):
            y2 = y1 + n
            if y2 > 10000:
                continue
            if is_prime(y2) and is_combo(term, y2):
                print("Found one, {0}, {1}, {2}".format(term, y1, y2))
