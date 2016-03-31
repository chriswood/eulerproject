# How many n-digit positive integers exist which are also an nth power?
from itertools import count
n = 3
total = 0
for n in count(1):
    subtotal = 0
    print("__________________________________________________")
    for i in range(1, 10):
        t = pow(i, n)
        if len(str(t)) == n:
            total += 1
            subtotal += 1
            print("{0} = {1} ^ {2}".format(t, i, n))

    print("Total for n =", n, "is", subtotal)
    if subtotal == 0:
        break

print("Final total is", total)
