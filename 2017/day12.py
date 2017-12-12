


inp="""0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5"""



def parse(inp):
	nbs = dict([(int(x),map(int, y.split(','))) for (x,y) in [i.split(' <-> ') for i in inp.split('\n')]])
	# print(nbs)
	all_nodes = set(nbs.keys())
	groups = 0
	while all_nodes:
		n = all_nodes.pop()
		vs = extractGroup(nbs, n)
		print('{} visited {}'.format(n, len(vs)))
		all_nodes -= vs
		groups=groups+1
	print('groups {}'.format(groups))


def extractGroup(nodes, node=0):
	visited = set()
	visit = [node]
	while visit:
		n = visit.pop()
		visited.add(n)
		for node in nodes[n]:
			# print(node)
			if not node in visited:
				visit.append(node)
	return visited

parse(inp)

with open('input/day12.txt') as f:
	parse(f.read().strip())



