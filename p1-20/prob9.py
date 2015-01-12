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

# Formula obtained by solving for c using 2 provided equations
for b in count(1):
    c = (pow(1000, 2) - 2000.0*b + 2.0*pow(b, 2))/(2000.0 - 2.0*b)
    if c.is_integer():
        a = 1000 - b - c
        print("(a, b, c):", (a, b, c))
        print("Pythagorean test:", is_pyth((a, b, c)))
        print("Product: ", a*b*c)
        break
