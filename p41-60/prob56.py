from itertools import product

limit = 100
longest = 0
la = 0
lb = 0

def isum(n):
    return sum(int(i) for i in str(n))

for a, b in product(range(limit), repeat=2):
    print(a, "^", b)
    res = isum(pow(a, b))
    if res > longest:
        longest = res
        la = a
        lb = b
        print("NEW LONGEST: {0} sum with a = {1}, b = {2}".format(longest, la, lb))


print("Final: {0} sum with a = {1}, b = {2}".format(longest, la, lb))
