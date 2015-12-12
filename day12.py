import json
def sumit(fn, f):
	return {
	  int: lambda i: i, 
	  dict: lambda d: sum([fn(fn, v) for v in d.values()]),
	  list: lambda l: sum([fn(fn, v) for v in l]),
	  unicode: lambda f: 0,
	}[type(f)](f)

def sumit2(fn, f):
	if type(f) == dict and 'red' in f.values():
		return 0
	return sumit(sumit2, f)

j = json.loads(open('input/day12.txt').read())
print sumit(sumit, j), sumit2(None, j)
