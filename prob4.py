
# Find the largest palindrome made from the product of two 3-digit numbers.

# need to test for a palindrome
import math

def is_palindrone(num):
    snum = str(num)
    num_len = len(snum)
    for index, c in enumerate(snum):
        if not (c == snum[num_len - index - 1] or
                index > math.ceil(float(num_len)/2.0)):
            return False
    return True

test = 80121108
print(is_palindrone(test))
