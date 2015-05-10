
from math import factorial

def choose(n, r):
    return factorial(n)/(factorial(r) * factorial(n - r))

limit = 10**6
count = 0

for n in range(23, 101):
    print("n = ", n)
    for r in range(n, 0, -1):
        if choose(n, r) > limit:
            count += 1;

print("count: ", count)
