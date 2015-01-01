# The sum of the squares of the first ten natural numbers is,

# 1^2 + 2^2 + ... + 10^2 = 385

# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 552 = 3025

# Hence the difference between the sum of the squares of the
# first ten natural numbers and the square of the sum is
#

# Find the difference between the sum of the squares of the first
# one hundred natural numbers and the square of the sum.

diff = pow(sum(range(1, 101)), 2) - sum(map(lambda x:x*x, range(1, 101)))
print("difference: ", diff)
