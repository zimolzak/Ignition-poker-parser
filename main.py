from ignition import Hand, filename2hands

hands = filename2hands('example_ignition.txt')

## reporting

pfr = 0
n = 0

for x in hands:
    print(x.hand_number)
    print('----')
    for a in x.preflop.actions:
        if '[ME]' in a:
            print(a)
    [p, ac] = x.pf_raises_actions()
    pfr += p
    n += ac
    print()

print('VPIP = {}/{} = {}, over {} hands.'.format(pfr, n, float(pfr) / n,
                                                 len(hands)))
