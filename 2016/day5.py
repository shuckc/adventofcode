from itertools import *
import md5

def md5inline(inp):
	m = md5.new()
	m.update(inp)
	return m.hexdigest()
def hashes(doorid):
	return ifilter( lambda x: x.startswith('00000'), imap(lambda x: md5inline(doorid + str(x)), count()))

def findit_p1(doorid):
	print(''.join(map(str, islice( imap(lambda x: x[5], hashes(doorid) ), 8))))

def findit_p2(doorid):
	answer = list('_'*8)
	g = hashes(doorid)
	while '_' in answer:
		a = g.next()
		print a
		pos,value = a[5], a[6]
		if int(pos, base=16) < 8 and answer[int(pos)] == '_':
			answer[int(pos)] = value
		print(''.join(answer))

# findit_p1('abc')
# findit('ugkcyxxp')
# findit_p2('abc')
findit_p2('ugkcyxxp')
