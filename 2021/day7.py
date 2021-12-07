import numpy as np
eg = "16,1,2,0,4,2,7,1,2,14"

def sim(eg, part2=False):
	pos = np.fromiter(eg.split(","), int)
	fuel = np.zeros(max(pos), int)
	for p in range(max(pos)):
		ns = np.abs(pos - p)
		if part2:
			ns = ns*(ns+1) / 2
		fuel[p] = np.sum(ns)
	print(np.sort(fuel)) # check for duplicates
	print("min fuel index {}".format(np.argmin(fuel)))
	print("min fuel {}".format(fuel[np.argmin(fuel)]))

sim(eg)
sim(open('input/day7.txt').read())
sim(eg, True)
sim(open('input/day7.txt').read(), True)
