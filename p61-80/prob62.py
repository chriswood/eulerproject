from itertools import permutations, count
from collections import Counter

digit_len = 8
c = Counter()

def dr_match(n):
    i = sum(int(i) for i in str(n))
    while i > 9:
        i = sum(int(x) for x in str(i))
    return i in [1,8,9]

def is_cube(n):
    a = round(n**(1/3))
    if pow(a, 3) == n:
        return True
    return False

def store(n):
    j = int(''.join(sorted(str(n))))
    if j == 12334556789:
        print("n=",n)
        print(pow(n,(1/3)))
    c.update({n:1})


for i in range(4642,10000):
    n = pow(i, 3)
    if is_cube(n):
        store(n)
        if c.most_common()[0][1] == 5:
            print("here it is",i)
            break


print(c.most_common()[0])
