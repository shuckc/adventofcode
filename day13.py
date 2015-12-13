import re, collections, itertools
names = set()
weights = collections.defaultdict(lambda: collections.defaultdict(int))

with open('input/day13.txt') as f:
	for inst in f.read().splitlines():
		m = re.match('(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+)\.', inst)
		names.add(m.group(1))
		w = {'lose': -1, 'gain': 1}[m.group(2)] * int(m.group(3))
		weights[m.group(1)][m.group(4)] = w

def get_best(names):
	max_w = 0
	for x in itertools.permutations(list(names)):
		# pair each element with next, table is circular so wrap it
		r = list(x[1:]); r.append(x[0])
		w = sum([ weights[i][j] + weights[j][i] for i,j in zip(list(x), r)])
		if w > max_w:
			max_w = w
	return max_w

print 'Max w = %d' % get_best(names)
names.add('Me')
print 'Max w = %d' % get_best(names)
