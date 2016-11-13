from ignition import HandList

hands = HandList('example_ignition.txt')

pfr = 0
n = 0

print(hands)

for x in hands.hand_list:
#    print(x.hand_number)
#    print('----')
#    for a in x.preflop.actions:
#        if '[ME]' in a:
#            print(a)
    [p, ac] = x.pf_raises_actions()
    pfr += p
    n += ac
#    print()

print('VPIP = {}/{} = {}, over {} hands.'.format(pfr, n, float(pfr) / n,
                                                 len(hands.hand_list)))
