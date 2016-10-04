import sys

def print_items(items, f):
	for key,value in items:
		print "{0}\t{1}".format(key,f(value))

lenXscore = {}
classXscore = {}
classXlen = {}
count = 0
for line in sys.stdin:
	entry = line.strip().split()
	cls = entry[2]
	len = int(entry[1])
	score = float(entry[3])

	lenXscore[len] = lenXscore.get(len,0) + score
	classXscore[cls] = classXscore.get(cls,0) + score
	classXlen[cls] = classXlen.get(cls,0) + len

	count += 1

print_items(lenXscore.items(), lambda x: x)

print "classXscore"
print_items(classXscore.items(), lambda x:x)

print "classXlen"
print_items(classXlen.items(), lambda x: x/float(count))
