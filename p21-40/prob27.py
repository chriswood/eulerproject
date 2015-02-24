# Find the product of the coefficients, a and b, for the quadratic expression
# that produces the maximum number of primes for consecutive values of n,
# starting with n = 0. for |a|<1000, |b|<1000,
# form n^2 + an + b

# NOTE for given sequence, b must be prime, and a+b+1 must be prime
from math import ceil, sqrt

def quad(n, a, b):
    return pow(n, 2) + n * a + b

def is_prime(x):
    # check predefined values
    if x == 1:
        return False
    if x in (2, 3):
        return True

    #get last value to test for even division into N
    last_value = ceil(sqrt(x))

    for n in range(2, int(last_value) + 1):
        if (x%n == 0):
            return False
    return True

primes = [x for x in range(1, 1001) if is_prime(x)]
max_coef = (0, 0)
max_n = 0
# test b = 7

for b in primes:
    print("checking b={0}. greatest is {1}".format(b, max_n))
    for a in range(-1000, 1000):
        n = 0
        still_prime = True
        while still_prime:
            res = quad(n, a, b)
            if res > 1:
                if not is_prime(res):
                    still_prime = False
                else:
                    if n > max_n:
                        max_n = n
                        max_coef = (a, b)
                    n += 1
            else:
                still_prime = False
print("max n: {0}, coefficients: {1}".format(max_n, max_coef))
