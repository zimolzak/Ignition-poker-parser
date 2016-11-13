from ignition import HandList
from pprint import pprint
from sys import argv

## usage: python main.py example_ignition.txt

h = HandList(argv[1])
print(h)
print('VPIP = {}/{} = {}, over {} hands.'.format(h.pfcr_n, h.n,
                                                 h.vpip, h.n_hands))
print('PFR = {}/{} = {}, over {} hands.'.format(h.pfr_n, h.n,
                                                 h.pfr, h.n_hands))
for key, handlist in h.hero_range.items():
    print(key + ':')
    pprint(handlist)
