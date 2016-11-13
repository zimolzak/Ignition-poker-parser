import re

class BettingRound:
    def __init__(self, lines):
        self.cards = []
        self.actions = []
        _round_name_re = re.compile(r"^([A-Z ]+) \*\*\*.*$")
        _street_cards_re = re.compile(r".*\[(.*)\].*")
        # "street" hits only last [Kh] construct because 1st * is greedy.
        _hole_cards_re = re.compile(r".*Card dealt to a spot \[(.*)\]")
        assert ('HOLE' in lines[0]
                or 'FLOP' in lines[0]
                or 'TURN' in lines[0]
                or 'RIVER' in lines[0] )
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
                print('*** unhandled line ' + self.round_name +
                      str(lines.index(L)) + ':' + L )
        ### Tally hero's preflop raises, calls, and all actions.
        if self.round_name == 'HOLE CARDS':
            self.raise_n = 0
            self.call_n = 0
            self.action_n = 0
            for a in self.actions:
                if '[ME]' in a:
                    self.action_n += 1
                    if 'Raises' in a:
                        self.raise_n += 1
                    if 'Calls' in a:
                        self.call_n += 1
    def __repr__(self):
        return str(self.__dict__)

class Hand:
    def __init__(self, string):
        _hand_num_re = re.compile(r"^Hand #(\d+) .*$")
        self.seats = None
        self.preflop = None
        self.flop = None
        self.turn = None
        self.river = None
        self.summary = None
        ## step 2: split each hand into segments
        s = string.split('\n*** ')
        while s:
            # Not known whether flop, turn, riv, or summary is in
            # there.
            ## step 3: split each segment into lines
            v = s.pop(0).splitlines()
            if 'Hand #' in v[0]:
                self.seats = v
            elif 'HOLE' in v[0]:
                self.preflop = BettingRound(v)
            elif 'FLOP' in v[0]:
                self.flop = BettingRound(v)
            elif 'TURN' in v[0]:
                self.turn = BettingRound(v)
            elif 'RIVER' in v[0]:
                self.river = BettingRound(v)
            elif 'SUMMARY' in v[0]:
                self.summary = v
            else:
                assert False
        assert len(s) == 0
        ## step 4: parse various elements at sub-line level
        match = _hand_num_re.match(self.seats[0])
        self.hand_number = int(match.group(1))
    def __repr__(self):
        return str(self.__dict__)

class HandList:
    def __init__(self, filename):
        input = open(filename).read()
        hands_raw = input.split('Ignition ')
        self.hand_list = []
        empty = hands_raw.pop(0) # remove 1st always empty element
        assert empty == ''
        for h in hands_raw:
            self.hand_list.append(Hand(h))
    def __repr__(self):
        R = ''
        for x in self.hand_list:
            R += str(x.hand_number) + '\n----\n'
            for a in x.preflop.actions:
                if '[ME]' in a:
                    R += (a + '\n')
            R += '\n'
        return R
    def compute_vpip(self):
        ### fixme - could legitimately become part of __init__
        self.pfcr_n = 0
        self.pfr_n = 0
        self.n = 0
        for x in self.hand_list:
            self.pfcr_n += (x.preflop.call_n + x.preflop.raise_n)
            self.pfr_n += x.preflop.raise_n
            self.n += x.preflop.action_n
        self.n_hands = len(self.hand_list)
        self.vpip = float(self.pfcr_n) / self.n
        self.pfr = float(self.pfr_n) / self.n
