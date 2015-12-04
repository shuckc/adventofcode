import hashlib, itertools
md = hashlib.md5('ckczppom')
for target in ['0'*5, '0'*6]:
    for count in itertools.count():
        md2 = md.copy()
        md2.update(str(count))
        hd = md2.hexdigest()
        if hd.startswith(target):
            print('Target {0} count {1}, hash {2}'.format(target, count, hd))
            break
