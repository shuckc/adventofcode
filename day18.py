
# http://www.labri.fr/perso/nrougier/teaching/numpy/numpy.html#the-game-of-life
import numpy as np

def loadLife(fn='input/day18.txt'):
	with open(fn) as f:
		row = len(f.read().splitlines()[0])

	Z = np.zeros([row+2, row+2], dtype=np.int8)
	corners = np.zeros([row,row], dtype=np.bool)
	with open(fn) as f:
		for row,inst in enumerate(f.read().splitlines()):
			for col,val in enumerate(inst):
				Z[row+1][col+1] = 1 if val == '#' else 0
	corners[[0,0,-1,-1], [0,-1,0,-1]] = 1
	return Z, corners

def iterate_2(Z, c):
    # Count neighbours
    N = (Z[0:-2,0:-2] + Z[0:-2,1:-1] + Z[0:-2,2:] +
         Z[1:-1,0:-2]                + Z[1:-1,2:] +
         Z[2:  ,0:-2] + Z[2:  ,1:-1] + Z[2:  ,2:])

    # Apply rules
    birth = (N==3) & (Z[1:-1,1:-1]==0)
    survive = ((N==2) | (N==3)) & (Z[1:-1,1:-1]==1)
    Z[...] = 0
    Z[1:-1,1:-1][birth | survive | c] = 1
    return Z

Z,c = loadLife()
Z[1:-1,1:-1][c] = 1
print Z[1:-1,1:-1]
for i in range(1,101):
	print('After {} steps:'.format(i))
	Z = iterate_2(Z, c)
	print Z[1:-1,1:-1]
print np.sum(Z)
