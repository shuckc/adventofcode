

def parse(text):
	nested = 1
	garbage = False
	gchars = 0
	skipping = False
	for i, c in enumerate(text):
		if skipping:
			skipping = False
			continue
		elif c == '!':
			skipping = True
		elif c == '<' and not garbage:
			garbage = True
		elif c == '>' and garbage:
			garbage = False
		elif garbage:
			gchars = gchars + 1
		elif c == '{':
			yield (1,nested, 0)
			nested = nested + 1
		elif c == '}':
			nested = nested - 1
		elif c == ',':
			# comma between groups ignored
			pass
		else:
			raise Exception('What is this "{}" at pos {} in {}'.format(c, i, text))
	yield (0,0,gchars)

def c(text, groups, score):
	bits = list(parse(text))
	g = sum(b[0] for b in bits)
	s = sum(b[1] for b in bits)
	gc = sum(b[2] for b in bits)
	if groups != None and g != groups:
		raise Exception('groups {} target {} got {}'.format(text, groups, s))
	if score != None and s != score:
		raise Exception('score {} target {} got {}'.format(text, groups, s))
	print('{} groups: {} got {}, score: {} got {}, gchars {}'.format(text, groups, g, score, s, gc))

c('{}', 1, 1) # group.
c('{{{}}}', 3, 6) # groups.
c('{{},{}}', 3, 5) # also 3 groups.
c('{{{},{},{{}}}}', 6, 16) # groups.
c('{<{},{},{{}}>}', 1, 1) # group (which itself contains garbage).
c('{<a>,<a>,<a>,<a>}', 1, None) # group.
c('{{<a>},{<a>},{<a>},{<a>}}', 5, None) # groups.
c('{{<!>},{<!>},{<!>},{<a>}}', 2, None) # groups (since all but the last > are canceled).

c('{{<ab>},{<ab>},{<ab>},{<ab>}}', 5, 9) #, score of 1 + 2 + 2 + 2 + 2 = 9.
c('{{<!!>},{<!!>},{<!!>},{<!!>}}', 5, 9) #, score of 1 + 2 + 2 + 2 + 2 = 9.
c('{{<a!>},{<a!>},{<a!>},{<ab>}}', 2, 3) #, score of 1 + 2 = 3.
c('<{!>}>', 0, 0)
c('<{o"i!a,<{i<a>', 0, 0)

with open('input/day9.txt') as f:
	bits = list(parse(f.read().strip()))
	g = sum(b[0] for b in bits)
	print(sum(b[1] for b in bits))
	print(sum(b[2] for b in bits))


