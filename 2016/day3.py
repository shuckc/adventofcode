import itertools

def possible(triangle):
	for ss in itertools.permutations(triangle, 3):
		if (ss[0] + ss[1] <= ss[2]):
			return False
	return True

print( possible( [20,10,25] ))
print( possible( [5,10,25] ))
print( possible( [5,10,5] ))

working = 0
accum = [], [], []
with open('day3-input.txt') as f:
	for inst in f.read().splitlines():
		triangle = map( int, inst.strip().split())
		if possible( triangle ):
			working += 1
		for lst, item in zip(accum, triangle):
			lst.append(item)
col_working = 0
onecol = accum[0] + accum[1] + accum[2] 
for a, b, c in zip(*[iter(onecol)]*3):
	if possible( (a,b,c) ):
		col_working += 1

print('working {} col_working {}'.format(working, col_working))
