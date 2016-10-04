import sys
import os
from parameter import Parameter

p = Parameter("stream.reads.")

reads_1 = p._("1")
reads_2 = p._("2")

os.system("paste -d '\n' {0} {1}".format(reads_1, reads_2))
