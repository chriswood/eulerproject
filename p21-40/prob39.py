
#
# If p is the perimeter of a right angle triangle with integral length sides,
#  {a,b,c}, there are exactly three solutions for p = 120.
#
# {20,48,52}, {24,45,51}, {30,40,50}
#
# For which value of p ≤ 1000, is the number of solutions maximised?
from math import sqrt
from time import time

t = time()
p = 120
# a+b+c=p
max_p = 0
max_s = 0
for p in range(3, 1001):
    solutions = 0
    for a in range(1, p-2):
        for b in range(a, p - a + 1):
            c = sqrt(a**2 + b**2)
            if c.is_integer() and a + b + c == p:
                solutions += 1
    if solutions > max_s:
        max_p = p
        max_s = solutions
        print("p={0} has {1} solutions.".format(p, solutions))

print("********************")
print("max p is {0} with {1} solutions.".format(max_p, max_s))
print("time is {0}".format(time() - t))
