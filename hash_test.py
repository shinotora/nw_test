aMap = []

aMap.append('a')
aMap.append('b')

print aMap

def hash_key(aMap, key):
	return hash(key) % len(aMap)

