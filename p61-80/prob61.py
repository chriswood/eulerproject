#Find the sum of the only ordered set of six cyclic 4-digit numbers
#for which each polygonal type: triangle, square, pentagonal,
#hexagonal, heptagonal, and octagonal, is represented by a
#different number in the set.

#need cyclical set of 6, 4 digit, numbers
#one is triangular, one is pentagonal, etc...

# First find sample problem
import sys
import math

def pentagonal(start=1):
    #p(27)=1080 gives first non-zero padding 4 digit
    n = start
    while True:
        yield int(n * (3*n - 1)/2)
        n += 1

def get_range(n):
    '''Given a 2 digit number, return list of
       start and end integers for all possible cyclical numbers'''
    start = n*100 + 10
    end = start + 90
    return start,end

class Figurate:
    def __init__(self):
        self.tri_set = set()
        self.square_set = set()
        self.hex_set = set()
        self.hept_set = set()
        self.oct_set = set()
        self.set_names = ['tri_set', 'square_set', 'hex_set',
                          'hept_set', 'oct_set']
        self.membership = {'tri_set': False, 'square_set': False, 'hex_set': False,
                           'hept_set': False, 'oct_set': False}
        self.candidates = []

    def _build_square_set(self):
        n = 32
        s = 0
        while s < 10000:
            s = pow(n,2)
            self.square_set.add(s)
            n += 1

    def _build_triangle_set(self):
        n = 45
        t = 0
        while t < 10000:
            t = n * (n + 1)/2
            self.tri_set.add(t)
            n += 1

    def _build_hexagonal_set(self):
        n = 23
        t = 0
        while t < 10000:
            t = n * (2 * n - 1)
            self.hex_set.add(t)
            n += 1

    def _build_heptagonal_set(self):
        n = 21
        t = 0
        while t < 10000:
            t = int(n * (5*n - 3)/2)
            self.hept_set.add(t)
            n += 1

    def _build_octagonal_set(self):
        n = 19
        t = 0
        while t < 10000:
            t = n * (3*n - 2)
            self.oct_set.add(t)
            n += 1

    def build_data(self):
        self._build_square_set()
        self._build_triangle_set()
        self._build_hexagonal_set()
        self._build_heptagonal_set()
        self._build_octagonal_set()

    def get_open_sets(self):
        return {k for k, v in self.membership.items() if not v}

    def check_range(self, n, sets=None):
        self.candidates.append(n)
        last_two = int(n%100)
        if last_two > 9:
            test_range = get_range(last_two)
            for i in range(test_range[0], test_range[1]):
                open_sets = sets if sets else self.set_names
                for s in open_sets:
                    result = i in getattr(self, s)
                    if result:
                        new_set_list = open_sets.copy()
                        new_set_list.remove(s)
                        if len(new_set_list) == 0:
                            if int(i%100) == math.floor(p/100):
                                self.candidates.append(i)
                                print("WINNNNNER", self.candidates)
                                print("sum is", sum(self.candidates))
                                sys.exit()
                            else:
                                continue
                        if not self.check_range(i, new_set_list):
                            continue
                        else:
                            return True
        self.candidates.remove(n)
        return False

my_f = Figurate()
my_f.build_data()

p_sieve = pentagonal(start=27)
p = next(p_sieve)
while p < 10000:
    my_f.check_range(p)
    p = next(p_sieve)
