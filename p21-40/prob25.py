#What is the first term in the Fibonacci sequence to contain 1000 digits?
from itertools import count

n1 = 1
n2 = 1
limit = 1000

for i in count(3):
    next = n1 + n2
    n2 = n1
    n1 = next
    if len(str(next)) >= limit:
        print("Done. ", next)
        break


    
    


