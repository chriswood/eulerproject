
import math
from math import sqrt, ceil

def is_prime(N):
    if N in (1, 4):
        return False
    if N in (2, 3):
        return True
    last_value = math.ceil(sqrt(N))
    for n in range(2, int(last_value) + 1):
        if (N%n == 0):
            return False
    return True

def check(start):
    total = 0
    count = 0
    vals = []

    for i in range(start, len(primes)):
        new_total = total + primes[i]
        if new_total < limit:
            total = new_total
            count += 1
            vals.append(primes[i])
        else:
            break

    while not is_prime(total):
        vals = vals[:-1]
        count -= 1
        total = sum(vals)

    return count



limit = 10**6
primes = list(filter(is_prime, range(2, limit)))
lcount = 0
lvals = []
longest_total = 0
start = 3

while start < len(primes) and start < 10000:
    new_count = check(start)
    if new_count >= lcount:
        lcount = new_count
        lvals = primes[start:lcount+start]
        ltotal = sum(lvals)
        print("New high! count: {0} totaling: {1} from start: {2}".format(
            lcount, ltotal, start))
    start += 1;


print(lvals)
print("{0} values totaling {1}".format(lcount, ltotal))
