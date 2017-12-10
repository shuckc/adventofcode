

def knot(r, idx, length):
	# sublist from (idx:idx+length)
	# to allow wrapping, first double up r
	r3 = r + r + r
	rl = len(r)
	p = r3[idx:idx+length]
	twist = list(reversed(p))
	# print(' tw {}'.format(twist))
	r3[idx:idx+length] = twist
	r3[rl+idx:rl+idx+length] = twist
	return r3[rl:rl+rl]

def puz(r, lengths, pos=0, ss=0):
	for length in lengths:
		# print(r)
		r = knot(r, pos, length)
		pos = (pos + length + ss) % len(r)
		ss = ss + 1

	#print(r)
	#print(r[0] * r[1])
	return (r, pos, ss)

pi = '183,0,31,146,254,240,223,150,2,206,161,1,255,232,199,88'
puz(list(range(5)), [3,4,1,5])

# part1
puz(list(range(256)), [int(i) for i in pi.split(',')] )

# part2
# multiple rounds, retaining position and ss values
def getasciilens(text):
	# '1,2,3' ~> 49,44,50,44,51,17,31,73,47,23
	return [ord(c) for c in text] + [17, 31, 73, 47, 23]

print(getasciilens('1,2,3'))
import operator
from functools import reduce

def part2(lengths):
	r = list(range(256))
	pos = 0
	ss = 0
	for i in range(64):
		r, pos, ss = puz(r, lengths, pos=pos, ss=ss)
	return hexify(r)

def hexify(r):
	# r is sparse hash
	ls = []
	for i in range(0, 256, 16):
		# reduce with xor
		sliced = r[i:i+16]
		ls.append(reduce(operator.xor, sliced, 0))
	sr = ''.join(['{:02x}'.format(l) for l in ls ])
	return(sr)

print(hexify([65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22] + list(range(256-16))))

part2([3, 4, 1, 5, 17, 31, 73, 47, 23])
assert part2(getasciilens('')) == 'a2582a3a0e66e6e86e3812dcb672a272'
assert part2(getasciilens('AoC 2017')) == '33efeb34ea91902bb2f59c9920caa6cd'
print(part2(getasciilens(pi)))


