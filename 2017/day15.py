
amult, bmult = [16807, 48271]
modulo = 2147483647
mask = 0xFFFF

def run(a, b, iters):
	total = 0
	for i in range(iters):
		a = (a * amult) % modulo
		b = (b * bmult) % modulo
		total = total + (1 if a & mask == b & mask else 0)
		# print('{:048b} {:048b} {}'.format(a,b, total))
	return total


#print(run(65, 8921, 8))
#print(run(65, 8921, 40000000))

#Generator A starts with 722
#Generator B starts with 354
#print(run(722, 354, 40000000))

# part 2
def run2(agen, bgen, iters):
	total = 0
	for i in range(iters):
		a = next(agen)
		b = next(bgen)
		total = total + (1 if a & mask == b & mask else 0)
		# print('{:048b} {:048b} {}'.format(a,b, total))
	return total

def gen(seed, mask, mult):
	while True:
		seed = (seed * mult) % modulo
		if seed & mask == 0:
			yield seed

# Generator A looks for values that are multiples of 4. = v&0x03=0 (bits 1,0, zero)
# Generator B looks for values that are multiples of 8. = v&0x07=0 (bits 2,1,0 zero)

#print(run2( gen(65, 0x03, amult), gen(8921, 0x07, bmult), 5000000)) # 309
print(run2( gen(722, 0x03, amult), gen(354, 0x07, bmult), 5000000))
