# What is the value of the first triangle number to have
# over five hundred divisors?

from itertools import count
from math import sqrt, ceil
from useful import is_prime
from collections import Counter

# too slow :(
def count_divisors(num):
    return len(filter(lambda x:num % x == 0, range(1, num + 1)))

def prime_factors(num):
    '''
    List prime factors as often as they occur
    '''
    if is_prime(num): #end condition
        plist.append(num)
        return
    end = int(ceil(float(num)/2.0))
    for n in range(2, end+1):
        if num % n == 0:
            if is_prime(n):
                plist.append(n)
            factor2 = num/n
            if is_prime(factor2):
                plist.append(factor2)
            else:
                prime_factors(factor2)
            #stop loop from continuing upon recursion
            break 

number = 27

tnum = 0
for n in range(1,8):
    plist = []
    tnum += n #new make triange :)
    print "The %ith triangle number is: " %n, tnum
    prime_factors(tnum) #stored in plist
    print(plist)


#('The 3905th triangle number is: ', 7626465)
#('Divisors: ', 96)
#('The 3906th triangle number is: ', 7630371)
#('Divisors: ', 24)
#('The 3907th triangle number is: ', 7634278)

