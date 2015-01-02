
# Find the thirteen adjacent digits in the 1000-digit number that
# have the greatest product. What is the value of this product?

str_num = ''
with open('data8.txt', 'r') as f:
    for line in f:
        str_num += line
	str_num = str_num.strip("\n")
    print(str_num)
f.closed
