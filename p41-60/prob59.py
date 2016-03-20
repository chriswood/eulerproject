
import itertools

class Cipher:
    def __init__(self, cipher):
        self.cipher = cipher
        self.transposed = []
        self.translated = []

    def xor(self, keys):
        self.transposed.clear()
        keygen = itertools.cycle(keys)
        for letter in self.cipher:
            self.transposed.append(letter ^ ord(next(keygen)))

    def translate(self):
        self.translated = [chr(x) for x in self.transposed]

    def display(self):
        print(''.join(self.translated))

    def addc(self):
        print(sum([ord(x) for x in self.translated]))

filename = '../data/p059_cipher.txt'
with open(filename, 'r') as f:
    c = f.readline().rstrip("\n").split(',')
    cipher = [int(x) for x in c]

pt = Cipher(cipher)
pt.xor('god')
pt.translate()
pt.display()
pt.addc()
