# Find number of right/down paths through a 20x20 grid

# Total number of moves is 40 (20 right 20 down)
# If we know the number of ways the right move goes we have it,
# the down is the same
# So for 40 moves, how many ways can we put in 20 rigths

# 40C20
from math import factorial

def choose(a,b):
    '''implement choose notation'''
    return (factorial(a)/(factorial(b) * factorial(a - b)))

print(choose(40, 20))

