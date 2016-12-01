import requests, os, re

def decorate(grid, inst):
	m = re.match('(turn on|toggle|turn off) (\d+),(\d+) through (\d+),(\d+)', inst)
	x0, y0, x1, y1 = map(int, m.group(2,3,4,5))
	ff_set, ff_rst, ff_xor = map(inst.startswith, ['turn on', 'turn off', 'toggle'])
	#print('inst {0} => set:{1} reset:{2} xor:{3}'.format(m.group(1), ff_set, ff_rst, ff_xor) )
	for x in range(x0,x1+1):
		for y in range(y0,y1+1):
			grid[x][y] = ((grid[x][y] or ff_set) and not ff_rst) ^ ff_xor
	return sum(map(sum, grid))

# Part one models the grid as a set of boolean flip flops
g = [[False]*10 for x in range(10)]
assert decorate(g, 'turn on 0,0 through 4,4') == 5*5
assert decorate(g, 'toggle 1,1 through 4,4') == 5+4

g = [[False]*1000 for x in range(1000)]
assert decorate(g, 'turn on 0,0 through 999,999') == 1000000
assert decorate(g, 'toggle 0,0 through 999,0') ==  1000000 - 1000
assert decorate(g, 'turn off 499,499 through 500,500') == 1000000 - 1000 - 4

# Part two uses integer weights. Could be unifyied by passing in a fn to
# mutate the current cell. 
def decorate_p2(grid, inst):
	m = re.match('(turn on|toggle|turn off) (\d+),(\d+) through (\d+),(\d+)', inst)
	x0, y0, x1, y1 = map(int, m.group(2,3,4,5))
	adj = {'turn on':1, 'turn off':-1, 'toggle':2}[m.group(1)]
	for x in range(x0,x1+1):
		for y in range(y0,y1+1):
			grid[x][y] = max(0, grid[x][y] + adj)
	return sum(map(sum, grid))

g = [[0]*10 for x in range(10)]
assert decorate_p2(g, 'turn on 0,0 through 4,4') == 25
assert decorate_p2(g, 'toggle 1,1 through 4,4') == 25 + 16*2

t = requests.get('http://adventofcode.com/day/6/input', cookies=dict(session=os.environ['ADVENT_SESSION'])).text
g = [[False]*1000 for x in range(1000)]
for line in t.splitlines():
	r = decorate(g, line)
print '(1) Lights on %d' % r

g = [[0]*1000 for x in range(1000)]
for line in t.splitlines():
	r = decorate_p2(g, line)
print '(2) cumulative brightness %d' % r
