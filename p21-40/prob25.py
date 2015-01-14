
#    F1 = 1
#    F2 = 1
#    F3 = 2
#    F4 = 3
#    F5 = 5
#    F6 = 8
#    F7 = 13
#    F8 = 21
#    F9 = 34
#    F10 = 55
#    F11 = 89
#    F12 = 144

#The 12th term, F12, is the first term to contain three digits.

#What is the first term in the Fibonacci sequence to contain 1000 digits?
from itertools import count

n1 = 1
n2 = 1
limit = 1000

for i in count(3):
    next = n1 + n2
    n2 = n1
    n1 = next
    print(i, "th term is ", next, sep='')
    if len(str(next)) >= limit:
        print("Done. ", next)
        break


    
    


