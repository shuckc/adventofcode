import numpy as np
eg = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
"""

def parse(eg):
	numbers,instructions = eg.split("\n\n")
	numbers = np.fromiter(numbers.replace("\n", ",").split(","), int).reshape([-1,2])
	#print(numbers)
	grid = np.zeros(shape=1+np.amax(numbers, axis=0), dtype=int)
	t = np.transpose(numbers)
	grid[t[0],t[1]] = 1
	instructions = [(i[11], int(i[13:])) for i in filter(None, instructions.split('\n'))]
	# print(grid)
	print(instructions)
	return np.transpose(grid), instructions

def fold(grid, instructions, limit=10^6):
	#print("grid\n{}".format(grid))
	for i,(direction,pos) in enumerate(instructions):
		#print(i)
		if direction == 'y':
			top = grid[0:pos,:]
			bot = np.flipud(grid[pos+1:,:])
			#print("top\n{}".format(top))
			#print("bottom\n{}".format(bot))
			grid = top+bot
		else:
			left = grid[:,0:pos]
			right = np.fliplr(grid[:,pos+1:])
			#print("left\n{}".format(left))
			#print("right\n{}".format(right))
			grid = left+right
		grid[grid>1] = 1
		#print("combined\n{}".format(grid))
		print("{} dots visible".format(np.sum(grid)))
		if i>= limit:
			break
	return(grid)

fold(*parse(eg))
fold(*parse(open('input/day13.txt').read()), limit=1)

g = fold(*parse(open('input/day13.txt').read()))
with np.printoptions(threshold=np.inf):
	print(g)

# [[1 1 1 1 0 1 1 1 1 0 1 0 0 0 0 1 1 1 1 0 0 0 1 1 0 0 1 1 0 0 1 1 1 0 0 1 1 1 1 0]
#  [1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 0 0 0 1 0 1 0 0 1 0 1 0 0 1 0 1 0 0 0 0]
#  [1 1 1 0 0 1 1 1 0 0 1 0 0 0 0 1 1 1 0 0 0 0 0 1 0 1 0 0 0 0 1 0 0 1 0 1 1 1 0 0]
#  [1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 0 0 0 1 0 1 0 1 1 0 1 1 1 0 0 1 0 0 0 0]
#  [1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 1 0 1 0 0 1 0 1 0 1 0 0 1 0 0 0 0]
#  [1 1 1 1 0 1 0 0 0 0 1 1 1 1 0 1 0 0 0 0 0 1 1 0 0 0 1 1 1 0 1 0 0 1 0 1 0 0 0 0]]

# EFLFJGRF
