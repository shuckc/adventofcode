import re

script = """value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2
"""

class Bot():
	def __init__(self, bot_num):
		self.low = None
		self.high = None
		self.values = []
		self.bot_num = bot_num
	def wire(self, low=None, high=None):
		self.low = low
		self.high  = high
		self.push()
	def add_value(self, value):
		self.values.append(value)
		self.push()
	def push(self):
		if len(self.values) == 2 and self.low and self.high:
			self.low.add_value(min(self.values))
			self.high.add_value(max(self.values))

class Output():
	def __init__(self, output_num):
		self.id = output_num
	def add_value(self, value):
		print('output {} gets value {}'.format(self.id, value))
		self.value = value

def displaymatch(match):
    if match is None:
        print('None')
    print('<Match: %r, groups=%r>' % (match.group(), match.groups()))


def build_bots(script, haystack=[2,3]):
	bots = {} # bots by number
	outputs = {}

	def get_or_create_bot(num):
		bot = bots.get(num)
		if not bot:
			bot = Bot(num)
			bots[num] = bot
		return bot

	def get_or_create_output(num):
		out = outputs.get(num)
		if not out:
			out = Output(num)
			outputs[num] = out
		return out

	for line in script.splitlines():
		print(line)
		vb = re.match('value (\d+) goes to bot (\d+)', line)
		wi = re.match('bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)', line)
		if vb:
			get_or_create_bot(vb.groups()[1]).add_value(int(vb.groups()[0]))
		elif wi:
			lowfn = get_or_create_bot if wi.groups()[1] == 'bot' else get_or_create_output
			highfn = get_or_create_bot if wi.groups()[3] == 'bot' else get_or_create_output
			get_or_create_bot(wi.groups()[0]).wire(lowfn(wi.groups()[2]), highfn(wi.groups()[4]))
		else:
			raise Exception('No match {}'.format(line))

	for b in bots.values():
		if sorted(b.values) == haystack:
			print('found bot {} with {}'.format(b.bot_num, b.values))
	#print(sorted(b.values))
	# part 2

	print('mult {}'.format(outputs['0'].value * outputs['1'].value * outputs['2'].value))

build_bots(script)

with open('day10-input.txt') as f:
	build_bots(f.read().strip(), haystack=[17, 61])

