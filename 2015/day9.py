import collections, re
adjacency = collections.defaultdict(dict)
for x in open('input/day9.txt').read().splitlines():
	m = re.match('(\w+) to (\w+) = (\d+)', x)
	adjacency[m.group(1)][m.group(2)] = int(m.group(3))
	adjacency[m.group(2)][m.group(1)] = int(m.group(3))
#print adjacency
cand = [ ([k], 0, set([k])) for k in adjacency]

min_score, max_score = 1<<24, 0
while cand:
	c = cand.pop(0)
	#print last
	for k,s in adjacency[c[0][-1]].iteritems():
		if not k in c[2]:
			visited = set([k])
			visited |= c[2]
			c2 = ( c[0] + [k], c[1] + s, visited )
			cand.append(c2)
	if len(c[0]) == len(adjacency): 
		if c[1] < min_score:
			min_score = c[1]
			print "cheapest %s" % str(c)
		if c[1] > max_score:
			max_score = c[1]
			print "longest %s" % str(c)
#for p in final:
#	print p
print min_score
print max_score
