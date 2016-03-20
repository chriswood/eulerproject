from math import pow

class Decay:
    def __init__(self, hl, N0=0):
        '''h1 = halflife
           N0 = initial amount present'''
        self.hl = hl
        self.N0 = N0
        self.amount = 0

    def take_dose(self, dose):
        self.amount += dose

    def get_amount_present(self, t):
        return self.amount * pow(2, -t/self.hl)
    
    def plot(resolution):
        pass

myd = Decay(37)
myd.take_dose(12)
me = myd.get_amount_present(37)
print(me)
print("taking another dose")
myd.take_dose(12)
