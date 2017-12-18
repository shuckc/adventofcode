

dancers = 5
# s1, a spin of size 1: eabcd.
# x3/4, swapping the last two programs: eabdc.
# pe/b, swapping programs e and b: baedc.
inp = 's1,x3/4,pe/b'

def dancers(count):
	return [chr(i + ord('a')) for i in range(count)]

def dance(init, inp):
	for i in inp.split(','):
		# print(' {:10}  {}'.format(i, ''.join(init)))
		if i[0] == 's':
			spin = int(i[1:])
			#print(spin)
			init = init[-spin:] + init[0:-spin]
		elif i[0] == 'x':
			exc = [int(p) for p in i[1:].split('/')]
			init[exc[0]], init[exc[1]] = init[exc[1]], init[exc[0]]
		elif i[0] == 'p':
			swp = i[1:].split('/')
			exc = [i for i,x in enumerate(init) if x in swp]
			#print(exc)
			init[exc[0]], init[exc[1]] = init[exc[1]], init[exc[0]]
		else:
			raise Exception(i)
	return init

dance(dancers(5), inp)

with open('input/day16.txt') as f:
	instrs = f.read().strip()
	before = dancers(16)
	after = dance(before, instrs)
print(''.join(after))

# part 2 - 1B iterations
# map effect of one iterations: before [abcd...] to after [djna...]

seen = {}

init = ''.join(dancers(16))
for i in range(1000000000):
	if init in seen:
		init = seen[init]
	else:
		key = init
		init = ''.join(dance(list(init), instrs))
		seen[key] = init
		print('generated {}'.format(init))

print(init)
