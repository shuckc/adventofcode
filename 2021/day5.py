import numpy as np
eg = "0,9 -> 5,9\n8,0 -> 0,8\n9,4 -> 3,4\n2,2 -> 2,1\n7,0 -> 7,4\n6,4 -> 2,0\n0,9 -> 2,9\n3,4 -> 1,4\n0,0 -> 8,8\n5,5 -> 8,2"

def cmp(a, b):
    return (a > b) - (a < b)

def parse(eg, part2):
	for l in filter(None, eg.split('\n')):
		x0,y0,x1,y1 = [int(p) for p in l.replace(' -> ', ',').split(',')]
		xstep = cmp(x1,x0)
		ystep = cmp(y1,y0)
		steps = max(abs((x1-x0)*xstep),abs((y1-y0)*ystep))
		#print("xstep={} ystep={} steps={}".format(xstep,ystep,steps))
		if part2 or (xstep==0 or ystep == 0):
			for i in range(steps+1):
				yield x0+xstep*i,y0+ystep*i

def fill(points):
	ps = list(points)
	d = max(max([p[0] for p in ps]),max([p[1] for p in ps]))
	grid = np.zeros((d+1,d+1), int)
	for x,y in ps:
		grid[x,y] += 1
	print(np.transpose(grid))
	return grid

def score(grid):
	return np.sum(grid >= 2)

print(score(fill(parse(eg, False))))
print(score(fill(parse(open('input/day5.txt').read(), False))))

print(score(fill(parse(eg, True))))
print(score(fill(parse(open('input/day5.txt').read(), True))))
