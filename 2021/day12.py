import numpy as np
from collections import defaultdict
eg = "start-A\nstart-b\nA-c\nA-b\nb-d\nA-end\nb-end\n"""


def p1visit(adj, lc, node, visited, twice, routes):
	visited.append(node)
	#print(visited)
	if node == 'end':
		routes.append('-'.join(visited))
	else:
		[p1visit(adj, lc, d, visited.copy(), False, routes) for d in sorted(adj[node]) if not ((d in lc) and (d in visited))]

def p2visit(adj, lc, node, visited, twice, routes):
	visited.append(node)
	if node == 'end':
		routes.append('-'.join(visited))
	else:
		if not twice:
			[p2visit(adj, lc, d, visited.copy(), True, routes) for d in sorted(adj[node]) if (d in lc) and (d in visited) and (d not in ('start', 'end'))]
		[p2visit(adj, lc, d, visited.copy(), twice, routes) for d in sorted(adj[node]) if not ((d in lc) and (d in visited))]


def router(eg, visitor):
	adj = defaultdict(list)
	lc = set()
	for line in filter(None,eg.split('\n')):
		a,b = line.strip().split("-")
		adj[a].append(b)
		adj[b].append(a)
		if a.lower() == a:
			lc.add(a)
		if b.lower() == b:
			lc.add(b)
	#lc.remove('start')
	#lc.remove('end')
	print(adj)
	print(lc)

	routes = []
	visitor(adj, lc, 'start', [], False, routes)
	print(routes)
	print(len(routes))

router(eg, p1visit)
#router("dc-end\nHN-start\nstart-kj\ndc-start\ndc-HN\nLN-dc\nHN-end\nkj-sa\nkj-HN\nkj-dc\n", p1visit)
#router("fs-end\nhe-DX\nfs-he\nstart-DX\npj-DX\nend-zg\nzg-sl\nzg-pj\npj-he\nRW-he\nfs-DX\npj-RW\nzg-RW\nstart-pj\nhe-WI\nzg-he\npj-fs\nstart-RW\n", p1visit)
#with open('input/day12.txt') as f:
#	router(f.read(), p1visit)

router(eg, p2visit)
router("dc-end\nHN-start\nstart-kj\ndc-start\ndc-HN\nLN-dc\nHN-end\nkj-sa\nkj-HN\nkj-dc\n", p2visit)
router("fs-end\nhe-DX\nfs-he\nstart-DX\npj-DX\nend-zg\nzg-sl\nzg-pj\npj-he\nRW-he\nfs-DX\npj-RW\nzg-RW\nstart-pj\nhe-WI\nzg-he\npj-fs\nstart-RW\n", p2visit)
with open('input/day12.txt') as f:
	router(f.read(), p2visit)

