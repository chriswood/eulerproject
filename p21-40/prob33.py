

# The fraction 49/98 is a curious fraction, as an inexperienced mathematician
# in attempting to simplify it may incorrectly believe that 49/98 = 4/8,
# which is correct, is obtained by cancelling the 9s.
#
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
# There are exactly four non-trivial examples of this type of fraction,less than
# one in value, and containing two digits in the numerator and denominator.
#
# If the product of these four fractions is given in its lowest common terms,
# find the value of the denominator.
from fractions import Fraction

def check(i, j):
    """ Find if i and j share a common digit, or have a zero """
    i, j = str(i), str(j)
    if '0' in i + j:
        return False
    for digit in i:
        if digit in str(j):
            return True
    return False

def process(i, j):
    """ Remove common digit and check fraction """
    i, j = str(i), str(j)
    common = i[0] if i[0] in j else i[1]
    numerator = i[0] if i[0] == i[1] else int(i.replace(common, ''))
    den = j[0] if j[0] == j[1] else int(j.replace(common, ''))
    numerator, den, i, j = [int(n) for n in [numerator, den, i, j]]
    if Fraction(numerator, den) == Fraction(i, j):
        if i < j: #just 0 < n < 1
            found.append((i,j))

found = []
for i in range(10, 100):
    #if not the same, and both don't end in 0
    for j in range(10, 100):
        if i != j and check(i, j):
            process(i, j)

a = 1
b = 1
for n in found:
    a *= n[0]
    b *= n[1]

print(Fraction(a, b))
