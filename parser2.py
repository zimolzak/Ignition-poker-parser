from pprint import pprint
input = open('example_ignition.txt').read()
hands = input.split('\n\n\n')

for i, h in enumerate(hands):
    segments = "seats preflop flop turn river".split()
    s = h.split('\n*** ')
    hands[i] = {}
    while len(s) > 1:
        # We don't always have flop, turn, riv, but last element is
        # always Summary.
        k = segments.pop(0)
        v = s.pop(0).splitlines()
        hands[i][k] = v
    hands[i]['summary'] = s.pop(0).splitlines()
    assert len(s) == 0

## [ { s:[] p:[] f:[] s:[] }  { s:[] p:[] f:[] t:[] r:[] s:[] }  {}  {} ]

print(hands[0])
