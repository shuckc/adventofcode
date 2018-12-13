import itertools

def readwords():
	with open('input/day1.txt') as f:
		for line in f.read().splitlines():
			yield int(line.strip())

print(sum(readwords()))


last = 0
p = set([last])
for i in itertools.cycle(readwords()):
	last += i
	if last in p:
		print(last)
		break
	p.add(last)
