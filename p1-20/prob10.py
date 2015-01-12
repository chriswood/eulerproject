# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

from math import sqrt, ceil

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
    last_value = ceil(sqrt(N))

    for n in xrange(2, int(last_value) + 1):
        if (N%n == 0):
            return False
    return True

total = 2 # skip 2 so the range step comes out right
for i in xrange(3, 2000000, 2):
    if is_prime(i):
		print("Prime: ", i)
		total += i
print("Total: ", total)
