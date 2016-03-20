from math import ceil, sqrt

def gen():
    n = 3
    while True:
        yield n**2
        n = n + 2

def is_prime(x):
    # check short values
    if x in (1,4):
        return False
    if x in (2, 3):
        return True

    #get last value to test for even division into N
    last_value = ceil(sqrt(x))

    for n in range(2, int(last_value) + 1):
        if (x%n == 0):
            return False
    return True

step_gen = gen()
primes = 0
non_primes = 1 #1 starting at 3
skip = 2
prev_step = 1
found = False
size = 1
while not found:
    step = next(step_gen)
    new_diags = range(prev_step + skip, step + 1, skip)
    primes += len([x for x in new_diags if is_prime(x)])
    non_primes += len(new_diags)
    r = float(primes)/float(non_primes)
    if r < .1:
        print("size = {0}".format(skip + 1))
        break
    print("ratio is = {0}".format(r))
    prev_step = step
    skip += 2
