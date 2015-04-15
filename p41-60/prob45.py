def hexagonal():
    n = 1
    while True:
        yield n * (2*n - 1)
        n += 1

def pentagonal():
    n = 1
    while True:
        yield n * (3*n - 1)/2
        n += 1

def exp_pent_check(i):
    """expand pentagonal list to i, and return membership"""
    pent = next(p)
    while pent < i:
        pent_list.append(pent)
    

def is_pentagonal(n):
    if n in pent_list:
        return True
    if n > pent_list[-1]:
        return exp_pent_check(n)

pent_list = [1]
f = hexagonal()
p = pentagonal()

while True:
    h = next(f)
    if is_pentagonal(h) and is_triangle(h):
        print("Found! {0}".format(h))
