from collections import Counter

def read_hands(filename):
    with open(filename, 'r') as f:
        for hand in f:
            print(hand)

# read_hands('../data/p054_poker.txt')
test = '8S JC 7S 9H TD 7C 8C 5C QD 6C'

class Hand:
    def __init__(self, cards):
        self.p1 = cards.split()[:5]
        self.p2 = cards.split()[5:]
        self.classes = ['rf', 'sf', 'fk', 'fh', 'fl', 'st']
        self.order = '23456789TJQKA'
        self.key1_card = None

    def display(self):
        print(self.p1)

    def sort_hand(self):
        pass

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



hand = Hand(test)
hand.display()
hand_type = hand.classify()
print(hand_type)

    # High Card: Highest value card.
    # One Pair: Two cards of the same value.
    # Two Pairs: Two different pairs.
    # Three of a Kind: Three cards of the same value.
    # Straight: All cards are consecutive values.
    # Flush: All cards of the same suit.
    # Full House: Three of a kind and a pair.
    # Four of a Kind: Four cards of the same value.
    # Straight Flush: All cards are consecutive values of same suit.
    # Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
