from common import ai
import re
import itertools
from collections import defaultdict
import math

inp = """
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""
def parse(inp):
	for l in inp.strip().split("\n"):
		yield list(map(int, l.split(" ")))

def deltas(row):
	return [r2-r1 for r1,r2 in zip(row[:-1], row[1:])]

ai(deltas([0,3,6,9]), [3, 3, 3])

def p1(inp):
	t, t2 = 0, 0
	for seq in parse(inp):
		print(seq)
		dd = seq
		lasts = []
		firsts = []
		while True:
			lasts.append(dd[-1])
			firsts.append(dd[0])
			dd = deltas(dd)
			print(f"   {dd}")
			if all([d == 0 for d in dd]):
				nxt = sum(lasts)
				prev = firsts[-1]
				# p = f0 - (f1 - f2)
				for f in reversed(firsts[:-1]):
					prev = f - prev
				print(f" {lasts} {firsts} next {nxt} prev {prev}")
				t += nxt
				t2 += prev
				break
	return t, t2

ai(p1(inp), (114, 2))
ai(p1(open("day9.txt").read()), (2038472161, 1091))
