from common import ai

def parsemaps(inp):
	allmaps = {}
	seeds = None
	currentmap = None
	for line in inp.strip().split("\n"):
		if "seeds: " in line:
			seeds = list(map(int, line[7:].split(" ")))
		elif "-to-" in line:
			currentmap = []
			tok,_ = line.strip().split(" ")
			x,y = tok.split('-to-')
			print(f" parsing map from {x} to {y}")
			allmaps[(x,y)] = currentmap
		elif line.strip() == "":
			continue
		else:
			a,b,c = map(int, line.strip().split(" "))
			currentmap.append((a,b,c))
	return seeds, allmaps

def lookup(s, amap):
	for dest,src,length in amap:
		if s >= src and s < src+length:
			return dest + s - src
	return s

# map entry is dest-start, source-start, length
# seed-to-soil:
#   50 98 2
#   52 50 48
# means
# seed 98 needs soil 50, seed 99 needs soil 51
# seed 53 needs soil 55
# seed 10 maps to soil 10 as outside of any range is identitity
testmap = [(50, 98, 2), (52, 50, 48)]
ai(lookup(98, testmap), 50)
ai(lookup(99, testmap), 51)
ai(lookup(53, testmap), 55)
ai(lookup(10, testmap), 10)

def p1(inp, seedfixer=lambda x: x):
	seeds, allmaps = parsemaps(inp)
	seeds = seedfixer(seeds)
	print(f"seeds {seeds}")
	print(f"allmaps {allmaps}")
	minlocs = None
	walk_order = 'seed soil fertilizer water light temperature humidity location'.split(" ")
	for s in seeds:
		# print(f'seed {s}:')
		for i,w in enumerate(walk_order):
			# print(f'at {walk_order[i]} {s}')
			if i+1 == len(walk_order):
				break
			mm = walk_order[i], walk_order[i+1]
			amap = allmaps[mm]
			# print(f' map {mm} is {amap}')
			s = lookup(s, amap)
		if minlocs is None:
			minlocs = s
		if s < minlocs:
			minlocs = s
	return minlocs

ai(p1(open("day5-sample.txt").read()), 35)
ai(p1(open("day5.txt").read()), 196167384)

def p2seedfixer(seeds):
	for a,b in zip(seeds[::2], seeds[1::2]):
		for i in range(a,a+b):
			yield i

ai(p1(open("day5-sample.txt").read(), seedfixer=p2seedfixer), 46)
# does not finish
# ai(p1(open("day5.txt").read(), seedfixer=p2seedfixer), 46)

