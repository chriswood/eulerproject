import sys
import math

def main():
    if len(sys.argv) <= 1:
        print("yer fergittin something")
    n = int(sys.argv[1])
    k = int(sys.argv[2])
    result = P(k, n)
    print('P({0}) = {1}'.format(n, result))
    
# for , we need p(2) + our new 111
def partition(n):
    if n < 3:
        print("recursion ended, n < 3")
        return n
    print("calling p({0})".format(n - 1))
    result = partition(n - 1) + 1 + find_odds(n)
    return(result)

# return the number of ways n can be summed in k non-zero terms, λ ⊢ n
# e.g. P(3,5) = 1 + 1 + 3 = 5, 2 + 2 + 1 = 5, = 2, 4+1+0, 3+2+0, 5+0+0
def P(k, n):
    if(k > n):
        return 0
    if(k == n):
        return 1
    return P(k+1, n) + P(k, n - k)




if __name__ == "__main__":
    main()