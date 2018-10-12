import itertools
import copy


# xM microchip
# xG generator
# where x is the material A-Z

class Board():
	def __init__(self, layout, e=0):
		# If a chip is left in the same area as generator, and it's not connected
		# to its own generator, the chip will be fried
		self.valid = True
		for i,xs in enumerate(layout):
			gs = set()
			ms = set()
			for x in xs:
				if x[1] == 'G':
					gs.add(x[0])
				elif x[1] == 'M':
					ms.add(x[0])
				else:
					raise
			# remove M protected by own G
			# an G powering an M is still dangerous to other microchips.
			unprotected_chips = ms - gs
			if len(gs) > 0 and len(unprotected_chips) > 0:
				self.valid = False
				self.reason = 'unprotected chips {} on F{}'.format(unprotected_chips, i+1)

		# immutable layout for hashing etc
		self.e = e
		self.layout = tuple([ tuple(x) for x in layout])
		self.floors = len(layout)

	def __hash__(self):
		return self.layout.__hash__() ^ self.e

	def __eq__(self, other):
		return self.layout == other.layout and self.e == other.e

	def print(self):
		s = set()
		for xs in self.layout:
			for x in xs:
				s.add(x)
		ss = sorted(list(s))
		item_col_idx = dict([ (s,i) for i,s in enumerate(ss) ])
		for i,fs in reversed(list(enumerate(self.layout))):
			sp = list('.  ' * len(ss))
			for item in fs:
				c = item_col_idx[item] * 3
				sp[c:c+2] = item
			print(' F{} {}  {}'.format(i+1, 'E' if i==self.e else '.', ''.join(sp)))
		print('   solved: {}'.format(self.solved()))

	def solved(self):
		return all(len(self.layout[i]) == 0 for i in range(self.floors-1))
	def moves(self):
		for m in self.moves_gen():
			mb = self.make_move(m)
			if mb:
				yield (mb, m)

	def make_move(self, m):
		direction, pieces = m
		# make the new board and see if it passes checks
		new_layout = [list(x) for x in self.layout]
		new_fl = self.e + direction
		# self.print()
		for p in pieces:
			new_layout[self.e].remove(p)
			new_layout[new_fl].append(p)

		b = Board(new_layout, e=new_fl)
		if b.valid:
			#print('ok move {} giving result'.format(m))
			#b.print()
			return b
		#print('invalid move {} as {}'.format(m, b.reason))
		return None

	def moves_gen(self):
		dirs = []
		if self.e > 0:
			dirs.append(-1)
		if self.e < self.floors - 1:
			dirs.append(+1)
		# how many items on current floor?
		#  - elevator only functions if it contains one or two items
		items = self.layout[self.e]
		if len(items) == 0:
			self.print()
			raise Exception('No moves from this board!')
		s = itertools.chain( 
			itertools.combinations(items, 2),
			itertools.combinations(items, 1))
		return itertools.product(dirs, s)

#F4 .  .  .  .  .  
#F3 .  .  .  LG .  
#F2 .  HG .  .  .  
#F1 E  .  HM .  LM
sample_layout = [['HM', 'LM'], ['HG'], ['LG'], []]

b = Board(sample_layout)
b.print()
print(list(b.moves_gen()))
assert not(b.solved())

b = Board([[], [], [], ['HM', 'LM','HG','LG']], e=3)
assert(b.solved())
b.print()

b = Board(sample_layout, e=2)
b.print()
# print(list(b.moves()))
assert not(b.solved())
assert list(b.moves_gen()) == [(-1, ('LG',)), (1, ('LG',))]

bs = set([b])
c = Board(sample_layout, e=2)
assert(c in bs)
assert(c == b)

# check opposing moves are detected as same position
b2 = b.make_move( (-1, ('LG',)))
b2.print()
assert(not b2 in bs)
b3 = b2.make_move( (1, ('LG',)))
assert(b3 in bs)

#print('moves are')
#for bx,m in b.moves():
# bx.print()

## container for evaluating a game
def rungame(layout):
	print('starting game')
	b = Board(layout, e=0)
	b.print()
	bfs = [ [(b, None)] ]

	# a slower way to get to a seen state is disgarded
	seen = set([b])
	count = 0
	while bfs:
		if (count & 0xffff) == 0:
			print('{} positions for consideration {} seen boards {}'.format(count, len(bfs), len(seen)))
		count = count+1
		path = bfs.pop(0)
		b,m = path[-1]
		for candidate_board, move in b.moves():
			if candidate_board in seen:
				# print('^ seen result before, discarding')
				continue
			seen.add(candidate_board)
			trail = list(path)
			trail.append( (candidate_board, move) )

			if candidate_board.solved():
				print('** Solved, move history {} moves:'.format(len(trail)-1))
				for b,m in trail:
					print('> move: {}'.format(m))
					b.print()
				return trail

			# re-insert new state and end of queue
			bfs.append( trail )

	raise Exception('bfs empty?')

print(sample_layout)
rungame(sample_layout)

# Get everything to top floor
# If a chip is left in the same area as another RTG, and it's not connected to its own RTG, the chip will be fried
# RTG protects own chip
#  - elevator always stops on each floor. 
#  - - items 'within it' and the items on that floor can irradiate each other.

# states are valid or not
# movements are: up or down, with 1 or 2 items from old floor
#   movement valid if the destination floor with new contents will not be fried
#   movement wins if all items on top floor



# Puzzle input
#The first floor contains 
# PG	a polonium generator, 
# TG TM a thulium generator, a thulium-compatible microchip, 
# OG    a promethium generator, 
# RG RM a ruthenium generator, a ruthenium-compatible microchip, 
# CG CM a cobalt generator, and a cobalt-compatible microchip.
#The second floor contains 
# PM OM a polonium-compatible microchip and a promethium-compatible microchip.
#The third floor contains nothing relevant.
#The fourth floor contains nothing relevant.

#F4 .  .  .  .  .  
#F3 .  .  .  LG .  
#F2 .  HG .  .  .  
#F1 E  .  HM .  LM
puzzle_layout = [['PG', 'TG', 'TM', 'OG', 'RG', 'RM', 'CG', 'CM'], ['PM', 'OM'], [], []]
b = Board(puzzle_layout, e=0)
b.print()
rungame(puzzle_layout)



