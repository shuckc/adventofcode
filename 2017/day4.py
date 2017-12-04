
def passp(line):
	wc = {}
	for word in line.split():
		if word in wc:
			return False
		wc[word] = 1
	return True

def checkwords(fn=passp):
	with open('input/day4.txt') as f:
		for line in f.read().splitlines():
			good = fn(line)
			# print('{} {}'.format(line, good))
			yield 1 if good else 0

print(sum(checkwords()))

def agram(line):
	wc = {}
	for word_unsort in line.split():
		word = ''.join(sorted(word_unsort))
		if word in wc:
			return False
		wc[word] = 1
	return True

print(sum(checkwords(fn=agram)))
