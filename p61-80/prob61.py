#Find the sum of the only ordered set of six cyclic 4-digit numbers
#for which each polygonal type: triangle, square, pentagonal,
#hexagonal, heptagonal, and octagonal, is represented by a
#different number in the set.

#need cyclical set of 6, 4 digit, numbers
#one is triangular, one is pentagonal, etc...

# First find sample problem
import sys

def pentagonal(start=1):
    #p(27)=1080 gives first non-zero padding 4 digit
    n = start
    while True:
        yield n * (3*n - 1)/2
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

    def display(self):
        print(self.membership)

    def clear_membership(self):
        for key in self.membership:
            self.membership[key] = False

my_f = Figurate()
my_f.build_data()

p_sieve = pentagonal(start=27)
p = next(p_sieve)
while p < 1081: #1080
    tri_member = False
    square_member = False
    last_two = int(p%100) #80
    if(last_two > 9):
        test_range = get_range(last_two)
        #check every set for this range
        for i in range(test_range[0], test_range[1]):
            my_f.clear_membership()
            for shape in my_f.set_names:
                shape_set = getattr(my_f, shape)
                test = i in shape_set
                my_f.membership[shape] = test
                # if test:
                #     print("found something!!!!!!!!!")
                #     print("p = %d, i = %d" % (p, i))
                #     sys.exit()
            print("p = %d, i = %d" % (p, i))
            my_f.display()
            my_f.clear_membership()


        # 1080 -> search other sets for something starting with 80. If found, check that
        # box and go search for the next thing. Otherwise, return
        #8010,8011,8012,... check for triangle or square
    p = next(p_sieve)
