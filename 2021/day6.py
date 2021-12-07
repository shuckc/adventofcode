import numpy as np
eg = "3,4,3,1,2"

def sim(eg, count=80):
	ages = np.fromiter(eg.split(","), int)
	print("initial: {}".format(ages))
	for i in range(count):
		ages = ages - 1
		reset = ages == -1
		ages[reset] = 6
		ages = np.append(ages, 8*np.ones(np.sum(reset), int))
		print("after day: {} {}".format(i, ages))
	print(ages.size)

def optim(eg, count=80):
	# extra input to ensure normalised grid in ages
	ages = np.fromiter((eg + ',0,1,2,3,4,5,6,7,8').split(","), int)
	ages,counts = np.unique(ages, return_counts=True)
	counts = counts - 1 # remove extras
	print("initial:     {} {}".format(counts, ages))
	for i in range(count):
		e = counts[0]
		counts = np.roll(counts, -1)
		counts[6] += e # parents
		counts[8] = e # children
		print("after day {}: {} @ {}".format(i, counts, ages))
	print(sum(counts))

#sim(eg)
#sim(open('input/day6.txt').read())
optim(eg,count=80)
optim(eg,count=256)
optim(open('input/day6.txt').read(),count=256)
