from __future__ import unicode_literals, absolute_import, division, print_function

import re
from decimal import Decimal

#    _split_re = re.compile(r"Dealing |\nDealing Cards\n|Taking |Moving |\n")
#    _blinds_re = re.compile(r"^Blinds are now \$([\d.]*) / \$([\d.]*)$")
#    _hero_re = re.compile(r"^\[(. .)\]\[(. .)\] to (?P<hero_name>.*)$")
_seat_re = re.compile(r"^Seat (\d\d?): (.*) \(\$([\d.]*) in chips\) ?(.*)$")
#    _sizes_re = re.compile(r"^Pot sizes: \$([\d.]*)$")
#    _card_re = re.compile(r"\[(. .)\]")
#    _rake_re = re.compile(r"Rake of \$([\d.]*) from pot \d$")
#    _win_re = re.compile(r"^(.*) wins \$([\d.]*) with: ")

class Player:
    def __init__(self, name, stack, seat):
        self.name = name
        self.stack = stack
        self.seat = seat

def parse_players(list_of_lines):
    players = [None] * 10
    for line in list_of_lines[1:]:
        match = _seat_re.match(line)
        if not match:
            print('no ' + line)
            break
        seat_number = int(match.group(1))
        n = match.group(2)
        st = Decimal(match.group(3))
        se = seat_number
        players[seat_number - 1] = Player(name=n, stack=st, seat=seat_number)
    max_players = seat_number
    players = players[:max_players]
    return players

if __name__ == '__main__':
    input = open('/Users/ajz/Desktop/example_ignition.txt').read().splitlines()
    
    P = parse_players(input)

    for plyr in P:
        if not plyr:
            continue
        print(' '.join([plyr.name, str(plyr.stack), str(plyr.seat)]))
