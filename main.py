from ignition import HandList
from pprint import pprint

h = HandList('example_ignition.txt')
print(h)
print('VPIP = {}/{} = {}, over {} hands.'.format(h.pfcr_n, h.n,
                                                 h.vpip, h.n_hands))
print('PFR = {}/{} = {}, over {} hands.'.format(h.pfr_n, h.n,
                                                 h.pfr, h.n_hands))
print("Raised with:")
pprint(h.raise_cards)
print("Called with:")
pprint(h.call_cards)
print("Folded:")
pprint(h.fold_cards)
