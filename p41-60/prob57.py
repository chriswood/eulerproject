# 1 + 1/2 = 3/2 = 1.5
# 1 + 1/(2 + 1/2) = 7/5 = 1.4
# 1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
# 1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...
from fractions import Fraction
import sys
sys.setrecursionlimit(1201)

limit = 1000
n = 1
def sqrt2(count):
    if count == rec_limit:
        return Fraction(1, 2)
    count += 1
    return Fraction(1, (2 + sqrt2(count)))

found = 0

for i in range(7, limit + 1):

    rec_limit = i
    try:
        res = 1 + sqrt2(0)
    except RuntimeError:
        sys.exit()
    if len(str(res.numerator)) > len(str(res.denominator)):
        found += 1
        print("n = {0}".format(i))

print("Total of {0} fractions.".format(found))
