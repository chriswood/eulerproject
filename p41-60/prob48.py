# Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.

limit = 1000
total = 0
for i in range(1, limit + 1):
    total += pow(i, i)
    print("sum = {0}".format(total))
