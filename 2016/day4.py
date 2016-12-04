import re, collections

def score(r):
	room,sector,chksum = re.match('([-a-z]+)(\d+)\[(\w+)\]', r).group(1,2,3)
	charcount = collections.defaultdict(int)
	for c in room:
		charcount[c] += 1
	del charcount['-']
	result = sorted(charcount.iteritems(), key=lambda x: (-x[1], x[0]))
	checksum_calc = ''.join([ x[0] for x in result[0:5] ])
	# print result, checksum_calc
	decoded_msg = ''.join([ chr( 97 + (ord(c) - 97 + int(sector)) % 26) if c != '-' else ' ' for c in room])
	return int(sector), chksum == checksum_calc, decoded_msg

print(score('aaaaa-bbb-z-y-x-123[abxyz]'))
print(score('a-b-c-d-e-f-g-h-987[abcde]'))
print(score('not-a-real-room-404[oarel]'))
print(score('totally-real-room-200[decoy]'))
print(score('qzmt-zixmtkozy-ivhz-343[zimth]'))

total = 0
message = []
with open('day4-input.txt') as f:
	for inst in f.read().splitlines():
		p = score(inst)
		if p[1]:
			total += p[0]
			message.extend(p[2])
			if 'storage' in p[2]:
				print p
print total
