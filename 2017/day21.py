
sample = """.#.
..#
###"""


pats = """../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#"""

# If the size is evenly divisible by 2, break the pixels up into 2x2 squares, and convert each 2x2 # square into a 3x3 square by following the corresponding enhancement rule.
# Otherwise, the size is evenly divisible by 3; break the pixels up into 3x3 squares, and convert 
# each 3x3 square into a 4x4 square by following the corresponding enhancement rule.

def parserules(rules):
	# rules are for 2s or 3s
	rules2 = {}
	rules3 = {}
	for r in rules.strip().split('\n'):
		match,repl = f.split(' -> ')
		# rotate and flip
		for r in range(4):
			for flip in [True, False]:
				pass

		

	return rules2, rules3



def enhance(pic, rules):
	pic = pic.split('\n')

	return pic


p2 = enhance(sample, pats)
print(p2)



