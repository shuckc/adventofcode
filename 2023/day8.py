from common import ai
import re
import itertools
from collections import defaultdict
import math

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
			m = re.match(r'([\w]*) = \(([\w]*), ([\w]*)\)', l)
			if m is None:
				raise ValueError(l)
			p = m.groups()
			stages[p[0]] = p[1:]
	return steps, stages


def p1_getplayers(stages):
	return ['AAA'], set(['ZZZ'])

def solve(inp, getplayers):
	steps, stages = parse(inp)
	players, terminals = getplayers(stages)
	print(steps)
	print(stages)
	print(f"players={players}, terminals={terminals}")
	for i, step in enumerate(itertools.cycle(steps)):
		for pi in range(len(players)):
			current = players[pi]
			if i < 100:
				print(f" {i:5} {pi:5} {current} -> {step}  -- {stages[current]}")
			idx = {'L': 0, 'R': 1}[step]
			current = stages[current][idx]
			players[pi] = current

		if set(players) <= terminals:
			#print(set(players))
			#print(set(terminals))
			break
	return 1+i

ai(solve(inp, p1_getplayers), 2)
inp2 = """
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""
ai(solve(inp2, p1_getplayers), 6)
ai(solve(open("day8.txt").read(), p1_getplayers), 19667)

inp_p2 = """
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
"""

def p2_getplayers(stages):
	players = [k for k in stages.keys() if k[-1] == "A"]
	terminals = [k for k in stages.keys() if k[-1] == "Z"]
	return players, set(terminals)

ai(solve(inp_p2, p2_getplayers), 6)
# not close to finishing by brute force...
# ai(solve(open("day8.txt").read(), p2_getplayers), 6)

def cycle_solve(inp):
	steps, stages = parse(inp)
	players, terminals = p2_getplayers(stages)
	print(f"players={players}, terminals={terminals}")

	players_cycle_len = [0] * len(players)
	player_done_recording = {} # empty -> False -> True
	players_term_squares = defaultdict(set)
	for i, step in enumerate(itertools.cycle(steps)):
		for pi in range(len(players)):
			print(f" {i:5} {pi:5} {players[pi]} -> {step}  -- {stages[players[pi]]}")
			idx = {'L': 0, 'R': 1}[step]
			players[pi] = stages[players[pi]][idx]
			if players[pi] in terminals:
				if players[pi] not in players_term_squares[pi]:
					player_done_recording[pi] = False # start Z->Z
				else:
					player_done_recording[pi] = True # finish
				players_term_squares[pi].add(players[pi])

			if player_done_recording.get(pi, None) == False:
				players_cycle_len[pi] += 1

		if len(player_done_recording) == len(players) and all(player_done_recording.values()):
			break
	# checks
	print(players_cycle_len)
	print(players_term_squares)
	return math.lcm(*players_cycle_len)

ai(cycle_solve(inp_p2), 6)
# cycle lengths Z->Z [2,3] and only one termination square each
# {0: {'11Z'}, 1: {'22Z'}})

ai(cycle_solve(open("day8.txt").read()), 19185263738117)
# cycle lengths [16343, 16897, 21883, 20221, 19667, 13019]
# only 1 Z check
# {5: {'SGZ'}, 0: {'BSZ'}, 1: {'NVZ'}, 4: {'ZZZ'}, 3: {'VKZ'}, 2: {'KRZ'}})
# lcm 19185263738117
