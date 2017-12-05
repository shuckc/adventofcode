sample="""0
3
0
1
-3"""
def inc(old):
	return old+1

def mazeiter(inp, fn=inc):
	instructions = [int(i) for i in inp]
	pc = 0
	while pc < len(instructions) and pc >= 0:
		pcn = pc + instructions[pc]
		instructions[pc] = fn(instructions[pc])
		# print('{} {} {}'.format(pc, pcn, instructions))
		pc = pcn
		yield 1

print(sum(mazeiter(sample.split())))

with open('input/day5.txt') as f:
	print(sum(mazeiter(f.read().splitlines())))
	
def part2(old):
	if old >= 3: 
		return old-1
	return old+1

print(sum(mazeiter(sample.split(), fn=part2)))


with open('input/day5.txt') as f:
	print(sum(mazeiter(f.read().splitlines(), fn=part2)))
	
