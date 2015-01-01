# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all
# of the numbers from 1 to 20?

def div_check(num):
	for n in range(20, 0, -1):
		if num%n is not 0:
			return False
	return True

# for 20, it must end in 0...
# just need to find lcm.

# 1 - Find prime factors of 1 - 20
# 2 - check for factors that occur multiple times in any number.
# 3 - for each of these, see how many times it occurs in each
# 4 - add the greatest number of this count to the final list
# 5 - add the rest of the numbers to the final list
# 6 - multiply these

# 1 - [1]
# 2 - [2]
# 3 - [3]
# 4 - [2, 2]
# 5 - [5]
# 6 - [2*3]
# 7 - [7]
# 8 - [2, 2, 2]
# 9 - [3, 3]
# 10 - [2, 5]
# 11 - [11]
# 12 - [2, 2, 3]
# 13 - [13]
# 14 - [2, 7]
# 15 - [3, 5]
# 16 - [2, 2, 2, 2]
# 17 - [17]
# 18 - [2, 3, 3]
# 19 - [19]
# 20 - [2, 2, 5]

# counts
counts = [(2, 4), (3, 2), (5, 1), (7, 1), (11, 1), (13, 1), (17, 1), (19, 1)]

total = 1
for prime, count in counts:
    total = total * (pow(prime, count)) # note not floating point pow

if div_check(total):
    print("total is true multiple: ", total)
