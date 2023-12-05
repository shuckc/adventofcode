from common import ai

inp = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""

def cards(inp):
	for l in inp.strip().split("\n"):
		print(l)
		_,rest = l.split(":")
		rest = rest.replace('  ', ' ')
		winners,numbers = rest.strip().split("|")
		winners = list(map(int, winners.strip().split(" ")))
		numbers = list(map(int, numbers.strip().split(" ")))
		print(f" card {winners} {numbers}")
		yield winners, numbers

def p1(inp):
	ptotal = 0
	for win,nums in cards(inp):
		winners = set(nums) & set(win)
		print(winners)
		wlen = len(winners)
		if wlen > 0:
			points = 1<<(wlen-1)
			print(f" {winners} {points}")
			ptotal += points
	return ptotal

ai(p1(inp), 13)
ai(p1(open("day4.txt").read()), 23441)

def p2(inp):
	card_pile = [len(set(win) & set(nums)) for win,nums in cards(inp)]
	card_copies = [1] * len(card_pile)
	for i in range(len(card_pile)):
		winners = card_pile[i]
		for n in range(winners):
			card_copies[i+1+n] += card_copies[i]
	print(card_copies)
	return sum(card_copies)

ai(p2(inp), 30)
ai(p2(open("day4.txt").read()), 5923918)
