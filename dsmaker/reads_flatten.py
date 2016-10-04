import sys
import string
from parameter import Parameter

def get_score(str, shift):
        sum = 0
        for ch in str:
                sum += (ord(ch) - shift)

        return sum/len(str)

p = Parameter("flatten.reads.")

score_thredhold = p.i("threshold")
score_shift = p.i("shift")

seq_symbol = "@"
qual_symbol = "+"

data = ""
state = -1 
# -1 = start, 0 = sequence, 1 = phred

read_no = 1
score = -1
for line in sys.stdin:
        if line.startswith(qual_symbol):
                state = 1
                continue

        if state == 1:
                score = get_score(line[1:], score_shift)

        if state == 0:
                data += string.strip(line) + " "

        if state == 1 and len(data)>0:
                if score >= score_thredhold:
                        print "{0}".format(data[1:].split()[1])
                        read_no += 1

                data = ""
                state = 0

        if line.startswith(seq_symbol):
                data = string.strip(line) + " "
                state = 0

