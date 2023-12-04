# p1 method
# numbers only run horizontally
# find locations of all symbols - point x,y
# then examine each point in 8 directions including diagonals from symbols, if a number,
# add to solution. each number only included once, so put x,y of first digit with the value as total
# then sum values
import string
from common import ai
from collections import defaultdict

inp = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

def grid_1d(inp):
    ls = inp.strip().split('\n')
    c = len(ls[0])
    ws = ''.join(ls)
    r = len(ws)//c
    assert len(ws) == r*c
    return r,c,ws

def rowcol_1d(r,c,pos):
    return pos//r, pos%c

def neighbours_1d(r, c, pos):
    pos_r, pos_c = rowcol_1d(r,c,pos)
    #      N  NE  E  SE  S  SW  W  NW
    # dr  -1  -1  0  +1 +1  +1  0  -1
    # dc   0  +1 +1  +1  0  -1 -1  -1
    for dr,dc,direction in [(-1,0,'N'), (-1,+1,'NE'), (0,+1,'E'), (+1,+1,'SE'), (+1,0,'S'), (+1,-1,'SW'), (0,-1,'W'), (-1,-1,'NW')]:
        if 0 <= pos_c+dc < c and 0 <= pos_r+dr < r:
            p = pos_c+dc + c*(pos_r+dr)
            yield direction, p

def iter_parts(inp):
    r,c,ws = grid_1d(inp)
    symbols = dict([(i,c) for i,c in enumerate(ws) if c not in '0123456789.'])
    for sym,s in symbols.items():
        sr, sc = rowcol_1d(r,c,sym)
        print(f"{sym} col={sc} row={sr}")
        for direction, p in neighbours_1d(r, c, sym):
            pr, pc = rowcol_1d(r,c,p)
            print(f"checking {direction} at {pc} {pr} => index {p} is {ws[p]}")
            if ws[p] in string.digits:
                # now find first digit of this number by reducing col until
                # no longer a digit or col=0
                prevdigitcol = pc-1
                while prevdigitcol >= 0:
                    p2 = c*pr + prevdigitcol
                    print(f'  checking digit at {p2} col {prevdigitcol} is {ws[p2]}')
                    if ws[p2] not in string.digits:
                        break
                    prevdigitcol -= 1
                print(f'firstdigit at row {pr} col {prevdigitcol+1}')
                nextdigitcol = pc+1
                while nextdigitcol < c:
                    p2 = c*pr + nextdigitcol
                    print(f'  checking digit at {p2} col {nextdigitcol} is {ws[p2]}')
                    if ws[p2] not in string.digits:
                        break
                    nextdigitcol += 1
                part_pos = c*pr+prevdigitcol+1
                digits = int(ws[part_pos:c*pr+nextdigitcol])
                print(f"digits at {part_pos} are {digits}")
                yield sym,s,part_pos,digits

def p1(inp):
    parts = {}
    for sym, s, part_pos, digits in iter_parts(inp):
        parts[part_pos] = digits
    return sum(parts.values())

ai(p1(inp), 4361)
ai(p1(open("day3.txt").read()), 528819)

def p2(inp):
    digits_around_gears = defaultdict(dict)
    for sympos, s, part_pos, digits in iter_parts(inp):
        if s != '*':
            continue
        digits_around_gears[sympos][part_pos] = digits
    gears = []
    for sympos, sym_parts in digits_around_gears.items():
        if len(sym_parts) == 2:
            v0, v1 = sym_parts.values()
            print(f"gear {v0} {v1} product {v0*v1}")
            gears.append(v0*v1)
    return sum(gears)

ai(p2(inp), 467835)
ai(p2(open("day3.txt").read()), 80403602)
