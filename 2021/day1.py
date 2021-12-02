import numpy as np

def readwords():
	with open('input/day1.txt') as f:
		for line in f.read().splitlines():
			yield int(line.strip())

inp = np.fromiter(readwords(), int)
increased = inp[1:] > inp[0:-1]
print(sum(increased))

# part two
sums = inp[0:-2] + inp[1:-1] + inp[2:]
increased = sums[1:] > sums[0:-1]
print(sum(increased))
