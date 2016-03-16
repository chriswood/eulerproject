from collections import Counter
import sys

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
        if self.is_straight(self.p1) and self.is_flush(self.p1):
            self.key1_card = self.high_card(self.p1)
            return True
        return False

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
                self.key1_card = res[0][0]
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


def tie_breaker(h1, h2, hand_type):
    if hand_type in ['sf', 'fk', 'fh', 'st', 'tk']:
        # just compare one key card
        return 1 if h1.order.index(h1.key1_card[0]) > \
                    h2.order.index(h2.key1_card[0]) else 2
    elif hand_type in ['fl', 'hk']:
        #run  down list
        cards1 = h1.p1
        cards2 = h2.p1
        key1 = h1.high_card(cards1)
        key2 = h2.high_card(cards2)
        while h1.order.index(key1[0]) == h2.order.index(key2[0]):
            cards1.remove(max(cards1, key=lambda x: h1.order.index(x[0])))
            cards2.remove(max(cards2, key=lambda x: h2.order.index(x[0])))
            key1 = h1.high_card(cards1)
            key2 = h2.high_card(cards2)
        return 1 if h1.order.index(key1[0]) > h2.order.index(key2[0]) else 2
    else: #tp, op
        key1 = h1.key1_card
        key2 = h2.key1_card
        print("key1 = {0}, key2 = {1}".format(key1, key2))
        if hand_type == 'op':
            if h1.order.index(key1[0]) == h2.order.index(key2[0]):
                cards1 = list(filter(lambda x: x[0] != key1[0], h1.p1))
                cards2 = list(filter(lambda x: x[0] != key1[0], h2.p1))
                key1 = h1.high_card(cards1)
                key2 = h2.high_card(cards2)
                while h1.order.index(key1[0]) == h2.order.index(key2[0]):
                    print("cards1 = {0}".format(cards1))
                    cards1.remove(max(cards1, key=lambda x: h1.order.index(x[0])))
                    cards2.remove(max(cards2, key=lambda x: h2.order.index(x[0])))
                    key1 = h1.high_card(cards1)
                    key2 = h2.high_card(cards2)
                return 1 if h1.order.index(key1[0]) > h2.order.index(key2[0]) else 2
            else:
                return 1 if h1.order.index(key1[0]) > \
                            h2.order.index(key2[0]) else 2

def read_hands(filename):
    wins = 0
    with open(filename, 'r') as f:
        for cardline in f:
            winner = process(cardline)
            if winner == 1:
                wins += 1
    print("Hand 1 won {0} times.".format(wins))

def process(cardline):
    hand1 = Hand(cardline[:14])
    hand1.display()
    hand1_type = hand1.classify()

    hand2 = Hand(cardline[14:])
    hand2.display()
    hand2_type = hand2.classify()

    if hand1_type == hand2_type:
        winner = tie_breaker(hand1, hand2, hand1_type)
    else:
        if hand1.classes.index(hand1_type) < hand2.classes.index(hand2_type):
            winner = 1
        else:
            winner = 2

    print("The winner is hand {0}".format(winner))
    return winner

read_hands('../data/p054_poker.txt')
#test = '8S AS TD 3C JD 7C 7D 5C QD 7H'
