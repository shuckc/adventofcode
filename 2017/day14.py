
inp="ugkiagan"
keys = ['{}-{}'.format(inp, i) for i in range (128)]

from day10 import part2, getasciilens
hashed = [ format(int(part2(getasciilens(k)),16), '0128b') for k in keys]

total1s = sum([sum([ 1 if s == '1' else 0 for s in h]) for h in hashed])

print('\n'.join(hashed))
print(total1s)

# part2 - flood fill each region of 1s
region = [ [ 0 for i in range(128)] for j in range(128) ]
next_region = 1

def neighbours(r,c,sz):
	if r < sz-1:
		yield (r+1,c)
	if r > 0:
		yield (r-1, c)
	if c > 0:
		yield (r, c-1)
	if c < sz-1:
		yield (r, c+1)

for row in range(128):
	for column in range(128):
		bit = hashed[row][column] == '1'
		if bit and region[row][column] == 0: # unassigned, start flooding
			# flood fill
			work = [ (row,column) ]
			while work:
				r,c = work.pop(0)
				region[r][c] = next_region
				for (r1,c1) in neighbours(r,c,128):
					if region[r1][c1] == 0 and hashed[r1][c1] == '1':
						work.append((r1,c1))
			next_region = next_region + 1

print('regions {}'.format(next_region-1))
