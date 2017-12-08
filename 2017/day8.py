import re
puzzle="""b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10"""

def parse(text):
	regs = {}
	maxr = -10000
	for t in text.split('\n'):
		m = re.match(r'(\w+) (inc|dec) (-?\d+) if (\w+) ([<>=!]+) (-?\d+)', t)
		if not m:
			raise Exception(text)
		print(m.groups())
		regr = m.groups()[0]
		mult = +1 if m.groups()[1] == 'inc' else -1
		delta = int(m.groups()[2])
		cond_regr = regs.get(m.groups()[3], 0)
		op = {'==': '__eq__', '>': '__gt__', '<':'__lt__', '>=':'__ge__', '<=':'__le__', '!=':'__ne__'}[m.groups()[4]]
		cmp_r = int(m.groups()[5])

		if getattr(cond_regr, op)(cmp_r):
			m = regs.get(regr, 0) + mult*delta
			regs[regr] = m
			maxr = max(maxr, m)

	return regs, maxr

print(parse(puzzle))

with open('input/day8.txt') as f:
	x,m = parse(f.read().strip())

print(max(x.items(), key=lambda y: y[1]))
print(m)
