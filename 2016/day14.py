import re, collections, itertools

def parse(t):
	sprinting = []
	resting = []
	for r,sp,sprint_t,recov_t in re.findall('(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d)+ seconds.', t):
		print r + ' speed=' + sp + ' sprint_t=' + sprint_t + ' recov_t=' + recov_t
		sprinting.append( { 'r':r, 'sp':int(sp), 'sprint_t' : int(sprint_t), 'recov_t': int(recov_t), 'count': int(sprint_t), 'dist': 0 })
	return sprinting, resting


def race(sprinting, resting, dist=1):	
	for i in range(1,dist+1):
		rs, rr = list(sprinting), list(resting)
		for r in rs:
			if r['count'] == 0:
				print str(i) + ': ' + r['r'] + ' is exhausted ' + str(r)
				sprinting.remove(r)
				resting.append(r)
				r['count'] = r['recov_t']
			else:
				r['count'] -= 1
				r['dist'] += r['sp']
		for r in rr:
			if r['count'] == 0:
				resting.remove(r)
				sprinting.append(r)
				r['count'] = r['sprint_t']
				print str(i) + ': ' + r['r'] + ' is finished resting' + str(r)
			else:
				r['count'] -= 1
	for r in sprinting:
		print 'sprinting: ' + str(r)
	for r in resting:
		print 'resting: ' + str(r)	
	# distance of winning raindeer
	print 'time ' + str(i) + ' max ' + str(max( [r['dist'] for r in sprinting + resting] ))

sprinting, resting = parse('Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds. Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.')
#race(sprinting, resting, 1)
#race(sprinting, resting, 9)
#race(sprinting, resting, 1)
#race(sprinting, resting, 1)
race(sprinting, resting, 1000)
exit()
with open('input/day14.txt') as f:
	sprinting, resting = parse(f.read())
	race(sprinting, resting, 2503)
