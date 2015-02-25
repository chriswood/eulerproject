#Find the sum of all numbers that can be written as 5th powers of their digits.
limit = 200000
power = 5

print(sum(n for n in range(2, limit) if n == sum(pow(int(digit), power) \
    for digit in str(n))))
