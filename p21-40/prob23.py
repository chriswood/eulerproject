

#A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

#A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

#As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

#Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

# Find lowest abundant numbers, such that a + b < limit
# First find abundant numbers < limit
# check oven at 14:10

from math import ceil

limit = 28123
start = 3
abundants = set()

def is_abundant(n):
    stop = ceil(float(n)/2.0);
    return sum(filter(lambda x: n % x == 0, range(1, stop + 1))) > n

def build_abundant_set():
    for n in range(start, limit):
        if is_abundant(n):
            abundants.add(n)

def check(n1):
    print("checking: ", n1)
    for n2 in filter(lambda x: x >= n1, abundants):
        s = n1 + n2
        if s > limit:
            continue
        try:
            possibles.remove(s)
        except KeyError:
            pass

with open('../data/prob20_ab_set.txt') as f:
    abundants = f.read()
    abundants = abundants.replace(' ', '').strip('\n{}').split(',')
    abundants = [int(x) for x in abundants]

possibles = set(range(limit + 1))

# remove all possible sums of abundants from possibles
for n in abundants:
    check(n)
        
print(possibles)
print(len(possibles))
print(sum(possibles))



