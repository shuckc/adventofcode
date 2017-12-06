import itertools

test = '0 2 7 0'
inp = '4	1	15	12	0	9	9	5	5	8	7	3	14	5	12	3'

def process(text):
	ts = [int(i) for i in text.split()]
	sz = len(ts)
	seen = set()
	p2 = False
	for c in itertools.count():
		print('{}: {}'.format(c, ts))
		# index of max,max
		im,m = max(enumerate(ts), key=lambda b: b[1])
		ts[im] = 0
		for i in range(m):
			idx = (im+i+1) % sz
			ts[idx] = ts[idx] + 1 
		tp = tuple(ts)
		if tp in seen:
			print(ts)
			yield c+1
			seen = set()
			if p2 == True:
				break
			p2 = True
		seen.add(tp)

print(list(process(test)))
print(list(process(inp)))
