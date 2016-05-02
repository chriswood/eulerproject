from time import time
from math import sqrt, ceil
from fractions import Fraction
#If the prime factorisation of n is given by n =p1e1*...*pnen, then φ(n) = n *(1 - 1/p1)* ... (1 - 1/pn).

import itertools
import functools

def is_prime(N):
    '''
    Check a number N and see if it is divisible by anything less than
    its square root evenly.
    '''
    # check quick values
    if N in (1, 4):
        return False
    if N in (2, 3):
        return True

    #get last value to test for even division into N
    last_value = ceil(sqrt(N))

    for n in range(2, int(last_value) + 1):
        if (N%n == 0):
            return False
    return True

def prime_factors(num):
    '''
    List prime factors as often as they occur
    '''
    if is_prime(num): #end condition
        plist.append(num)
        return
    end = int(ceil(float(num)/2.0))
    for n in range(2, end+1):
        if num % n == 0:
            if is_prime(n):
                plist.append(n)
            factor2 = num/n
            if is_prime(factor2):
                plist.append(int(factor2))
            else:
                prime_factors(factor2)
            #stop loop from continuing upon recursion
            break

t1 = time()
limit = 1000000
plist = []
max_n = 0
max_phi_n = 0
for n in range(2, limit+1):
    plist.clear()
    prime_factors(n)
    factors = set(plist)
    phi = n
    for factor in factors:
        f = Fraction(1, factor)
        phi *= (1 - f)
    phi_n = float(n/phi)
    if phi_n >= max_phi_n:
        max_phi_n = phi_n
        max_n = n
        print("NEW MAX HEAR  YEE", n, phi_n)
    #print("phi({0}) = {1}".format(n, phi))

print("The highest n was", max_n)
print("phi({0}) = {1}".format(max_n, max_phi_n))
print("this took", time() - t1)