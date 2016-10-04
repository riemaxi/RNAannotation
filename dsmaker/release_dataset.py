import sys
from parameter import Parameter
from common import Dictionary

p = Parameter("release.")

release = p._("path")
dic = Dictionary( p._("dictionary") )

for line in sys.stdin:
	entry = line.strip().split("\t")
	
	id = int(entry[0])
	l = int(entry[1])
	score = entry[2]

	contig = dic._(id)
	name = contig[0]
	cls = contig[2]

	print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}".format(id,name,cls,contig[1],l,score)

