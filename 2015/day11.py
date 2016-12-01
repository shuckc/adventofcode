
import re
def adder_chain(args):
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
	#print out
	return out

inp = 'hxbxwxba'
print(inp)
passwords = 2
while passwords > 0:
	inp = ''.join(map(chr, adder_chain(map(ord, inp))))
	#print inp
	if bool(re.match("[iol]", inp)):
		continue
	# all possible tripples
	if not any( ord(x)+2 == ord(y)+1 == ord(z) for x,y,z in zip( inp, inp[1:], inp[2:]) ):
		continue
	if len(set([x for x,y in zip( inp, inp[1:]) if x == y])) < 2:
		continue
	print "Password " + inp
	passwords -= 1
