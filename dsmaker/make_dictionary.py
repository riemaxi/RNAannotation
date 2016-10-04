import sys
import string

#table format
#type name id

clscode = {"mRNA" : 1, "ncRNA" : 2, "other" :  100}

print "{0}\t{1}\t{2}".format("mRNA",0,clscode["mRNA"])
print "{0}\t{1}\t{2}".format("ncRNA",0,clscode["ncRNA"])
print "{0}\t{1}\t{2}".format("other",0,clscode["other"])

id = 1
for line in sys.stdin:
	entry = line.split()
	print "{0}\t{1}\t{2}".format(entry[0], clscode[entry[1]], id )
	id += 1
