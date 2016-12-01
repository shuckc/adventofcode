import requests, os
r = requests.get('http://adventofcode.com/day/1/input', cookies=dict(session=os.environ['ADVENT_SESSION']))
s, cb = 0,-1
for c,up_down in enumerate(r.text):
	s += { '(': 1, ')': -1}[up_down]
	if s == -1 and cb == -1:
		cb = c
print 'final floor %d' % s
print 'basement at %d' % (cb+1)
