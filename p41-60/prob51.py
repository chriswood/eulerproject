import math
from math import sqrt, ceil
from itertools import combinations
from string import digits
from copy import deepcopy
import sys

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

def replace_count_primes(n):
    """Returns the number of primes made out of replacing
       various (mu) values"""
    s = list(str(n))
    length = len(s)
    print(n)
    for c in combinations(digits[:length], mu):
        test_list = []
        for i in range(10):
            new_s = deepcopy(s)
            for place in c:
                new_s[int(place)] = str(i)
            new_n = int(''.join(new_s))
            if no_leading_zeroes and len(str(new_n)) < length:
                continue
            if is_prime(new_n):
                test_list.append(new_n)
        if(len(test_list) >= 8):
            print("FOUND!!!")
            print(test_list)
            return True
    return False


test = 88888
mu = 3
no_leading_zeroes = True

found = False
start = 90008
while not found:
    found = replace_count_primes(start)
    start += 1
