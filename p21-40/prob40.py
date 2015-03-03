
def test(n):
    d = ''
    count = 0
    while len(d) <= n:
        d = d + str(count)
        count += 1

    return([d[1], d[10], d[100], d[1000], d[10000], d[100000], d[1000000]])

res = test(1000000)
print(res)
