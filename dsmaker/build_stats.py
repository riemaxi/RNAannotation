import sys
from parameter import Parameter
from common import Dictionary

def add(id,cls, lref, data, table ):
	data = eval("{" + data + "}") 
	table[id] = (lref, data)

def print_table( max_len, table, out_path):
	for item in table.items():
		id = item[0]
		l = item[1][0]
		data = item[1][1]

		for i in range(max_len):
			print "c{0}\t{1}\t{2}".format(id,i, data.get(i,0) )

p = Parameter("statistics.")
out_path = p._("out_path")
width = p.i("width")
mdh = p.i("mdh") # max differential height
k = p.i("k")
dict = Dictionary(p._("dictionary"))

max_len = 0
table = {}
for line in sys.stdin:
	line = line.strip().split("\t")

	if (len(line))>2:
		contig = dict._(int(line[0]))
		
		id = int(line[0])
		cls = contig[2]
		lref = int(line[1])
		data = line[2]
	
		max_len = max(lref, max_len)		

		add(id,cls, lref, data, table )

print_table ( max_len, table, out_path)
