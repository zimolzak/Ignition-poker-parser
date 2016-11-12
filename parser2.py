import re

class BettingRound:
    def __init__(self, lines):
        self.cards = []
        self.actions = []
        _round_name_re = re.compile(r"^([A-Z ]+) \*\*\*.*$")
        _street_cards_re = re.compile(r".*\[(.*)\].*")
        # hits only last [Kh] construct because 1st * is greedy.
        _hole_cards_re = re.compile(r".*Card dealt to a spot \[(.*)\]")
        match = _round_name_re.match(lines[0])
        self.round_name = match.group(1)
        if '[' in lines[0]:
            # only for flop/turn/riv
            match = _street_cards_re.match(lines[0])
            self.cards = match.group(1).split()
        for L in lines[1:]:
            if 'Card dealt to a spot' in L:
                assert not '[' in lines[0] # assert not flop/turn/riv
                match = _hole_cards_re.match(L)
                self.cards.append(match.group(1).split()) # list of lists
            elif ('Seat sit down' in L
                  or 'Table deposit' in L
                  or 'Seat stand' in L
                  or 'Table enter user' in L
                  or 'Table leave user' in L):
                continue
            elif ' : ' in L:
                self.actions.append(L)
            else:
                print('*** unhandled line:' + L)
    def __repr__(self):
        return str(self.__dict__)

class Hand:
    def __init__(self, string):
        segments = "seats preflop flop turn river".split()
        _hand_num_re = re.compile(r"^Ignition Hand #(\d+) .*$")
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
            ## step 3: split each segment into lines
            v = s.pop(0).splitlines()
            if k in "preflop flop turn river".split():
                self.__dict__[k] = BettingRound(v)
            else:
                self.__dict__[k] = v
        self.summary = s.pop(0).splitlines()
        assert len(s) == 0
        ## step 4: parse various elements at sub-line level
        match = _hand_num_re.match(self.seats[0])
        self.hand_number = int(match.group(1))
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
