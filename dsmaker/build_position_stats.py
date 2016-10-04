import sys

hit = {}
for line in sys.stdin:
	entry = line.strip().split()
	pos = int(entry[1])
	value = int(entry[2])
	hit[pos] = hit.get(pos,0) + value

for p,v in hit.items():
	print "{0}\t{1}".format(p,v)
