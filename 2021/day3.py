import numpy as np
import operator

eg="00100\n11110\n10110\n10111\n10101\n01111\n00111\n11100\n10000\n11001\n00010\n01010"

# turns out np.packbits is garbage in little endian, it packs the least significant
# end of the array, rather than MSB

def inp(eg):
	inp = np.fromiter(eg.replace('\n', ''), int)
	n = len(eg.split('\n')[0])
	return inp.reshape([-1,n])

def part1(inp):
	b = (sum(inp) / inp.shape[0]) > 0.5
	gamma = b.dot(2**np.arange(b.shape[0]-1,-1,-1))
	epsilon = np.invert(b).dot(2**np.arange(b.shape[0]-1,-1,-1))
	print("gamma={} epsilon={} result={}".format(gamma, epsilon, gamma*epsilon))

part1(inp(eg))
part1(inp(open('input/day3.txt').read()))

def part2(inputk):
	def chk(inp, op):
		for i in range(inp.shape[0]):
			b = op((sum(inp) / inp.shape[0]), 0.5)
			inp = inp[inp[:,i] == b[i]]
			if inp.shape[0] == 1:
				return inp[0]

	b = chk(inputk, operator.ge)
	oxygen = b.dot(2**np.arange(b.shape[0]-1,-1,-1))
	c = chk(inputk, operator.lt)
	co2 = c.dot(2**np.arange(c.shape[0]-1,-1,-1))
	print("oxygen={} co2={} result={}".format(oxygen, co2, oxygen*co2))

part2(inp(eg))
part2(inp(open('input/day3.txt').read()))
