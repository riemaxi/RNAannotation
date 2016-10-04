import sys
from parameter import Parameter
from common import Dictionary

def reapr_score(l, data, width, mdh,k):
	return data
	
p = Parameter("reapr.")
out_path = p._("out_path")
width = p.i("width")
mdh = p.i("mdh") # max differential height
k = p.i("k")
dict = Dictionary(p._("dictionary"))

max_len = 0
for line in sys.stdin:
	line = line.strip().split("\t")

	if (len(line))>2:
		contig = dict._(int(line[0]))
		
		id = line[0]
		cls = contig[2]
		lref = int(line[1])
		ref = line[2]
	
		max_len = max(lref, max_len)		
		print "{0}\t{1}\t{2}\t{3}".format(id, cls, lref, reapr_score(lref, ref, width, mdh,k))
