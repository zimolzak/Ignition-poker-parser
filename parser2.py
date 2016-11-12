from ignition import Hand

## main
## step 1: split flat file into hands
input = open('example_ignition.txt').read()
hands = input.split('Ignition ')
empty = hands.pop(0) # remove 1st always empty el
assert empty == ''
for i, h in enumerate(hands):
    hands[i] = Hand(h)

## reporting

for x in hands:
    print(x.hand_number)
    print('----')
    for a in x.preflop.actions:
        if '[ME]' in a:
            print(a)
    print()
