import sys
from parameter import Parameter
from common import Dictionary
import math

def add(id, name, cls, lref, data, table ):
	data = eval("{" + data + "}") 
	table[id] = (lref, data, cls, name)

def print_table( table ):
	for item in table.items():
		id = item[0]
		l = item[1][0]
		score = item[1][1]
		cls = item[1][2]
		name = item[1][3]	

		print "{0}\t{1}\t{2}\t{3}".format(name,l,cls,score)

def mean_table( max_len, table):
	mean = {}
	size = float(len(table))
	for item in table.items():
		data = item[1][1]

		for i in range(max_len):
			mean[i] = mean.get(i,0) + data.get(i,0)
	
	return map(lambda x: x/size, mean)			

def stdv_table( mean,  max_len, table):
	stdv = {}
	size = len(table)-1
	for item in table.items():
		data = item[1][1]

		for i in range(max_len):
			stdv[i] = stdv.get(i,0) + math.pow(data.get(i,0) - mean[i],2)
	
	return map(lambda x: math.sqrt(x)/size, stdv)

def feuler_score(size,data, mean, stdv):
	score = 0.0
	for i in range(size):
		d = abs(mean[i] - data.get(i,0))
		score += 1.0 if d<=stdv[i] else 0.0
	
	return score/size
	

def feuler_score_table(max_len, table):
	mean = mean_table(max_len, table)
	stdv = stdv_table(mean, max_len, table)

        for item in table.items():
                id = item[0]
                l = item[1][0]
                data = item[1][1]
		cls = item[1][2]
		name = item[1][3]
		
		score = feuler_score(l, data, mean, stdv)

		table[id] = (l,score,cls,name)
		
	

p = Parameter("feuler.")
dict = Dictionary(p._("dictionary"))

max_len = 0
table = {}
for line in sys.stdin:
	line = line.strip().split("\t")

	if (len(line))>2:
		contig = dict._(int(line[0]))
		
		id = int(line[0])
		name = contig[0]
		cls = contig[2]
		lref = int(line[1])
		data = line[2]
	
		max_len = max(lref, max_len)		

		add(id, name,  cls, lref, data, table )

feuler_score_table(max_len, table)

print_table ( table )
