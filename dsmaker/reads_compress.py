import sys
import string

def compress(str):
        code = ""
        for i in range(0,len(str),4):
                code += "{0:x}".format(int(str[i:i+4][::-1],2)).upper()
        return code

for line in sys.stdin:
        line = line.strip()
        print compress(line)


