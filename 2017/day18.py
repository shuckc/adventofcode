


def evaluate(code):
	instrs = [ j.split(' ') for j in code.split('\n') ]
	pc = 0
	regs = {}
	def regv(v):
		if (v[0] >= '0' and v[0] <= '9') or v[0] == '-':
			return int(v)
		return regs.get(v, 0)
	snd = None
	while pc >= 0 and pc < len(instrs):
		instr = instrs[pc]
		print('{} {}:  {}  {}'.format(p, pc, instr, regs))
		offset = 1
		if instr[0] == 'set':
			regs[instr[1]] = regv(instr[2])
		elif instr[0] == 'add':
			regs[instr[1]] = regv(instr[1]) + regv(instr[2])
		elif instr[0] == 'mul':
			regs[instr[1]] = regv(instr[1]) * regv(instr[2])
		elif instr[0] == 'mod':
			regs[instr[1]] = regv(instr[1]) % regv(instr[2])
		elif instr[0] == 'rcv':
			if not regv(instr[1]) == 0:
				regs[instr[1]] = snd
				yield snd
		elif instr[0] == 'jgz':
			if regv(instr[1]) > 0:
				offset = regv(instr[2])
				print('jumping by {}'.format(offset))
		elif instr[0] == 'snd':
			snd = regv(instr[1])
		else:
			raise Exception(instr)

		pc = pc + offset

	yield None

program = """set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2"""

#pe = evaluate(program)
#print(next(pe))

with open('input/day18.txt') as f:
	instrs = f.read().strip()

# pe = evaluate(instrs)
# print(next(pe))

# PART2 -- like CSP
# Make each program a generator. At instantiation they are passed code, an input stack (list) and program number.
# when a snd() happens, they yield ('snd', dest, value). When rcv occurs, yield ('rcv', p). If the generator is 
# invoked again after a rcv, this signals a value is waiting on the input stack.
# The control flow runner routes yielded values and declares deadlock appropriately. Similar to the asyncio 
# runner.

def evaluate2(code, p, input_stack):
	instrs = [ j.split(' ') for j in code.split('\n') ]
	pc = 0
	regs = { 'p': p}
	def regv(v):
		if (v[0] >= '0' and v[0] <= '9') or v[0] == '-':
			return int(v)
		return regs.get(v, 0)
	while pc >= 0 and pc < len(instrs):
		instr = instrs[pc]
		# print('{} @ {}:  {}  {}'.format(p, pc, instr, regs))
		offset = 1
		if instr[0] == 'set':
			regs[instr[1]] = regv(instr[2])
		elif instr[0] == 'add':
			regs[instr[1]] = regv(instr[1]) + regv(instr[2])
		elif instr[0] == 'mul':
			regs[instr[1]] = regv(instr[1]) * regv(instr[2])
		elif instr[0] == 'mod':
			regs[instr[1]] = regv(instr[1]) % regv(instr[2])
		elif instr[0] == 'jgz':
			if regv(instr[1]) > 0:
				offset = regv(instr[2])
		elif instr[0] == 'rcv':
			yield ('rcv', p)
			v = input_stack.pop(0)
			# print('p{} recieved {}'.format(p, v))
			regs[instr[1]] = v
		elif instr[0] == 'snd':
			yield ('snd', 1-p, regv(instr[1]))
		else:
			raise Exception(instr)
		pc = pc + offset
	yield None

def runner(instr):
	inputs = {}
	runnable = []
	progs = {}

	for p in range(2):
		inputs[p] = list()
		prog = evaluate2(instr, p, inputs[p])
		progs[p] = prog
		runnable.append(prog)

	c = 0
	while runnable:
		# print(runnable)
		# print(inputs)

		prog = runnable.pop(0)
		ps = next(prog)
		print(ps)
		if ps[0] == 'rcv':
			if len(inputs[ps[1]]) > 0:
				runnable.append(prog)

		elif ps[0] == 'snd':
			runnable.append(prog)
			inputs[ps[1]].append(ps[2])
			# if prog blocked, make runnable
			p = progs[ps[1]]
			if p not in runnable:
				runnable.append(p)

			if ps[1] == 0: # answer counter
				c = c +1
		else:
			raise Exception('else?')

	print(c)

p2script = """snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d"""

runner(p2script)
runner(instrs)  # not 254
