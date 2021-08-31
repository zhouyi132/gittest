import sys
import gzip
import os
import glob
all_file=glob.glob(sys.argv[1])
for item in all_file:
    if os.path.isfile(item):
        os.remove(item)
    if os.path.isdir(item):
        os.removedirs(item)