import sys

def pentagonal():
    n = 1
    while True:
        yield n * (3*n - 1)/2
        n += 1

def is_pentagonal(n):
    if n > pents[-1]:
        print("Error: {0} too large for pentagonal list.".format(n))
        sys.exit(0)
    return n in pents

# build list in memory
limit = 5000
pents = []
results = []
f = pentagonal()

for n in range(2 * limit + 1):
    pents.append(next(f))

for i in range(limit):
    print("x = {0}".format(pents[i]))
    for j in range(1200):
        x = pents[i]
        y = pents[j]
        if is_pentagonal(x + y):
            if (((x > y) and is_pentagonal(x - y)) or
               ((y > x) and is_pentagonal(y - x))):
                results.append((x, y))
                print("FOUNDDDDDDDDDDDDDDDDD ONE")
                print("{0},{1} is a plus".format(x,y))
print(results)
