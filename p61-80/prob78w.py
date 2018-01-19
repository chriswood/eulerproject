import sys
import math

def main():
    if len(sys.argv) <= 1:
        print("yer fergittin something")
    n = int(sys.argv[1])
    end  = math.ceil(n/2)

    #for i in range(n, end, -1):
    result = partition(n)
    print('P({0}) = {1}'.format(n, result))
    
# for , we need p(2) + our new 111
def partition(n):
    if n < 3:
        print("recursion ended, n < 3")
        return n
    print("calling p({0})".format(n - 1))
    result = partition(n - 1) + 1 + find_odds(n)
    return(result)

# given n, find any groupings that are not included in the P(n-1), 1 grouping
# todo generalize to P(n-1), step
def find_odds(n):
    return 0

def factori

if __name__ == "__main__":
    main()