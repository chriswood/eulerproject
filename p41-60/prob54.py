

def read_hands(filename):
    with open(filename, 'r') as f:
        for hand in f:
            print(hand)

read_hands('../data/p054_poker.txt')
