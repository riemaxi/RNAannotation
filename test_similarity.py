import sys
import string
import random

def to_binary(str, one):
	bin = "".join( map( lambda x: "{0}".format(int(string.find(one,x)>-1)), str ) )
	rest = len(bin) % 4
	if rest>0:
		return bin + "0000"[rest:]
	else:
		return bin

def compress(str):
        code = ""
        for i in range(0,len(str),4):
                code += "{0:x}".format(int(str[i:i+4][::-1],2)).upper()
        return code

def decompress(str):
	return "".join(  map( lambda x: "{0:04b}".format(int(x,16))[::-1],str ))


def similar(a,b,th):
        count = 0.0
        for i in range(len(a)):
                count += 1.0 if a[i]==b[i] and a[i]=="1"  else 0.0
        return count/len(a) >= th

def k_similar(r,ref,th,k):
        for i in range(len(ref) - k):
                if similar(r[:k],ref[i:i+k],th):
                        return True
        return False

def random_seq(size):
        letter = "ACGT"
        return "".join( map(lambda x: letter[random.randint(0,3)]  , range(size) ) )

argl = len(sys.argv)

one = "CG" if argl < 7 else  sys.argv[6]
cases = 999 if argl < 2 else int(sys.argv[1])
seqlen = 20 if argl < 3 else int(sys.argv[2])
r = "ACGT" if argl < 4 else sys.argv[3]
k = 4 if argl < 5 else int(sys.argv[4])
th = 0.5 if argl < 6 else float(sys.argv[5])

print one
print cases
print seqlen
print r
print k
print th

count = 0
r = compress(to_binary(r,one))
for i in range(cases):
        seq = compress(to_binary(random_seq(seqlen), one))
        sim = k_similar(decompress(r), decompress(seq),th,k)

        print "{0} {1} {2}".format(sim, decompress(r), decompress(seq))
	
	count += 1 if sim else 0

print "similar: {0}".format(count)


def assert_compare(a,b, one,k,th, valid, message):
        ca = compress(to_binary(a,one))
        cb = compress(to_binary(b,one))

        status = "ok" if k_similar( decompress(ca), decompress(cb),th,k ) == valid else "fail"

	print "{2}({3}) {0}<>{1}".format(a,b,status, message)

assert_compare("GGGG","AAAAAGGGGAAAA", "CG",4, 0.6, True, "found")
assert_compare("GGCCC","AAAAAGGGGCCCATTT", "CG",4, 0.6, True, "found")
assert_compare("ATTA","AAAAAGGGGAAAA", "CG",4, 0.6, False, "not found")
assert_compare("CTCT","AAAAAGGGGAAAA", "CG",4, 0.6, False, "not found")

