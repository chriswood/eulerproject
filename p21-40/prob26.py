
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
    def __init__(self, number, limit, log, mn, mp, md):
        """limit is length of number to search.
           number is the decimal to check
        """
        setcontext(Context(prec=limit + 1))
        self.limit = limit
        self.number = number
        self.s = str(Decimal(1)/Decimal(number))[2:]
        self.whole = len(self.s) < self.limit
        self.log = log
        self.max_number = mn
        self.max_period = mp
        self.max_digits = md

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
                break
            a, b, c = i, i + interval, i + interval + interval
            #self.interval_log(a, b, c)
            if self.s[a:b] == self.s[b:c] and self.make_sure(c, interval):
                self.match_log(a, b, c)
                self.log.append({'number': self.number,
                                 'period': interval,
                                 'digits': self.s[a:b]})
                return True
        return False

    def make_sure(self, c, interval):
        """Check several more times for match"""
        for i in range(c, 3*interval, interval):
            if not self.s[i:i + interval] == self.s[i + interval:i + 2 * interval]:
                print(self.s[i:i + interval])
                print("***")
                print(self.s[i + interval:i + 2 * interval])
                import sys
                sys.exit(1)
        return True

test = 7
log = []
limit = 100000
chunk_limit = 10000
mn = 0
mp = 0
md = ''
for x in range(1, 1001):
    search = DecSearch(x, limit, log, mn, mp, md)
    if not search.whole:
        count = 5
        while not search.run(count) and count <= chunk_limit:
            count += 1
    else:
        log.append({'number': x, 'period': 0})
