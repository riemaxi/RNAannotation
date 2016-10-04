import sys
import os
from parameter import Parameter
import random

class  DataManager:
        def __init__(self, path, out_path, limit):
		self.out_path = out_path
                self.load(path, limit)

        def load(self,path, limit):
                self.table = {}
                for line in  open(path):
                        line = line.strip().split()
                        self.add( int(line[0]), line[2] )
			limit -= 1
			if limit <= 0:
				break

	def pack(self,data):
		return ",".join(  map(lambda(x,y): "{0}:{1}".format(x,y) , data.items() ) )	

	def save(self):
		with open(self.out_path,"w") as out:
			for item in self.table.items():
				data = self.pack( item[1][2] )
				out.write( "{0}\t{1}\t{2}\n".format(item[0], item[1][3], data) )
			out.flush()

        def add(self,id, seq):
                self.table[id] = (seq,0, {}, len(self.decompress(seq)))

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
                        	return i
        	return -1

	def update(self,r,k, th):
		rd = self.decompress(r)
                for contig in self.table.items():
                        data = contig[1]
                        ref = self.decompress(data[0])
                        pos = self.k_similar(rd, ref, th, k )
			if pos>-1:
				try:
					data[2][pos] = data[2][pos] + 1
				except:
					data[2][pos] = 1

				self.table[contig[0]] = (data[0], data[1] + 1, data[2], data[3] )
				
				sys.stdout.write( "{0} {1} {2}\r".format(r, contig[0], pos) )
				sys.stdout.flush()

def process(param):
        r = param[0]
        k = param[1]
        th = param[2]
        dm = param[3]
	dm.update(r,k,th)

def flush(dm):
	print "saving ...\n"
	dm.save()

def jump(current, limit):
	return current + random.randint(1,limit)

p = Parameter("dsbuilder.")

path = p._("contigs_path")
sim_threshold =  p.f("sim_threshold")
k = p.i("k")
css = p.i("contigs_sample_size")
rss = p.i("reads_sample_size")
rrj = p.i("reads_random_jump")
save_frequency = p.i("save_frequency")
out_path = p._("out_path")

dm = DataManager(path, out_path, css)

print "processing {0} contigs and {1} reads".format(css,rss)

#receive reads stream
count = 0
pos = 0
random_pos = jump(pos,rrj)
for line in sys.stdin:
	line = line.strip()
	pos += 1

	if pos != random_pos:
		continue
	else:
		random_pos = jump(pos,rrj)
	
	count += 1
	print "{0} {1}: ".format(pos,count)

        process( ( line, k, sim_threshold, dm ) )
	
	if count == rss:
		flush(dm)
		break

	if count % save_frequency == 0:
		flush(dm)

