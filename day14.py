import re, collections, itertools
RaindeerRec = collections.namedtuple('Reindeer', 'name, speed, runfor, restfor')
rds, scored = [], []
with open('input/day14.txt') as f:
	for inst in f.read().splitlines():
		m = re.match('(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.', inst)
		rr = RaindeerRec(m.group(1), *map(int, m.group(2,3,4)))
		scored.append( (rr, 0, True, rr.runfor, 0))
print scored

for t in range(2504):
	print("after {0}s : {1}".format(t, ', '.join([ '{0.name}={1}/{3}/{4}pts'.format(*a) for a in rds])))
	init, rds, scored = scored, [], []
	for (rd,dist,running,remaining, pts) in init:
		if remaining == 0:
			running = not running
			remaining = rd.runfor if running else rd.restfor
			print("  * {0.name} is now {1}".format(rd, ('Resting', 'Running')[running] ))			
		if running:
			dist += rd.speed
		rds.append((rd, dist, running, remaining-1, pts))
	maxdist = max([i[1] for i in rds])
	for (rd,dist,running,remaining, pts) in rds:
		if dist == maxdist: pts += 1
		scored.append((rd, dist, running, remaining, pts))

print('max dist {0} max pts {1}'.format(max([i[1] for i in scored]), max([i[4] for i in scored])))
