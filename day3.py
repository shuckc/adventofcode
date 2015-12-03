import requests, os
r = requests.get('http://adventofcode.com/day/3/input', cookies=dict(session=os.environ['ADVENT_SESSION'])).text
#r='^v^v^v^v^v'
for players in [1,2]:
	houses, x, y = {(0,0):0}, [0]*players, [0]*players
	for c, move in enumerate(r):
		p = c % players
		x[p] += { '^': 0, 'v': 0, '>': 1, '<':-1}[move]
		y[p] += { '^': 1, 'v':-1, '>': 0, '<': 0}[move]
		houses[(x[p],y[p])] = houses.get((x[p],y[p]), 0) + 1
	print('houses visited by {0} players: {1}'.format(players, len(houses)))
