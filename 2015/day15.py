# Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
# Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
sc = ( [-1, -2, 6, 3], [2, 3, -2, -1] )
cal = (8, 3)

def scoreRecipie(amts, sc): # [1,99]
	assert sum(amts) == 100
	parts = len(sc[0])
	part = [0]*parts  # [0,0,0,0]
	for i, amt in enumerate(amts):
		for pi in range(parts):
			part[pi] += amt*sc[i][pi]
	score = 1
	for x in map(lambda x: max(0,x), part):
		score *= x
	return score

def gen2():
	for x0 in range(99):
		yield x0, 100-x0

def check(gen, types, scores, cal):
	best = 0
	for amts in gen():
		if sum( [ i*j for i,j in zip(amts, cal) ]) != 500: continue
		score = scoreRecipie(amts, scores)
		if score > best:
			print '{0} -> {1}'.format( ', '.join(['{} {}'.format(*b) for b in zip(types, amts)]), score)
			best = score

check(gen2, ('Butterscotch', 'Cinnamon'), sc, cal)

#Sprinkles: capacity 5, durability -1, flavor 0, texture 0, calories 5
#PeanutButter: capacity -1, durability 3, flavor 0, texture 0, calories 1
#Frosting: capacity 0, durability -1, flavor 4, texture 0, calories 6
#Sugar: capacity -1, durability 0, flavor 0, texture 2, calories 8
sc = ( [5, -1, 0, 0], [-1, 3, 0, 0], [0, -1, 4, 0], [-1, 0, 0, 2] )
cal = (5, 1, 6, 8)

def gen4():
	for x0 in range(97):
		for x1 in range(x0+1, 98):
			for x2 in range(x1+1, 99):
				yield x0, x1-x0, x2-x1, 100-x2

check(gen4, ('Sprinkles', 'PenutButter', 'Frosting', 'Sugar'), sc, cal)
