import re
def iter(inp):
	xs = ['%d%s' % (len(m.group(0)), m.group(0)[0]) for m in re.finditer(r"(\d)\1*", inp)]
	#print xs
	r = ''.join(xs)
	#print r
	return r

assert iter('1') == '11'
assert iter('11') == '21'
assert iter('21') == '1211'
assert iter('1211') == '111221'
assert iter('111221') == '312211'

x = '1113122113'
for i in range(50):
	x = iter(x)
print len(x)