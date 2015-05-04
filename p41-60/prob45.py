

def hexagonal():
    n = 144 #skip the first example 40755
    while True:
        yield n * (2*n - 1)
        n += 1

def pentagonal():
    n = 2
    while True:
        yield n * (3*n - 1)/2
        n += 1

def triangle():
    n = 2
    while True:
        yield n * (n + 1)/2
        n += 1

def exp_pent_check():
    """expand pentagonal list to i, and return membership"""
    for i in range(chunk):
        pent_list.append(next(p))

def exp_tri_check(n):
    big_enough = False
    while not big_enough:
        end = tri_list[-1]
        if end < n:
            for i in range(chunk):
                tri_list.append(next(t))
        else:
            big_enough = True

def is_pentagonal(n):
    if n > pent_list[-1]:
        print("expanding pents for n = {0}".format(n))
        exp_pent_check()
    return n in pent_list

def is_triangle(n):
    if n > tri_list[-1]:
        print("expanding tri for n = {0}".format(n))
        exp_tri_check(n)
    return n in tri_list


chunk = 1000
pent_list = [1]
tri_list = [1]
f = hexagonal()
p = pentagonal()
t = triangle()

while True:
    h = next(f)
    if is_pentagonal(h) and is_triangle(h):
        print("Found! {0}".format(h))
        break
