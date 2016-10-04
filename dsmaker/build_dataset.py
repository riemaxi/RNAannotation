import sys
import os
from parameter import Parameter

class  DataManager:
        def __init__(self, path):
                self.load(path)

        def load(self,path):
                self.table = {}
                for line in  open(path):
                        line = line.strip().split()
                        self.add( int(line[0]), line[2] )

        def add(self,id, seq):
                self.table[id] = (seq,0)

        def incScore(self, id, min_hth, max_hth):
                entry = self.table[id]
		hits = entry[1] + 1
		if hits>=min_hth and hits<=max_hth:
			del self.table[id]
		else:
                	self.table[id] = (entry[0], hits)

		return hits


	def decompress(self,str):
        	return "".join(  map( lambda x: "{0:04b}".format(int(x,16))[::-1],str ))


	def similar(self,a,b,th):
        	count = 0.0
        	for i in range(len(a)):
                	count += 1.0 if a[i]==b[i] else 0.0
        	return count/len(a) >= th

	def k_similar(self,r,ref,th,k):
        	for i in range(len(ref) - k):
                	if self.similar(r[:k],ref[i:i+k],th):
                        	return True
        	return False



	def find(self,r,k, th, min_hth, max_hth):
		r = self.decompress(r)
                for contig in self.table.items():
                        data = contig[1]
                        ref = self.decompress(data[0])
                        if self.k_similar(r, ref, th, k ):
				hits = self.incScore(contig[0], min_hth, max_hth)
				return (contig[0], len(ref), hits)
                return (0,0,0)


def process(param):
        r = param[0]
        k = param[1]
        th = param[2]
	min_hth = param[3]
	max_hth = param[4]
        dm = param[5]
	id,l,hits =  dm.find(r,k,th,min_hth, max_hth)
	if id and hits>=min_hth and hits<=max_hth:
		return (id,l,hits)

	return (0,0,0)

def flush(data, file):
	file.write(data)
	file.flush()
	

p = Parameter("dsbuilder.")

path = p._("contigs_path")
min_hits_threshold = p.i("min_hits_threshold")
max_hits_threshold = p.i("max_hits_threshold")
sim_threshold =  p.f("sim_threshold")
k = p.i("k")
out_path = p._("out_path")
save_frequency = p.i("save_frequency")

dm = DataManager(path)

#receive reads stream
out = open(out_path,"w")
for line in sys.stdin:
        id, l, hits = process( ( line.strip(), k, sim_threshold, min_hits_threshold, max_hits_threshold, dm ) )
	if id:
		flush( "{0}\t{1}\t{2}\n".format(id,l,hits/float(l)), out )

out.close()

