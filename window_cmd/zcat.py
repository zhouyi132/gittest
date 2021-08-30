import sys
import gzip
f=gzip.open(sys.argv[1]) 
print(f.read().decode())
f.close()