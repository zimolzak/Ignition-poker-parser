from pprint import pprint

class Hand:
    def __init__(self, string):
        segments = "seats preflop flop turn river".split()
        self.seats = None
        self.preflop = None
        self.flop = None
        self.turn = None
        self.river = None
        self.summary = None
        ## step 2: split each hand into segments
        s = string.split('\n*** ')
        while len(s) > 1:
            # We don't always have flop, turn, riv, but last element is
            # always Summary.
            k = segments.pop(0)
            v = s.pop(0).splitlines()
            self.__dict__[k] = v
        ## step 3: split each segment into lines
        self.summary = s.pop(0).splitlines()
        assert len(s) == 0
    def __repr__(self):
        return str(self.__dict__)


## main

input = open('example_ignition.txt').read()

## step 1: split flat file into hands
hands = input.split('\n\n\n')

for i, h in enumerate(hands):
    hands[i] = Hand(h)

## [ { s:[] p:[] f:[] s:[] }  { s:[] p:[] f:[] t:[] r:[] s:[] }  {}  {} ]

print(hands[0])
