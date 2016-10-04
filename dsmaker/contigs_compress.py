import sys
import string

def compress(str):
        code = ""
        for i in range(0,len(str),4):
                code += "{0:x}".format(int(str[i:i+4][::-1],2)).upper()
        return code

for line in sys.stdin:
        entry = line.split()
        print "{0} {1} {2}".format(entry[0], entry[1], compress(entry[2]) )
