# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
#
# 43 44 45 46 47 48 49
# 42 21 22 23 24 25 26
# 41 20  7  8  9 10 27
# 40 19  6  1  2 11 28
# 39 18  5  4  3 12 29
# 38 17 16 15 14 13 30
# 37 36 35 34 33 32 31
# It can be verified that the sum of the numbers on the diagonals is 101.
#
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
# formed in the same way?


# s = [range(1, end1 + 1, step1), range(end1 + step2, end2 + 1, step1 * 2),
# range(end2 + step3, end3 + 1, step1 * 2 * 2)]
size = 1001
diags = [1]
skip = 2
prev_step = 1
for step in [x**2 for x in range(3, size + 1, 2)]:
    diags.extend(range(prev_step + skip, step + 1, skip))
    prev_step = step
    skip += 2

print(sum(diags))



# 1,3,5,7,9,13,17,21,25,31,37,43,49,57,65
