from collections import Counter

def read_hands(filename):
    with open(filename, 'r') as f:
        for hand in f:
            print(hand)

# read_hands('../data/p054_poker.txt')
test = '8S AS TD 3C JD 7C 7D 5C QD 7H'

class Hand:
    def __init__(self, cards):
        self.p1 = cards.split()
        self.classes = ['rf', 'sf', 'fk', 'fh', 'fl', 'st', 'tk', 'tp', 'op', 'hk']
        self.order = '23456789TJQKA'
        self.key1_card = None

    def display(self):
        print(self.p1)

    def classify(self):
        for fname in self.classes:
            f = getattr(self, fname)
            if f():
                return f.__name__

    def rf(self):
        match = sorted(set(self.order[-5:]))
        return (self.is_flush(self.p1) and
            sorted(set(''.join([x[0] for x in self.p1]))) == match)

    def sf(self):
        return self.is_straight(self.p1) and self.is_flush(self.p1)

    def fk(self):
        return self.is_pair(self.p1, 4)

    def fh(self):
        return self.is_pair(self.p1, 0, fh_check=True)

    def fl(self):
        if self.is_flush(self.p1):
            self.key1_card = self.high_card(self.p1)
            return True
        return False

    def st(self):
        if self.is_straight(self.p1):
            self.key1_card = self.high_card(self.p1)
            print(self.key1_card)
            return True
        return False

    def tk(self):
        return self.is_pair(self.p1, pair_count = 3)

    def tp(self):
        groups = Counter(x[0] for x in self.p1)
        res = groups.most_common()
        if res[0][1] == 2 and res[1][1] == 2:
            self.key1_card = (res[0][0], res[1][0])
            return True
        return False

    def op(self):
        return self.is_pair(self.p1, pair_count = 2)

    def hk(self):
        self.key1_card = self.high_card(self.p1)
        return True

    def high_card(self, cards):
        return max(cards, key=lambda x: self.order.index(x[0]))

    def is_pair(self, cards, pair_count, fh_check=False):
        # pair_count = 4 for 4 of a kind, etc...
        groups = Counter(x[0] for x in cards)
        res = groups.most_common()
        if fh_check:
            if len(res) == 2 and res[0][1] == 3:
                self.key1_card = (res[0][0], res[1][0])
                return True
        elif res[0][1] == pair_count:
            self.key1_card = res[0][0]
            return True
        return False

    def is_flush(self, cards):
        return len([x for x in cards if x[1] == cards[0][1]]) == len(cards)

    def is_straight(self, cards):
        start = self.lowest_card(cards)
        match = sorted(set(self.order[start:start + 5]))
        return match == sorted(set([x[0] for x in cards]))

    def lowest_card(self, cards):
        lowest = self.order.index(cards[0][0])
        for card in cards:
            pos = self.order.index(card[0])
            if pos < lowest:
                lowest = pos
        return lowest

def tie_breaker(h1, h2, t1, t2):
    return 1

# Classify hand 1
hand1 = Hand(test[:14])
hand1.display()
hand1_type = hand1.classify()
print("Hand 1 is a {0}.".format(hand1_type))

hand2 = Hand(test[14:])
hand2.display()
hand2_type = hand2.classify()
print("Hand 2 is a {0}.".format(hand2_type))

if hand1_type == hand2_type:
    winner = tie_breaker(hand1, hand2, hand1_type, hand2_type)
else:
    if hand1.classes.index(hand1_type) < hand2.classes.index(hand2_type):
        winner = 1
    else:
        winner = 2

print("The winner is hand {0}".format(winner))
