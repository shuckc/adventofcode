import re
def count(input, t_code=0, t_chars=0):
	for x in [i.strip() for i in input.splitlines()]:
		code = len(x)
		y = re.sub('(\\\\x[\da-f]{2})|(\\\\")|(\\\\\\\\)', '#', x)
		chars = len(y) - 2
		#print(" %s -> %s %d  %d" % (x, y, code, chars))
		t_code += code; t_chars += chars
	return t_code - t_chars

assert count('""\n"abc"\n"aaa\\"aaa"\n"\\x27"') == 12
assert count('"utsgfkm\\\\vbftjknltpthoeo"') == 3

with open('input\day8.txt') as f:
	print count(f.read())

def count_enc(input, t_code=0, t_chars=0):
	for x in [i.strip() for i in input.splitlines()]:
		chars = len(x)
		y = re.sub('"', '##', x)
		y = re.sub('\\\\', '##', y)
		code = len(y) + 2
		print(" %s -> %s %d  %d" % (x, y, chars, code))
		t_code += code; t_chars += chars
	return t_code - t_chars

assert count_enc('""\n"abc"\n"aaa\\"aaa"\n"\\x27"') == 19

with open('input\day8.txt') as f:
	print count_enc(f.read())