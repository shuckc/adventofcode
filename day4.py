import hashlib, itertools, sys
key='ckczppom'
for target in ['0'*5, '0'*6]:
    for count in itertools.count():
        md = hashlib.md5()
        md.update(key + str(count))
        hd = md.hexdigest()
        if hd.startswith(target):
            print('Target {0} Count {1}, hash {2}'.format(target, count, hd))
            break
