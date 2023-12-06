from common import ai
from math import sqrt, ceil, floor

inp = """
Time:      7  15   30
Distance:  9  40  200
"""

def parse_p1(inp):
    res = []
    for l in inp.strip().split("\n"):
        a,ns = l.split(':')
        res.append(list(map(int, ns.strip().split())))
    assert len(res) == 2
    return res

def p1(inp):
    ts, ds = inp
    ways = 1
    for t,d in zip(ts, ds):
        print(f"race t {t} record d {d}")

        # known t,d  unknown time charging, tc
        # d = ts*speed   where ts=t-tc, speed=tc
        #   = (t-tc)*tc
        #   = t*tc - tc*tc
        # 0 = -1*tc^2 +t*tc -d
        # solve roots by quadratic eqn a=-1, b=t, c=-d, x=tc
        # tc = (-b +- sqrt(bb - 4ac)))/2a
        # tc = (-t +- sqrt(tt - 4*d))/-2
        # tc = (t +- sqrt(tt - 4d)) /2
        tc_p = (t + sqrt(t*t - 4*d))/2
        tc_m = (t - sqrt(t*t - 4*d))/2
        tc_m = ceil(tc_m)
        tc_p = floor(tc_p)
        print(f"tc={tc_m}  tc={tc_p}")

        # need to beat the record, not match it exactly.
        # nudge by 1 more towards max distance
        while tc_m * (t-tc_m) <= d:
            tc_m += 1
        while tc_p * (t-tc_p) <= d:
            tc_p -= 1
        print(f"after inequality adjustment {tc_m} - {tc_p}")
        ways = ways * (tc_p - tc_m + 1)
    return ways

ai(p1(parse_p1(inp)), 288)
ai(p1(parse_p1(open("day6.txt").read())), 1710720)

# stupid part2 parser without spaces
def parse_p2(inp):
    res = []
    for l in inp.strip().split("\n"):
        a,ns = l.split(':')
        ns = ns.replace(" ", "")
        res.append(list(map(int, ns.strip().split())))
    assert len(res) == 2
    return res

ai(p1(parse_p2(inp)), 71503)
ai(p1(parse_p2(open("day6.txt").read())), 35349468)
