#What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

from itertools import permutations

cutoff = 10**6
for index, p in enumerate(permutations(range(10)), 1):
    if index >= cutoff:
        print(index, "th is ", p)
        break


