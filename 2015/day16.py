import re, operator
filt = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0,
		'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1 }

def checkit(opmap):
	with open('input/day16.txt') as f:
		for inst in f.read().splitlines():
			m = re.match('Sue (\d+): (.*)', inst)
			theSue = True
			for x in m.group(2).split(', '):
				k,vstring = x.split(': ')
				v = int(vstring)
				theSue = theSue and opmap[k](filt[k], v)
			if theSue: print inst

d = dict( [ (k,operator.eq) for k in filt.keys()] )
checkit(d)

# In particular, the 'cats' and 'trees' readings indicates that there are greater than that many 
# while the 'pomeranians' and 'goldfish' readings indicate that there are fewer than that many 
d['cats'] = operator.lt
d['trees'] = operator.lt
d['pomeranians'] = operator.gt
d['goldfish'] = operator.gt
checkit(d)
