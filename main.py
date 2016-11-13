from ignition import HandList

hands = HandList('example_ignition.txt')
print(hands)
hands.compute_vpip()
print('VPIP = {}/{} = {}, over {} hands.'.format(hands.pfcr_n, hands.n,
                                                 hands.vpip, hands.n_hands))
print('PFR = {}/{} = {}, over {} hands.'.format(hands.pfr_n, hands.n,
                                                 hands.pfr, hands.n_hands))
