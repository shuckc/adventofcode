import requests, os, re

def get(inp, known, override):
	return int(inp) if inp.isdigit() else override.get(inp, known[inp])

def emulate(known, pending, override={}):
	while pending:
		inst = pending.pop(0)
		m = re.match('(?:(?:([\d\w]+) )?(AND|OR|LSHIFT|RSHIFT|NOT) )?([\d\w]+) -> (\w+)', inst)
		if not all([x in known for x in m.group(1, 3) if x and not x.isdigit()]):
			pending.append(inst)
			# print ' deferring %s' % inst
		else:
			rhs = get(m.group(3), known, override)
			if not m.group(2): # simple assignment
				known[m.group(4)] = rhs
			else:
				fn = m.group(2)
				if fn == 'NOT': # unary
					known[m.group(4)] = (~ rhs) & 0xFFFF
				else: # binary
					lhs = get(m.group(1), known, override)
					if fn == 'AND':
						known[m.group(4)] = lhs & rhs
					elif fn == 'OR':
						known[m.group(4)] = lhs | rhs
					elif fn == 'LSHIFT':
						known[m.group(4)] = lhs << rhs
					elif fn == 'RSHIFT':
						known[m.group(4)] = lhs >> rhs
					else:
						raise ValueError(fn)
	return known

circuit = {}
assert emulate(circuit, ['123 -> x'])['x'] == 123
assert emulate(circuit, ['x AND y -> d', '456 -> y'])['y'] == 456
assert circuit['d'] == 72
assert emulate(circuit, ['x OR y -> e'])['e'] == 507
assert emulate(circuit, ['x LSHIFT 2 -> f'])['f'] == 492
assert emulate(circuit, ['y RSHIFT 2 -> g'])['g'] == 114
assert emulate(circuit, ['NOT x -> h'])['h'] == 65412
assert emulate(circuit, ['NOT y -> i'])['i'] == 65079

t = requests.get('http://adventofcode.com/day/7/input', cookies=dict(session=os.environ['ADVENT_SESSION'])).text
circuit = {}
emulate(circuit, t.splitlines())
print '1) emulate a is %d' % circuit['a']
circuit2 = {}
emulate(circuit2, t.splitlines(), override={'b': circuit['a']})
print '2) emulate a is %d' % circuit2['a']
