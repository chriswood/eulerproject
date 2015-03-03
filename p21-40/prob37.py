
# The number 3797 has an interesting property. Being prime itself, it is possible
# to continuously remove digits from left to right, and remain prime at each
# stage: 3797, 797, 97, and 7. Similarly we can work from right to left:
#  3797, 379, 37, and 3.
#
# Find the sum of the only eleven primes that are both truncatable from left to
#  right and right to left.
#
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
from math import ceil, sqrt
from time import time

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

def trim(n, direction):
    """takes and returns string"""
    if direction == 'left':
        return(n[1:])
    else:
        return(n[:-1])

def check_left(n):
    if len(n) == 1 and is_prime(int(n)):
        return True
    if is_prime(int(n)):
        return check_left(trim(n, 'left'))
    else:
        return False

def check_right(n):
    if len(n) == 1 and is_prime(int(n)):
        return True
    if is_prime(int(n)):
        return check_right(trim(n, 'right'))
    else:
        return False

t = time()
limit = 11
sieve = filter(is_prime, range(11, 10**6))
found = []

while len(found) < limit:
    p = str(next(sieve))
    if check_left(p) and check_right(p):
        print("found one! {0}".format(p))
        found.append(int(p))

print(found)
print(sum(found))
print("time is {0}".format(time() - t))
