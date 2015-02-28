#
#
# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
#
# Find the sum of all numbers, less than one million, which are palindromic
# in base 10 and base 2.
#
# (Please note that the palindromic number, in either base, may not include
# leading zeros.)
from math import ceil
from time import time

def is_palindrone(num):
    snum = str(num)
    num_len = len(snum)
    for index, c in enumerate(snum, start=1):
        if not (c == snum[num_len - index] or
                index > ceil(float(num_len)/2.0)):
            return False
    return True

t = time()
limit = 10**6
both = []
for i in range(1, limit):
    if i % 10 == 0:
        continue
    if is_palindrone(i) and is_palindrone(bin(i)[2:]):
        print("found one! {0}, {1}".format(i, bin(i)[2:]))
        both.append(i)

print("time is {0}".format(time() - t))
print(sum(both))
