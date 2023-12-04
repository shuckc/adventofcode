from common import ai
from collections import defaultdict

inp = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

def chopit(inp):
	r = {}
	for l in inp.strip().split("\n"):
		g,ps = l.split(":")
		print(g)
		gn = int(g[5:])
		l = []
		for pp in ps.split(";"):
			pp = pp.strip()
			d = {}
			for ncol in pp.split(','):
				print(ncol)
				n, col = ncol.strip().split(" ")
				d[col] = int(n)
			l.append(d)
		r[gn] = l
	return r

def p1(games, limits={}):
	t = 0
	for score,g in games.items():
		valid = True
		for trial in g:
			for colour, count in trial.items():
				if count > limits[colour]:
					valid = False
		if valid:
			t += score
	return t
cons = {'blue': 14, 'green':13, 'red':12}
ai(p1(chopit(inp), cons), 8)
ai(p1(chopit(open("day2.txt").read()), cons), 1734)

def p2(games, limits={}):
	t = 0
	for score,g in games.items():
		limits = defaultdict(int)
		for trial in g:
			for colour, count in trial.items():
				if count > limits[colour]:
					limits[colour] = count
		p = 1
		[p := p * x for x in limits.values()]
		print(f"{limits.values()} p={p}")
		t += p
	return t

ai(p2(chopit(inp)), 2286)
ai(p2(chopit(open("day2.txt").read())), 70387)
