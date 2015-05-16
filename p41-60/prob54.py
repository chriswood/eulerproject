

def read_hands(filename):
    with open(filename, 'r') as f:
        for hand in f:
            print(hand)

# read_hands('../data/p054_poker.txt')
test = 'AS TS QS JS KS 7C 8C 5C QD 6C'

class Hand:
    def __init__(self, cards):
        self.p1 = cards.split()[:5]
        self.p2 = cards.split()[5:]
        self.classes = ['rf', 'sf', 'fk']
        self.order = '23456789TJQKA'

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
        return False

    def fk(self):
        return True

    def is_flush(self, suits):
        # takes string of suits
        return True

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
