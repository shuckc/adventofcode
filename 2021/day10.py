import numpy as np

eg = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
"""

pairs = "[],(),{},<>".split(",")
closer_for = dict([p for p in pairs])
scores = {")": 3, "]": 57, "}": 1197, ">": 25137}
p2sd = {")": 1, "]": 2,"}": 3, ">": 4}

def part1(eg):
	score = 0
	p2scores = []
	for l in eg.strip().split("\n"):
		closers = []
		print(l)
		for p in l:
			# print("{} {}".format(closers, p))
			if p in "[({<":
				closers.append(closer_for[p])
			elif p == closers[-1]:
				closers.pop()
			else:
				print("corrupt! expected {} but found {} instead".format(closers[-1], p))
				score += scores[p]
				break
		else:
			print("loop reached end, closers: {}".format("".join(reversed(closers))))
			p2s = 0
			for c in reversed(closers):
				p2s = 5*p2s + p2sd[c]
			p2scores.append(p2s)
	print("p1 score {}".format(score))
	p2scores.sort()
	print(p2scores)
	print("p2 middle score {}".format(p2scores[len(p2scores)//2]))

part1(eg)

with open('input/day10.txt') as f:
	part1(f.read())
