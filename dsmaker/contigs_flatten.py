import string
from  parameter import Parameter

p = Parameter("flatten.")

len_min  = p.i("minsize")
len_max  = p.i("maxsize")

seq_symbol = ">"

data = ""
head = ""
for line in sys.stdin:
        line = line.strip()
        if line.startswith(seq_symbol):
                ldata = len(data)
                if ldata:
                        if ldata <= len_max and ldata >= len_min:
                                print "{0} {1}".format(head,data)
                        data = ""

                head = line.split()[0][1:]
        else:
                data += string.strip(line)

