import numpy as np

DIR = dict([(x,np.array(y)) for (x,y) in [('forward', (0,1)), ('down', (1,0)), ('up', (-1,0))]])
eg = "forward 5\ndown 5\nforward 8\nup 3\ndown 8\nforward 2\n"

def part1(steps):
	pos = np.array([0,0])
	for line in steps.splitlines():
		#print(line)
		d,n = line.split()
		pos += DIR[d] * int(n)
	return pos[0] * pos[1]

print(part1(eg))

with open('input/day2.txt') as f:
	print(part1(f.read()))

def part2(steps):
	aim = np.array([0,1])
	pos = np.array([0,0])
	for line in steps.splitlines():
		d,n = line.split()
		aim[0] += DIR[d][0] * int(n)
		pos += DIR[d][1] * int(n) * aim
	return pos[0] * pos[1]

print(part2(eg))

with open('input/day2.txt') as f:
	print(part2(f.read()))
