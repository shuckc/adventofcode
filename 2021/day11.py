import numpy as np
eg = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
"""
eg2 = "11111\n19991\n19191\n19991\n11111\n"

def grid(eg):
	inp = np.fromiter(eg.replace('\n', ''), int)
	n = len(eg.split('\n')[0])
	return inp.reshape([-1,n])

def run(g, n=10):
	print("before\n{}".format(g))
	flashcount = 0
	for i in range(1,n+1):
		g = g + 1
		flashed = np.zeros(g.shape, bool)
		while True:
			flashers = np.argwhere(np.logical_and(g>9, flashed==False))
			if len(flashers) == 0:
				break
			for x,y in flashers:
				for xd,yd in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
					if x+xd >= 0 and x+xd < g.shape[0] and y+yd >= 0 and y+yd < g.shape[1]:
						g[x+xd,y+yd] += 1
				flashed[x,y] = True
		g[flashed] = 0
		flashcount += np.sum(flashed)
		print("after step {}\n{}".format(i, g))
		if np.all(flashed):
			print("all flashed")
			exit()
	print(flashcount)

print(run(grid(eg2), n=2))
print(run(grid(eg), n=100))
print(run(grid(open('input/day11.txt').read()), n=10000000))
