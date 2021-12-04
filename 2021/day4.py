import numpy as np
eg = "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1\n\n" \
	"22 13 17 11  0\n 8  2 23  4 24\n21  9 14 16  7\n 6 10  3 18  5\n 1 12 20 15 19\n\n" \
	" 3 15  0  2 22\n 9 18 13 17  5\n19  8  7 25 23\n20 11 10 24  4\n14 21 16 12  6\n\n" \
	"14 21 17 24  4\n10 16 15  9 19\n18  8 23 26 20\n22 11 13  6  5\n 2  0 12  3  7\n\n"

def boardparse(eg):
	parts = eg.split("\n\n")
	nums = np.array(parts[0].split(","), int)
	boards, called = [], []
	for b in filter(None, parts[1:]):
		boards.append(np.array([b[i:i+2].strip() for i in range(0, len(b), 3)], int).reshape([5,5]))
		called.append(np.zeros((5,5), dtype=bool))
	return nums, boards, called

def play(nums,boards,called):
	for n in nums:
		print("n={} boards={}".format(n, len(boards)))
		xd = []
		for i,(b,s) in enumerate(zip(boards, called)):
			s[b == n] = True
			for check in range(5):
				if all(s[check,:]) or all(s[:,check]):
					print(" completed board i={}".format(i))
					print(b)
					print(s)
					yield n,b,s
					xd.append(i)
					break
		# delete after iteration, and in reverse order by index
		for i in reversed(xd):
			del boards[i]
			del called[i]

def score(src):
	for n, board, called in src:
		score = sum(board[called == False]) * n
		print("n {} score {}".format(n, score))
		yield score

# part 1 - first
print(list(score(play(*boardparse(eg))))[0])
print(list(score(play(*boardparse(open('input/day4.txt').read()))))[0])

#part 2 last
print(list(score(play(*boardparse(eg))))[-1])
print(list(score(play(*boardparse(open('input/day4.txt').read()))))[-1])
