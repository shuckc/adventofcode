import itertools

# logo script to walk the spiral
def gen_logo():
	for n in itertools.count():
		for n in range(n+1):
			yield('F')
		yield('L')
		for n in range(n+1):
			yield('F')
		yield('L')

print(''.join(itertools.islice(gen_logo(), 100))) # grab the first five elements

# logo turtle interpreter, returns (n,x,y) each square visited
rotL = {'N': 'W', 'S': 'E', 'E':'N', 'W': 'S' }
move = {'N': (0,1), 'S':(0,-1), 'E':(1,0), 'W':(-1,0)} # (x,y)
def gene():
	x,y,n = 0,0,0
	direction = 'E'
	for cmd in gen_logo():
		if cmd == 'L':
			direction = rotL[direction]
		elif cmd == 'F':
			xd, yd = move[direction]
			n = n + 1
			yield( (n, x, y) )
			x = x + xd
			y = y + yd

print(list(itertools.islice(gene(), 26)))

def walk(steps):
	for n, x, y in gene():
		if n == steps:
			return abs(x) + abs(y)

def check(steps, e):
	print('{} == {}'.format(walk(steps), e))

check(1, 0) #1 is carried 0 steps, since it's at the access port.
check(12, 3) #Data from square 12 is carried 3 steps, such as: down, left, left.
check(23, 2) #Data from square 23 is carried only 2 steps: up twice.
check(1024, 31) #Data from square 1024 must be carried 31 steps.

print(walk(289326))

# part 2 
# each position in the spiral has an associated value, which is assigned once
# based ont he sum of the neigbouring 9 squares, or zero if not assigned at that time

def neighbours(x,y):
	yield (x,y+1)
	yield (x,y-1)
	yield (x+1,y)
	yield (x-1,y)
	yield (x+1,y+1)
	yield (x-1,y+1)
	yield (x+1,y-1)
	yield (x-1,y-1)

def gene2():
	saved_values = {}
	around = 1
	for n,x,y in gene():
		if n > 1:
			around = sum([ saved_values.get( (nx, ny), 0) for (nx,ny) in neighbours(x,y) ])
		saved_values[ (x,y) ] = around
		yield(around)

print(list(itertools.islice(gene2(), 26)))

for x in gene2():
	if x > 289326:
		print(x)
		break

