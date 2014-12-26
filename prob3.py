# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

# find 2 multiples.
#     is first prime?
#         yes -> save
#         no -> repeat process with this number
#     is second prime?
#         yes -> save, quit
#      no -> repeat process with this number

# number = 61
# pfactors = []
# if number % 2 == 0:
#     pfactors.append(2)
#     ptest(2, number/2)
# elif number % 3

number = 1169
pfactors = []

def termGenerator(start):
    # Already tested 2, so no need to test multiples of it
    # TODO weed out multiples of 5 after a pretest
    for i in range(start, number, 2):
        yield i


def findMultiple(start):
    termGenObj = termGenerator(start)
    for n in termGenObj:
        if number % n == 0:
            multiple = n
            print("Found a multiple %i" %multiple)
            if isPrime(multiple):
                pfactors.append(multiple)
            else:
                start = n
                findMultiple(n)
