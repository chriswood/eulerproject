# Working clockwise, and starting from the group of three with the 
# numerically lowest external node 
# Total   Solution Set
# 9   4,2,3; 5,3,1; 6,1,2
# 9   4,3,2; 6,2,1; 5,1,3
# 10  2,3,5; 4,5,1; 6,1,3
# 10  2,5,3; 6,3,1; 4,1,5
# 11  1,4,6; 3,6,2; 5,2,4
# 11  1,6,4; 5,4,2; 3,2,6
# 12  1,5,6; 2,6,4; 3,4,5
# 12  1,6,5; 3,5,4; 2,4,6
#  the maximum string for a 3-gon ring is 432621513.
# What is the maximum 16-digit string for a "magic" 5-gon ring?

# first devise a test for a correct solution
# each group of n digits should add up to the same number
# zeroes are always part of a ten
#first number of first group should be lower than first number of other groups
import sys
from string import digits
from itertools import zip_longest, permutations
from collections import Counter
import pprint

polygon_size = 3
line_size = 3
d = digits[1:7] #test
ans_size = 6

#TODO deal with 10

def grouper(iterable, n):
    args = [iter(iterable)] * n
    print(list(args[0]))
    return zip(*args)

def test(s):
    '''n = size of polygon
       -16 digits,  10,9,8,7,6,5,4,3,2,1
       -each group of 3 must add up to the same thing
       -each digit may only be used once in the graph, therefore 
            no more than twice in the number, and only twice in certain spots
       -the first digit must be the lowest of any first digit of the sets of three
       abc,dce,feg,hgi,jib'''
    #print("testing {0} with digits {1}".format(n, d))
    #s = str(n)
    #ns = grouper(s, line_size)
    #for 16 digits there must be one 10, and it can't be in position  of repeat
    #test 1 - sums
    for i in range(0, ans_size + 1, line_size):
        a = sum(map(int, s[i:i + line_size]))
        if i == 0:
            first = a    
        if a is not first:
            #print("sums don't check out")
            return False

    #test 2 - right counts of digits
    tcount = Counter(s)
    if len(tcount) is not ans_size:
        #print("wrong number of digits")
        return False
    #test 3 - each number used only twice at the most
    if tcount.most_common(1)[0][1] > 2:
        #print("too many {0}'s".format(tcount.most_common(1)[0][0]))
        return False
    # for 6 digits, abcdcefeb
    # for 16,  abc,dce,feg,hgi,jib 
    position_tests = [s[4] == s[2], s[7] == s[5], s[8] == s[1]]
    if not all(position_tests):
        #print("positions wrong, JACKASS")
        return False

    return True

def arrange(s):
    #123456
    return s[:4] + s[2] + s[4] + s[5] + s[4] + s[1]


perms = permutations('123456')
for p in perms:
    s = ''.join(p)
    ring_f = arrange(s)
    if test(ring_f):
        print("found one!!!", ring_f)

# for each permutation of 123456,
# check with the specific order
# for 123456
# 123435652

# we could list all initial sets of 3 that add up to a certain sum, then check those
