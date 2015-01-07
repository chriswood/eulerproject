# Find longest number of terms in Collatz sequence for n < 1000000.

# n = n/2 for even n
# n = 3n + 1 for odd n

# Using the rule above and starting with 13, we generate the following sequence:

def collatz(n):
    '''return next term in collatz sequence'''
    if n%2 == 0: # even
        return n/2
    else: # false
        return (3*n + 1)

limit = 1000000
hi_term_count = 0
hi_term = 0
for start in xrange(2, limit):
    print("Term: %i" %start)
    term_list = [start]
    next = collatz(start)
    while next != 1:
        term_list.append(next)
        next = collatz(next)
    new_len = len(term_list) + 1

    if new_len > hi_term_count:
        hi_term_count = new_len
        hi_term = start
        print("Found new high!! ", hi_term_count)

print("Highest number of terms: ", hi_term_count, "from ", hi_term)

