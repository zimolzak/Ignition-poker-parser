from ignition import Hand, filename2hands

hands = filename2hands('example_ignition.txt')

## reporting

for x in hands:
    print(x.hand_number)
    print('----')
    for a in x.preflop.actions:
        if '[ME]' in a:
            print(a)
    print()
