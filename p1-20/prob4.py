
# Find the largest palindrome made from the product of two 3-digit numbers.

# need to test for a palindrome
import math
from itertools import repeat
import sys

def is_palindrone(num):
    snum = str(num)
    num_len = len(snum)
    for index, c in enumerate(snum, start=1):
        if not (c == snum[num_len - index] or
                index > math.ceil(float(num_len)/2.0)):
            return False
    return True

# largest number is 999*999
start = 999
found = False
largest = 0

for i in range(start, 0, -1):
    for n in zip(repeat(i), range(start, 0, -1)):
        print(n)
        product = n[0] * n[1]
        if is_palindrone(product):
            print("FOUND one... %i" %product)
            if product > largest:
                largest = product

print("largest = %i" %largest)

# for products in map(lambda x:(x, x*x, x*(x-1)), range(mult1, 0, -1)):
#     n = products[0]
#     print(n)
#     print(n-1)
#     print(n*n)
#     print(n*(n-1))
#     if is_palindrone(products[1]):
#         print("FOUND!!!! %i" %products[1])
#         break
#     elif is_palindrone(products[2]):
#         print("FOUND!!!! %i" %products[2])
#         break
