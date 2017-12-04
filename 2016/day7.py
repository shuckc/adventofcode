import re

def has_tls(text):
	r = any([p.group()[0] != p.group()[1] for p in re.finditer('(\w)(\w)\\2\\1', text) ])
	print('has {} = {}'.format(text, r))
	return r

def support_tls(test):
	return has_tls(test) and all([not has_tls(p.groups()[0]) for p in re.finditer('.*?\\[(.*?)\\]', test) ])

def check(test, exp):
	found = support_tls(test)
	print('{} expected {} got {}'.format(test, exp, found))

check('abba[mnop]qrst', True) #supports TLS (abba outside square brackets).
check('abcd[bddb]xyyx', False) #does not support TLS (bddb is within square brackets, even though xyyx is outside square brackets).
check('aaaa[qwer]tyui', False) #does not support TLS (aaaa is invalid; the interior characters must be different).
check('ioxxoj[asdfgh]zxcv[bn]hh', True) #supports TLS (oxxo is outside square brackets, even though it's within a larger string).

# how many lines in file pass check?
with open('day7-input.txt') as f:
	print(sum([1 if support_tls(line) else 0 for line in f.read().splitlines() ]))

# Part 2
# ABA outside of [] and BAB inside of []
def chunks(test, want_inside=True):
	inside = False
	for p in re.split(r'([\[\]])', test):
		if p == '[':
			inside = True
		elif p == ']':
			inside = False
		else:
			if inside == want_inside:
				yield p

def candidate_aba(chunk):
	for i in range(0, len(chunk) - 2):
		c = ''.join([chunk[i], chunk[i+1], chunk[i+2]])
		if c[0] != c[1] and c[0] == c[2]:
			yield c

def find_ssl(text):
	print('== {} =='.format(text))
	for c in chunks(text, False):
		for aba in candidate_aba(c):
			bab = ''.join([aba[1], aba[0], aba[1]])
			print(' {}->  {}'.format(aba, bab))
			for c3 in chunks(text, True):
				print('looking for {} in {}'.format(bab, c3))
				if bab in c3:
					return True
	return False

print(find_ssl('qaba[bab]xyz'))
print(find_ssl('qabaqqqss[bac]xyz[aba]'))
print(find_ssl('zazbz[bzb]cdb'))

with open('day7-input.txt') as f:
	print(sum([1 if find_ssl(line) else 0 for line in f.read().splitlines() ]))


