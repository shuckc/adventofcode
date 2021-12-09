import numpy as np
eg = "2199943210\n3987894921\n9856789892\n8767896789\n9899965678\n"

def parse(eg):
	return np.array([[int(x) for x in line] for line in filter(None, eg.split('\n'))])

def lowpoints(grid):
	# lowpoint is smaller than all four neighbours, accounting for edges
	# pad with 9s so that the boundary conditions are handled
	pad = np.ones((grid.shape[0]+2, grid.shape[1]+2))*9
	pad[1:-1,1:-1] = grid
	# roll in each of the four directions, up, down, left, right
	udlr = [np.roll(pad, -1, axis=0), np.roll(pad, 1, axis=0), np.roll(pad, -1, axis=1), np.roll(pad, 1, axis=1)]
	# take elementwise minimums
	mins = np.minimum(np.minimum(udlr[0], udlr[1]), np.minimum(udlr[2], udlr[3]))[1:-1,1:-1]
	return grid,grid < mins

def p1(grid, minpoints):
	mp = sum(1+grid[minpoints])
	return mp

# print(parse(eg))
print(p1(*lowpoints(parse(eg))))
print(p1(*lowpoints(parse(open('input/day9.txt').read()))))


def fill(boundary, x, y):
	queue = [(x,y)]
	f = 0
	bs = boundary.shape
	while(queue):
		x,y = queue.pop()
		if not boundary[x,y]:
			boundary[x,y] = True
			f += 1
			for xd,yd in [(1,0),(-1,0),(0,-1),(0,1)]:
				if x+xd < bs[0] and x+xd >= 0 and y+yd >= 0 and y+yd < bs[1]:
					queue.append((x+xd,y+yd))
	return f

def p2(grid, minpoints):
	# translate grid so that 9's are True (stop fill) everything else False
	boundary = grid == 9
	print(boundary)
	fills = [fill(boundary, x, y) for x,y in np.transpose(minpoints.nonzero())]
	return np.product(sorted(fills)[-3:])

print(p2(*lowpoints(parse(eg))))
print(p2(*lowpoints(parse(open('input/day9.txt').read()))))
