from common import ai
from math import sqrt, ceil, floor
from collections import Counter

inp = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""

def parse(inp):
    res = []
    for l in inp.strip().split("\n"):
        cards,bid = l.split()
        res.append((cards, int(bid)))
    return res

strength = "AKQJT98765432"
sd = dict([(k,i) for i,k in enumerate(reversed(strength))])

def score_p1(cards: str):
    # return tuple of (hand_type, s0, s1, s2, s3, s4, s5)
    ss = [sd[c] for c in cards]
    # hand_type is 7 thru 1
    c = Counter(cards)
    xs = tuple(sorted(c.values()))
    # print(xs)
    scores = {
        (5,):    7, # five of a kind
        (1, 4): 6, # four of a kind
        (2, 3): 5, # full house (3 and a pair)
        (1, 1, 3): 4, # three of a kind
        (1, 2, 2): 3, # two pair
        (1, 1, 1, 2): 2, # one pair
        (1, 1, 1, 1, 1): 1, # high card
    }
    return scores[xs], ss

ai(score_p1('AA8AA'), (6, [12, 12, 6, 12, 12]))
ai(score_p1('23432'), (3, [0, 1, 2, 1, 0]))

def p1(inp, scorefn):
    scored = [(scorefn(cards), cards, bid) for cards,bid in parse(inp)]
    t = 0
    for i, hand in enumerate(sorted(scored)):
        (score, cards, bid) = hand
        rank = i + 1
        print(f" {rank:8} {cards} {bid:5} {score}")
        t += rank*bid
    return t

ai(p1(inp, score_p1), 6440)
ai(p1(open("day7.txt").read(), score_p1), 254024898)

strength_p2 = "AKQT98765432J"
sd_p2 = dict([(k,i) for i,k in enumerate(reversed(strength_p2))])

def score_p2(cards: str):
    # return tuple of (hand_type, s0, s1, s2, s3, s4, s5)
    ss = [sd_p2[c] for c in cards]
    # hand_type is 7 thru 1
    c = Counter(cards)
    # remove the count of Jokers
    js = c['J']
    del c['J']
    print(f'{cards} => {js}')
    xs = tuple(sorted(c.values()))
    # print(xs)
    scores = {
        0: {
            (5,):    7, # five of a kind
            (1, 4): 6, # four of a kind
            (2, 3): 5, # full house (3 and a pair)
            (1, 1, 3): 4, # three of a kind
            (1, 2, 2): 3, # two pair
            (1, 1, 1, 2): 2, # one pair
            (1, 1, 1, 1, 1): 1, # high card
            },
        1: {
            (4,):    7, # five of a kind
            (1, 3): 6, # four of a kind
            (2, 2): 5, # full house (3 and a pair)
            (1, 1, 2): 4, # three of a kind
            (1, 1, 1, 1): 2, # one pair
        },
        2: {
            (3,):    7, # five of a kind
            (1, 2): 6, # four of a kind
            (1, 1, 1): 4, # three of a kind
            },
        3: {
            (2,):    7, # five of a kind
            (1, 1):  6, # four of a kind
            },
        4: {
            (1,):    7, # five of a kind
            },
        5: {
            ():    7,
           },
    }
    return scores[js][xs], ss

ai(score_p2('AA8AA'), (6, [12, 12, 7, 12, 12]))
ai(score_p2('23432'), (3, [1, 2, 3, 2, 1]))
ai(score_p2('JJJJJ'), (7, [0, 0, 0, 0, 0]))

ai(p1(inp, score_p2), 5905)
ai(p1(open("day7.txt").read(), score_p2), 254115617)
