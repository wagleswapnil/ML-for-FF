#! /usr/env/python

import os
from file_parser import File_Parser

i=0 
path= '/Users/wagle/Downloads/FF_for_swapnil/'
files =[]
for r, d, f in os.walk(path):
    for file in f:
        files.append(os.path.join(r,file))

for f in files:
        instance= File_Parser(f, i)
        if f.endswith('.txt'):
            continue
            instance.txt_parser(f)
            break
        elif f.endswith('.itp'):
            instance.itp_parser()
            break
        else:
            print (f)
            continue
        i=i+1
        
