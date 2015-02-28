# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial
# of their digits.

from math import factorial

def check(n):
    return n == sum(factorial(int(i)) for i in str(n))

found = []
for i in range(3, 9999999):
    if check(i):
        print("found one! {0}".format(i))
        found.append(i)
