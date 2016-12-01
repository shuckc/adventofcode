import collections, itertools
def load(fn):
	rules = collections.defaultdict(list)
	with open(fn) as f:
		for inst in f.read().splitlines():
			if '=>' in inst:
				k,v = inst.split(' => ')
				rules[k].append(v)
	return dict(rules), inst

def iter(rules, molecule):
	outs = []
	for i,x in enumerate(molecule):
		for sz in range(1,3):
			sub1 = molecule[i:i+sz]
			if len(sub1) == sz:
				repl = rules.get(sub1, [])
				# print sub1, repl
				for r in repl:
					outs.append(molecule[0:i] + r + molecule[i+sz:])
	return outs, len(set(outs))

rules, molecule = load('input/day19-sample.txt')
print iter(rules, molecule)
print
print iter(rules, 'HOHOHO')
print
r2, m2 = load('input/day19.txt')
#print iter(r2, m2)

def evolve(rules, molecule, c1='e'):
	cand = [c1]
	for i in itertools.count(1):
		print 'Starting step {}'.format(i)
		out = []
		for c in cand:
			outs,cnt = iter(rules, c)
			# print 'checking {} -> {}'.format(c, outs)
			if molecule in outs:
				print 'finished found {} after {} steps'.format(molecule,i)
				return i
			out.extend(outs)
		cand, out = list(set(out)), []

print evolve(rules, molecule)
print evolve(rules, 'HOHOHO')

print evolve(r2, m2)
