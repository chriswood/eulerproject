
# We shall say that an n-digit number is pandigital if it makes use of all the
# digits 1 to n exactly once; for example, the 5-digit number, 15234,
# is 1 through 5 pandigital.
#
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
# multiplicand, multiplier, and product is 1 through 9 pandigital.
#
# Find the sum of all products whose multiplicand/multiplier/product identity
#  can be written as a 1 through 9 pandigital.
# HINT: Some products can be obtained in more than one way so be sure to only
# include it once in your sum.


def is_pandigital(n):
    """ can't start with 0 """
    n = str(n)
    return all(['0' not in n, len(n) == 9, len(set(n)) == 9])

def ccat(x, y, z):
    return ''.join([str(i) for i in [x,y,z]])

found = set()
for x in range(1, 10000):
    if x%500 == 0:
        print("x={0}".format(x))
    for y in range(1, 10000):
        term = ccat(x, y, x*y)
        if is_pandigital(term):
            found.add(x*y)


print("set is {0}".format(found))
print("total is {0}".format(sum(found)))
