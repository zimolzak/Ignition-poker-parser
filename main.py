from ignition import HandList

hands = HandList('example_ignition.txt')
print(hands)
hands.compute_vpip()
print('VPIP = {}/{} = {}, over {} hands.'.format(hands.pfr, hands.n,
                                                 hands.vpip, hands.n_hands))
