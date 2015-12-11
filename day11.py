
def plus(args):
	c = 1
	out = []
	for x in reversed(args): 
		if c > 0:
			x += 1
			c = 0
		if x > ord('z'):
			c = 1
			x = ord('a')
		out.insert(0, x)
	print out
	return out

inp = 'xx'
for i in range(8):
	print inp
	inp = ''.join(map(chr, plus(map(ord, inp))))
	
