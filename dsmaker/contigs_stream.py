from parameter import Parameter

p = Parameter("stream.contigs.")

for line in open(p._("source")):
        print line.strip()

