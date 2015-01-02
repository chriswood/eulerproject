
# Find the thirteen adjacent digits in the 1000-digit number that
# have the greatest product. What is the value of this product?

str_num = ''
with open('data8.txt', 'r') as f:
    for line in f:
        str_num += line
    str_num = "".join(str_num.split('\n'))
f.closed

lproduct = 0
num_len = 1000
test_len = 13
for n in range(num_len + 1 - test_len):
    test = str_num[n:n+test_len]

    #no need to test if zeroes
    if test.find('0') < 0:
        product = 1
        for i in test:
            product = product * int(i)
        lproduct = product if (product > lproduct) else lproduct

print("largest product is ", lproduct)
