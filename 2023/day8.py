from common import ai
import re
import itertools

inp = """
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
"""

def parse(inp):
	stages = {}
	for i, l in enumerate(inp.strip().split("\n")):
		if i == 0:
			steps = list(l)
		if i > 1:
			m = re.match(r'([A-Z]*) = \(([A-Z]*), ([A-Z]*)\)', l)
			p = m.groups()
			stages[p[0]] = p[1:]
	return steps, stages

def solve(inp):
	steps, stages = parse(inp)
	print(steps)
	print(stages)
	current = 'AAA'
	for i, step in enumerate(itertools.cycle(steps)):
		print(f" {i:5} {current} -> {step}  -- {stages[current]}")
		idx = {'L': 0, 'R': 1}[step]
		current = stages[current][idx]
		if current == 'ZZZ':
			break
	return 1+i

ai(solve(inp), 2)
inp2 = """
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""
ai(solve(inp2), 6)
ai(solve(open("day8.txt").read()), 6)

