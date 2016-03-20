
#
# The primes 3, 7, 109, and 673, are quite remarkable.
# By taking any two primes and concatenating them in any order the result will
#  always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime.
#  The sum of these four primes, 792, represents the lowest sum for a set of
#  four primes with this property.
#
# Find the lowest sum for a set of five primes for which any two primes
# concatenate to produce another prime.
import math
import sys
from itertools import permutations, combinations, count
from collections import deque
from math import sqrt, ceil
from datetime import datetime

def numcat(a,b):
    return int(math.pow(10,(int(math.log(b,10)) + 1)) * a + b)

def is_prime(N):
    if N in (0, 1, 4):
        return False
    if N in (2, 3):
        return True
    last_value = math.ceil(sqrt(N))
    for n in range(2, int(last_value) + 1):
        if (N%n == 0):
            return False
    return True

def check(terms):
    """Takes a list of numbers and checks perms"""
    for term0, term1 in permutations(terms, 2):
        if term0 in prime_pairs:
            if term1 in prime_pairs[term0]:
                continue
        else:
            prime_pairs[term0] = []
        new_term = numcat(term0, term1)
        if new_term in checked_non_primes:
            return False
        if new_term in checked_primes:
            prime_pairs[term0].append(term1)
            continue
        if not is_prime(new_term):
            checked_non_primes.add(new_term)
            return False

        checked_primes.add(new_term)
        prime_pairs[term0].append(term1)
    return True

def build_prime_list(limit):
    # Need to weed as many values as possible out.
    # 2,5 can't be one
    p = filter(is_prime, count(7, 2))
    prime_list = [3]
    term_count = 1
    while term_count <= limit:
        prime_list.append(next(p))
        term_count += 1
    return prime_list

prime_limit = 1500
prime_list = build_prime_list(prime_limit)
checked_non_primes = set()
checked_primes = set()
prime_pairs = {}
found = False

t1 = datetime.now()

#find sets of four

match_fours = filter(check, combinations(prime_list, 4))
while not found:
    print("looking for a match")
    match = next(match_fours)
    print("testing", match)
    for prime in prime_list:
        test_list = list(match)
        if prime in test_list:
            continue
        test_list.append(prime)
        print("checking", test_list)
        if check(test_list):
            print("found it!", test_list)
            found = True
            sys.exit(1)

t2 = datetime.now()
print("this took", t2 - t1)
