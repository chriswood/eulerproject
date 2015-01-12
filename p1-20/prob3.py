# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

import math
import itertools

def is_prime(N):
    '''
    Check a number N and see if it is divisible by anything less than
    its square root evenly.
    '''
    # check quick values
    if N in (1, 4):
        return False
    if N in (2, 3):
        return True

    #get last value to test for even division into N
    last_value = math.ceil(math.sqrt(N))

    for n in xrange(2, int(last_value) + 1):
        if (N%n == 0):
            return False
    return True

def find_multiple(start, end):
    if((end - start) < 1):
        return

    for n in itertools.count(start):
        if n >= number:
            break
        elif number % n == 0: #true
            factor1 = n #
            factor2 = number/n #
            print("factor1 %i" %factor1)
            print("factor2 %i" %factor2)
            if is_prime(factor1): #
                pfactors.append(factor1)
            else:
                if(math.ceil(math.sqrt(number)) - factor1 < 1):
                    break
                find_multiple(factor1 + 1, factor2 - 1)

number = 600851475143
pfactors = []
find_multiple(2, number)
print(pfactors)
