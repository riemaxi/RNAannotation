import sys
import string
from parameter import Parameter

def to_binary(str, one):
        bin = "".join( map( lambda x: "{0}".format(int(string.find(one,x)>-1)), str ) )
        rest = len(bin) % 4
        return bin + "0000"[rest:]

p = Parameter("encode.reads.")

one = p._("one")

for line in sys.stdin:
        line = line.strip()
        print to_binary(line, one)
