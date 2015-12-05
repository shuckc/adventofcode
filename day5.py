import requests, os, re

def nice(t):
	three_vowels = re.match('(.*[aeiou]){3,}', t) != None
	consecutive = re.compile(r".*(.)\1").match(t) != None
	bads = re.match( '.*(ab|cd|pq|xy)', t) != None
	# print ('text %s:  3v %s  consec %s  bads %s' % (t, three_vowels, consecutive, bads))
	return three_vowels and consecutive and not bads
assert nice('ugknbfddgicrmopn')
assert nice('aaa')
assert nice('jchzalrnumimnmhp') == False
assert nice('haegwjzuvuyypxyu') == False
assert nice('dvszwmarrgswjxmb') == False
assert nice('xy') == False

def part2_nice(t):
	pair_twice = re.match(r".*(.)(.).*\1\2", t) != None
	rept_between = re.match(r".*(.)(.)\1", t) != None
	return pair_twice and rept_between
assert part2_nice('qjhvhtzxzqqjkmpb')
assert part2_nice('xxyxx')
assert part2_nice('uurcxstgmygtbstg') == False
assert part2_nice('ieodomkazucvgmuy') == False

t = requests.get('http://adventofcode.com/day/5/input', cookies=dict(session=os.environ['ADVENT_SESSION'])).text
print '(1) Nice words %d' % sum(nice(line) for line in t.splitlines())
print '(2) Nice words %d' % sum(part2_nice(line) for line in t.splitlines())
