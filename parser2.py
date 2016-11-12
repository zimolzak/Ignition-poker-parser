from pprint import pprint
input = open('example_ignition.txt').read()
hands = input.split('\n\n\n')

class Hand:
    def __init__(self, se=None, p=None, f=None, t=None, r=None, su=None):
        self.seats = se
        self.preflop = p
        self.flop = f
        self.turn = t
        self.river = r
        self.summary = su
    def __repr__(self):
        return str(self.__dict__)

for i, h in enumerate(hands):
    segments = "seats preflop flop turn river".split()
    s = h.split('\n*** ')
    hands[i] = Hand()
    while len(s) > 1:
        # We don't always have flop, turn, riv, but last element is
        # always Summary.
        k = segments.pop(0)
        v = s.pop(0).splitlines()
        hands[i].__dict__[k] = v
    hands[i].summary = s.pop(0).splitlines()
    assert len(s) == 0

## [ { s:[] p:[] f:[] s:[] }  { s:[] p:[] f:[] t:[] r:[] s:[] }  {}  {} ]

print(hands[0])
