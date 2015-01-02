# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a2 + b2 = c2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

from itertools import count
from math import hypot

def is_pyth(sides):
    return hypot(sides[0], sides[1]) == float(sides[2])



# not found :(
# I need to generate all triplets, using a modified version of Euclid's
# formula for primitive triplets (add the k multiple in).

# first need test for if numbers are coprime

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def coprime(a, b):
	return gcd(a, b) == 1

print(coprime(4,10))

# where m greater n, m minus n odd, and with m and n coprime.
# a = k(m^2 - n^2)
# b = k(2mn)
# c = k(m^2 + n^2)
