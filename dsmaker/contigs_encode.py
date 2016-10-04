import sys
import string
from  parameter import Parameter

def to_binary(str, one):
        bin = "".join( map( lambda x: "{0}".format(int(string.find(one,x)>-1)), str ) )
        rest = len(bin) % 4
        if rest>0:
                return bin + "0000"[rest:]
        else:
                return bin

p = Parameter("encode.")

path = p._("dictionary")
one = p._("one")

# load dictionary
file = open(path)
code = {}
for line in file:
        entry = line.split("\t")
        code[entry[0]] = (entry[1], entry[2])
file.close()

for line in sys.stdin:
        entry = line.split()
        c = code[entry[0]]
        print "{0} {1} {2}".format(c[1].strip(), c[0], to_binary(entry[1], one)  )

