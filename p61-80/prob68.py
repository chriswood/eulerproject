
# What is the maximum 16-digit string for a "magic" 5-gon ring?


import sys
from string import digits
from itertools import permutations
from time import time

polygon_size = 3
line_size = 3
ans_size = 15

def test(s):
    '''n = size of polygon
       -16 digits,  10,9,8,7,6,5,4,3,2,1
       -each group of 3 must add up to the same thing
       abc,dce,feg,hgi,jib'''
    for i in range(0, ans_size, line_size):
        a = sum(map(int, s[i:i + line_size]))
        if i == 0:
            first = a
        if a is not first:
            return False
    return True

def arrange(s):
    #return s[:4] + s[2] + s[4] + s[5] + s[4] + s[1]
    #abc,dce,feg,hgi,jib
    # 12345678910
    # 123,435,657,879,1092
    return s[:4] + [s[2], s[4], s[5], s[4], s[6], s[7], s[6], s[8], s[9], s[8], s[1]]



t1 = time()
terms = [i for i in digits[1:]] + ['10']
perms = permutations(terms)
solutions = []

def order(n):
    '''1) group by threes
       2) find highest end node
       3) rearrange clockwise from there'''
    grouped = [n[i:i + 3] for i in range(0, 13, 3)]
    end_nodes = [int(i[0]) for i in grouped]
    start = end_nodes.index(min(end_nodes))
    new_list = grouped[start:] + grouped[:start]
    new_list_f = []
    for group in new_list:
        for number in group:
            new_list_f.append(number)
    return ''.join(new_list_f)

for p in perms:
    ring_f = arrange(list(p))
    if test(ring_f):
        solutions.append(ring_f)


print("finding max......")
m = [order(x) for x in solutions]
print(max(m))

print("time is {0}".format(time() - t1))


