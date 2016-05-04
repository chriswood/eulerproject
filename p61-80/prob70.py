#Find the value of n, 1 < n < 10^7, for which φ(n) is a permutation
# of n and the ratio n/φ(n) produces a minimum.
'''
***STRATEGY***
Start with smallest values of n/phi(n), likely primes
for each of these, find a permutation which matches n
**************
'''
import sys
from math import ceil, sqrt
from fractions import Fraction

def is_prime(x):
    # I don't trust these guys :]
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

def anti_prime_sieve(start):
    '''send only odd numbers that are not prime'''
    i = start
    while i > 1:
        if i % 2 == 0 or (not is_prime(i)):
            yield i
        i -= 1

def quick_phi(x):
    phi = 0
    for i in range(1, x):
        if is_coprime(i, x):            
            phi += 1
    return phi

def is_perm(a, b):
    if len(a) == len(b):
        return sorted(a) == sorted(b)
    else:
        return False

def get_phi(n):
    plist.clear()
    prime_factors(n)
    factors = set(plist)
    phi = n
    for factor in factors:
        f = Fraction(1, factor)
        phi *= (1 - f)
    return phi

plist = []
limit = 10**7
min_phi_n_n = limit
min_n = limit
sieve = anti_prime_sieve(limit)
n = next(sieve)
while n > 498000:
    if n % 10000 == 0:
        print(n)
    phi_n = get_phi(n)
    #print("n, phi_n, n/phi_n",n ,phi_n, float(n/phi_n))
    if is_perm(str(n), str(phi_n)):
        phi_n_n = float(n/phi_n)
        if phi_n_n < min_phi_n_n:
            min_n = n
            min_phi_n_n = phi_n_n
            print("new lowest at n", n, min_phi_n_n)
    n = next(sieve)

print("The lowest n was", min_n)