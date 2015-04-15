from itertools import permutations

def gen_is_pandigital(n, r):
    """ Generalized version of pandigital function.
        Still can't start with 0 """
    n = str(n)

    compa = "".join([str(i) for i in range(r)])
    compb = "".join(sorted(n))

    return compa == compb

def check(num):
    checkset = [2, 3, 5, 7, 11, 13, 17]
    for i in range(1, 8):
        me = num[i:i + 3]
        if int(me) % checkset[i - 1] != 0:
            return False
    return True

base = '0123456789'
found = []
# permutations sorts lexicographicaly, so 0's will be first and can be skipped
for v in permutations(base):
    if v[0] is not '0':
        nstr = "".join(v)

        if check(nstr):
            print("Found: ", nstr)
            found.append(int(nstr))

print(found)
print(sum(found))

#check('1406357289')
