msg="""eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar"""

msgs = msg.split('\n')

def score(msgs, weight=-1):
	for i in range(len(msgs[0])):
		counts = {}
		for w in msgs:
			c = w[i]
			counts[c] = counts.get(c, 0) + 1
		# most occuring
		x = sorted( [ (l,c) for l,c in counts.items()], key=lambda c: weight*c[1] )
		yield x[0][0]

print(''.join(list(score(msgs))))
print(''.join(list(score(msgs, 1))))

with open('day6-input.txt') as f:
	print(''.join(list(score( f.read().splitlines() ))))

with open('day6-input.txt') as f:
	print(''.join(list(score( f.read().splitlines(), 1))))


