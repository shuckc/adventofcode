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

walk_order = 'seed soil fertilizer water light temperature humidity location'.split(" ")
def p1(inp):
	seeds, allmaps = parsemaps(inp)
	print(f"seeds {seeds}")
	print(f"allmaps {allmaps}")
	minlocs = []
	for s in seeds:
		print(f'seed {s}:')
		for i,w in enumerate(walk_order):
			# print(f'at {walk_order[i]} {s}')
			if i+1 == len(walk_order):
				break
			mm = walk_order[i], walk_order[i+1]
			amap = allmaps[mm]
			# print(f' map {mm} is {amap}')
			s = lookup(s, amap)
		minlocs.append(s)
	return min(minlocs)

ai(p1(open("day5-sample.txt").read()), 35)
ai(p1(open("day5.txt").read()), 196167384)
print('p1 done')
# the trick for part2 is to work with ranges. Each map in amap may
# split the input range sr into multiple ranges. Eventually we
#
#  amap      aaaaaaaaa      bbbbbb        ccccc
#  sr           -----------------------
#  output       aaaaaa------bbbbbb-----
#
def lookup_split_range(sr, amap):
	print(f'lsr {sr} against {amap}')
	# sort amap based on src start index
	amap = sorted(amap, key=lambda entry: entry[1])
	rs = []
	pos = sr[0]
	while pos < sr[1]:
		for dest,src,length in amap:
			print(f' pos {pos} against range {src}-{src+length} (shift to {dest})')
			if src <= pos and pos < (src+length):
				# stop at either end of range or src+length
				shift = dest - src
				stop = min(src+length, sr[1])
				print(f'  match ends at {stop}')
				rs.append( (pos+shift, stop+shift) )
				pos = stop
				break
		else:
			stop = min([sr[1]] + [src for dest,src,_ in amap if pos <= src])
			print(f'no match until {stop}')
			rs.append((pos,stop))
			pos = stop
		print(f'here {rs}')
	return rs

# map entry is dest-start, source-start, length
# seed-to-soil:
#   50 98 2
#   52 50 48
# means
# seed 98-99 needs soil 50-51
# seed 50-60 needs soil 52-62
# seed 10-20 maps to soil 10-20 as outside of any range is identitity
testmap = [(50, 98, 2), (52, 50, 48)]
ai(lookup_split_range((98,99), testmap), [(50,51)])
ai(lookup_split_range((50,60), testmap), [(52,62)])
ai(lookup_split_range((10,20), testmap), [(10,20)])
ai(lookup_split_range((10,60), testmap), [(10,50), (52,62)])
ai(lookup_split_range((10,110), testmap), [(10,50), (52,100), (50,52), (100,110)])

# swap the order of the loops compared to p1 so that
# we push all ranges through the first map, then the second...
def p2(inp):
	seeds, allmaps = parsemaps(inp)
	seedrange = []
	for a,b in zip(seeds[::2], seeds[1::2]):
		seedrange.append((a, a+b))

	print(f"p2 seeds {seedrange}")
	print(f"allmaps {allmaps}")
	for i,w in enumerate(walk_order):
		if i+1 == len(walk_order):
			break
		nextsr = []
		mm = walk_order[i], walk_order[i+1]
		amap = allmaps[mm]
		print(f' map {mm} is {amap}')

		for sr in seedrange:
			print(f'at {walk_order[i]} range {sr}')
			ss = lookup_split_range(sr, amap)
			nextsr.extend(ss)

		seedrange = nextsr

	return min([sr[0] for sr in seedrange])

ai(p2(open("day5-sample.txt").read()), 46)
ai(p2(open("day5.txt").read()), 125742456)

