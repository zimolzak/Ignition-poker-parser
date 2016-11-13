Ignition Poker parser
========

Parse a hand history file from Ignition Casino into Python objects.
I'm trying to parse it directly, not convert to intermediate and use
one of the parsers for other sites' formats. Also trying to do so
without many external modules.

Ignition has anonymous players, so my main focus is on tracking stats,
patterns, ranges, areas for improvement on *myself*.

Usage: `python main.py hand_history_file.txt`

Hand history files tend to be located/named like

    /Applications/IgnitionCasino.app/Contents/MacOS/Hand\ History/12345678/
    HH20161106-170102\ -\ 1234567\ -\ RING\ -\ \$0.02-\$0.05\ -\ HOLDEM\ -\ NL\ -\ TBL\ No.12345678.txt

And have contents like

    Ignition Hand #1234567890 TBL#12345678 HOLDEM No Limit - 2016-11-06 17:01:02
    Seat 1: Big Blind [ME] ($4.98 in chips)
    Seat 4: Dealer ($5.02 in chips)
    Dealer : Set dealer [4]
    Dealer : Small Blind $0.02
    Table deposit $1.50
    Table enter user
    Big Blind  [ME] : Big blind $0.05
    *** HOLE CARDS ***
    Big Blind  [ME] : Card dealt to a spot [7s Jd]
    Dealer : Card dealt to a spot [9d Kd]
    Dealer : Calls $0.03
    Seat sit down
    Big Blind  [ME] : Raises $0.05 to $0.10
    Table deposit $1.50
    Dealer : Calls $0.05
    *** FLOP *** [8h 7h 7d]
    Big Blind  [ME] : Checks

...*et cetera.*

Example output
--------

    ['Jh', '4h'] (#3381295466)
    Big Blind  [ME] : Checks

    ['7d', 'Jc'] (#3381295659)
    Small Blind  [ME] : Folds

    ['Td', '6s'] (#3381295996)
    Dealer  [ME] : Folds

    ['3s', 'Jc'] (#3381296511)
    UTG+4  [ME] : Folds

    ['7s', 'As'] (#3381296817)
    UTG+3  [ME] : Raises $0.25 to $0.25

    ['Th', '9h'] (#3381297248)
    UTG+1  [ME] : Raises $0.15 to $0.15
    UTG+1  [ME] : Calls $0.15

    ['As', '3h'] (#3381297552)
    UTG+1  [ME] : Folds


    VPIP = 3/8 = 0.375, over 7 hands.
    PFR = 2/8 = 0.25, over 7 hands.
    Call:
    []
    Raise:
    [['7s', 'As'], ['Th', '9h']]
    Fold:
    [['7d', 'Jc'], ['Td', '6s'], ['3s', 'Jc'], ['As', '3h']]
