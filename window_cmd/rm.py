import sys
import gzip
import os
import glob
all_file=glob.glob(sys.argv[1])
for item in all_file:
    os.remove(item)