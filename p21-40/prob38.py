
def is_pandigital(n):
    """ can't start with 0 """
    return all(['0' not in n, len(n) == 9, len(set(n)) == 9])

def ccat(alist):
    return ''.join([str(i) for i in alist])

x_limit = 10000
n = 2
ms = range(1, n+1)
greatest_so_far = 0
g_int = 0
#gen = permutations(digits)
for x in range(1, x_limit):
    res = ccat([x*y for y in ms])
    print(res)
    if is_pandigital(res) and int(res) > greatest_so_far:
        print("found larger! {0}".format(res))
        greatest_so_far = int(res)
        g_int = x

print("greatest so far {0}, from n={1} and x={2}".format(greatest_so_far, n, g_int))

# For y = (1,2,3,4,5,6) no results
#range must be (1,2,3,4,5) or smaller
#greatest so far 327654981, from n=3 and x=327
#greatest so far 918273645, from n=5 and x=9
#greatest so far 932718654, from n=2 and x=9327
