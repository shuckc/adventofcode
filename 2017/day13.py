
inp="""0: 3
1: 2
4: 4
6: 4"""

def parse(inp):
	cs = [map(int, i.split(': ')) for i in inp.split('\n')]
	cols = max(cs, key=lambda x: x[0])[0] + 1
	heights = [0 for i in range(cols)]
	for c in cs:
		heights[c[0]] = c[1]
	
	print(heights)
	for delay in range(200000000):
		severity = game(heights, delay=delay)
		# print('delay {} severity {}'.format(delay, severity))
		if severity == 0:
			print('delay {} severity {}'.format(delay, severity))
			return delay

def game(heights, delay):
	cols = len(heights)
	severity = 0
	collision = False
	time = 0
	while (time - delay) < cols:
		#print(scanners)
		position = time - delay
		# print(position)
		collision = position >= 0 and heights[position] > 0 and (time % (2*heights[position] - 2)) == 0
		if collision:
			# print('Caught on position {}'.format(position))
			severity = severity + 1 + position * heights[position]
			return severity

		time = time + 1

	#print('severity {}'.format(severity))
	return severity

parse(inp)

with open('input/day13.txt') as f:
	parse(f.read().strip())


