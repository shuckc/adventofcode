

DIR = {'n':(0,1,-1), 's':(0,-1,1), 'ne':(1,0,-1), 'se':(1,-1,0), 'nw':(-1,+1,0), 'sw':(-1,0,1) }
def hcount(steps):
	dx,dy,dz = 0,0,0
	mx = 0
	for s in steps:
		dx = dx + DIR[s][0]
		dy = dy + DIR[s][1]
		dz = dz + DIR[s][2]
		md = (abs(dx)+abs(dy)+abs(dz))/2
		if md > mx:
			mx = md
	return md, mx 

def test(steps, s):
	p = hcount(steps.split(','))[0]
	if p != s:
		raise Exception('mismatch expected {} got {} for {}'.format(s, p, steps))

test('ne,ne,ne', 3) # is 3 steps away.
test('ne,ne,sw,sw', 0) # is 0 steps away (back where you started).
test('ne,ne,s,s', 2) # is 2 steps away (se,se).
test('se,sw,se,sw,sw', 3) # is 3 steps away (s,s,sw).

with open('input/day11.txt') as f:
	print(hcount(f.read().strip().split(',')))

