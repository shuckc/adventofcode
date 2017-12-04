

def expand_p1(sz, section):
	return len(section)

def decompressed_len(input, expander=expand_p1):
	skip_to = -1
	sz = 0
	lb = -1
	lx = 0
	copy = True
	for i, c in enumerate(input):
		# find opening bracket
		if i <= skip_to:
			pass
		elif c == '(':
			lb = i
			copy = False
		elif c == 'x':
			lx = i
		elif c == ')':
			length = int(input[lb+1:lx])
			times = int(input[lx+1:i])
			sample = input[i+1:i+1+length]
			print('Rep {} x {} sample={}'.format(times, length, sample))

			sz = sz + times*expander(length, sample)
			skip_to = i + length
			copy = True
		else:
			if copy:
				sz = sz + 1

		print('  i={} c={!r} sz={} lb={} lx={} copy={} skip_to={}'.format(i, c, sz, lb, lx, copy, skip_to))	
	return sz

def test(input, e, **kwargs):
	r = decompressed_len(input, **kwargs)
	print('{} = {} {}'.format(input, r, e))
	if e != r:
		raise Exception('Incorrect length')

test('ADVENT', 6)
test('A(1x5)BC', 7) # repeats only the B a total of 5 times, becoming ABBBBBC for a decompressed length of 7.

test('(3x3)XYZ', 9) # becomes XYZXYZXYZ for a decompressed length of 9.
test('A(2x2)BCD(2x2)EFG', 11) # doubles the BC and EF, becoming ABCBCDEFEFG for a decompressed length of 11.
test('(6x1)(1x3)A', 6) # simply becomes (1x3)A - the (1x3) looks like a marker, but because it's within a data section of another marker, it is not treated any differently from the A that comes after it. It has a decompressed length of 6.
test('X(8x2)(3x3)ABCY', 18) # becomes X(3x3)ABC(3x3)ABCY (for a decompressed length of 18), because the decompressed data from the (8x2) marker (the (3x3)ABC) is skipped and not processed further.

with open('day9-input.txt') as f:
	print(decompressed_len(f.read().strip()))

def expand_p2(sz, section):
	return decompressed_len(section, expander=expand_p2)

test('X(8x2)(3x3)ABCY', 20, expander=expand_p2)

test('(27x12)(20x12)(13x14)(7x10)(1x12)A', 241920, expander=expand_p2)
test('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN', 445, expander=expand_p2)

with open('day9-input.txt') as f:
	print(decompressed_len(f.read().strip(), expander=expand_p2))

