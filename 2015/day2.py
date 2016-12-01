import requests, os
r = requests.get('http://adventofcode.com/day/2/input', cookies=dict(session=os.environ['ADVENT_SESSION']))
s, ri = 0, 0
for parcel in r.text.splitlines():
	l,w,h = map(int, parcel.split('x'))
	# print ("l = {0}, w={1}, h={2}".format(l,w,h))
	surf = 2*l*w + 2*w*h + 2*h*l
	slack = min(l*w, w*h, h*l)
	s += surf + slack
	# a,b are least two dimensions
	a,b,_ = sorted([l,w,h])
	ri += (a+a+b+b) + (l*w*h)
print 'paper %d' % s
print 'ribbon %d' % ri
