# Find Lychrel numbers below 10000
from math import ceil

iter_limit = 10000
step_limit = 50
found = 0

def reverse(i):
    k = list(str(i))
    k.reverse()
    return int(''.join(k))

def is_palindrone(num):
    snum = str(num)
    num_len = len(snum)
    for index, c in enumerate(snum, start=1):
        if not (c == snum[num_len - index] or
                index > ceil(float(num_len)/2.0)):
            return False
    return True

def is_lychrel(i):
    iters = 1
    test = i + reverse(i)
    while iters < iter_limit:
        if is_palindrone(test):
            return False
        else:
            test = test + reverse(test)
            iters += 1
    print("Found one!".format(i))
    return True

for n in range(1, iter_limit):
    if is_lychrel(n):
        found += 1

print("Found {0} Lychrel numbers between 1 and {1}".format(found, iter_limit))
