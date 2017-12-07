import re
inp="""pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)"""

def parse(text):
	parentof = {}
	childrenof = {}
	names = set()
	for t in text.split('\n'):
		print(t)
		m = re.match('(\w+) \\((\d+)\\)(?: -> (.*))?', t)
		name = m.groups()[0]
		weight = int(m.groups()[1])
		children = m.groups()[2].split(', ') if m.groups()[2] else []
		childrenof[name] = (weight, children)
		print(children)
		for c in children: # backlink to find root
			parentof[c] = name
		names.add(name)
	s = name
	while True:
		p = parentof.get(s)
		print(p)
		if not p:
			print('ultimate parent is {}'.format(s))
			break
		s = p

	# check weights of child of each name sum
	def self_and_child_weights(name):
		weight, cs = childrenof[name]
		child_weights = [ self_and_child_weights(c) for c in cs]
		if sum(child_weights) > 0 and max(child_weights) != min(child_weights):
			print('inbalence detected at {}, with children {} cum weights: {} childweights: {}'.format(name, cs, child_weights, [childrenof[c][0] for c in cs]))
		return weight + sum(child_weights)

	for n in names:
		self_and_child_weights(n)

parse(inp)

with open('input/day7.txt') as f:
	print(parse(f.read().strip()))
	
# inbalence detected at nieyygi, with children ['ptshtrn', 'mxgpbvf', 'cfqdsb', 'yfejqb']
#   cum weights: [1122, 1117, 1117, 1117] childweights: [526, 52, 556, 493]
# 1122-1117=5    526-5=521
