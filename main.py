from ignition import HandList
from pprint import pprint

h = HandList('example_ignition.txt')
print(h)
print('VPIP = {}/{} = {}, over {} hands.'.format(h.pfcr_n, h.n,
                                                 h.vpip, h.n_hands))
print('PFR = {}/{} = {}, over {} hands.'.format(h.pfr_n, h.n,
                                                 h.pfr, h.n_hands))
for key, handlist in h.hero_range.items():
    print(key + ':')
    pprint(handlist)
