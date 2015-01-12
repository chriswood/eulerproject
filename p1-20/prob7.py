# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13.

# What is the 10001st prime number?
from itertools import count
import math

def is_prime(N):
    '''
    Check a number N and see if it is divisible by anything less than
    it's square root evenly.
    '''
    # check predefined values
    if N in (1, 4):
        return False
    if N in (2, 3):
        return True

    #get last value to test for even division into N
    last_value = math.ceil(math.sqrt(N))

    for n in xrange(2, int(last_value) + 1):
        if (N%n == 0):
            return False
    return True

find = 10001
prime_count = 1 #starting with 3
for n in count(3, 2):
    if is_prime(n):
        prime_count += 1
        print("%ith prime found:" %prime_count, n)
        if prime_count >= find:
            break
