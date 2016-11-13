from ignition import HandList

h = HandList('example_ignition.txt')
print(h)
h.compute_vpip()
print('VPIP = {}/{} = {}, over {} hands.'.format(h.pfcr_n, h.n,
                                                 h.vpip, h.n_hands))
print('PFR = {}/{} = {}, over {} hands.'.format(h.pfr_n, h.n,
                                                 h.pfr, h.n_hands))
