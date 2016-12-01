import itertools
def eggnog(litres, cartons):
	for num in range(1, len(cartons)):
		for cb in itertools.combinations(cartons, num):
			if sum(cb) == litres:
				yield cb
print list(eggnog(25, (20, 15, 10, 5, 5) ))

ls = list(eggnog(150, (50, 44, 11, 49, 42, 46, 18, 32, 26, 40, 21, 7, 18, 43, 10, 47, 36, 24, 22, 40) ))
print(len(ls))
minsz = min(map(len, ls))
print len([i for i in ls if len(i) == minsz])
