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


#if a^2 + b^2 = c^2, then (n)a^2 + (n)b^2 = (n)c^2 for n = 1,2,3...
side_len = (3, 4, 5)
for n in range(1, 100):
    new_len = map(lambda x:n*x, side_len)
    print("trying: ", new_len, n)
    print("sum: ", sum(new_len))
    if is_pyth(new_len) and (sum(new_len) == 1000):
        print("Fount it!!!", new_len)
        break
