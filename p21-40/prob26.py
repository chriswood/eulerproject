
# factor x into m and n, where m is an terminating number previously calculated
# and n is a repeating number previously calculated
# periodic part of x is periodic part of n
#
# So just need to check prime numbers
#
#  The multiplicative order of 10 mod an integer n relatively prime to 10 gives
#  the period of the decimal expansion of the reciprocal of n
#  . For example, the haupt-exponent of 10 (mod 13) is 6, and
# 1/(13)=0.076923
from decimal import Decimal, getcontext, setcontext, Context

class DecSearch:
    """Handle searching a floating point number for repeating patterns."""
    def __init__(self, limit, search_string):
        """limit is length of number to search.
           chunk is how much to break the search up by.
           e.g. chunk 3 means search the string in chunks of thirds
        """
        setcontext(Context(prec=100))
        self.limit = limit
        self.s = search_string

    def unit(self, j):
        return (Decimal(1)/Decimal(j))

    def interval_log(self, a, b, c):
        print("start = {0}, stop={1}".format(a, b))
        print("searching {0} to {1}".format(self.s[a:b], self.s[b:c]))

    def match_log(self, a, b, c):
        print("{0} equals {1}".format(self.s[a:b], self.s[b:c]))

    def run(self, interval):
        for i in range(0, self.limit, interval):
            if i + 2 * interval > self.limit:
                print("no match found.")
                break
            a, b, c = i, i + interval, i + interval + interval
            self.interval_log(a, b, c)
            if self.s[a:b] == self.s[b:c]:
                print("found match")
                self.match_log(a, b, c)
                break

    def make_sure(self):
        """Check several more times for match"""
        pass

test = '7862459287364978692435'
print("test string is {0}.".format(test))
print("Length: {0}".format(len(test)))
search = DecSearch(10, test)
search.run(2)

#search(3)
