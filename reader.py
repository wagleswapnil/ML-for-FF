#! /usr/env/python

import os
import numpy
from os import path
from file_parser import File_Parser


path= '/Users/wagle/Downloads/FF_for_swapnil/test/head_n_tails2'
files =[]
atomtypes = []
optypes = []
global i_vectors
global o_vectors


f = open('./atomtypes.txt', "r")
i=0
for x in f.readlines():
    data = x.split()
    atomtypes.append(data[0])
    i = i+1
f.close()

i=0
f = open('./optypes.txt', "r")
for x in f.readlines():
    data = x.split()
    optypes.append(data[0])
    i = i+1
f.close()

i_vectors = numpy.empty([0, len(optypes)], dtype=numpy.float64)
o_vectors = numpy.empty([0, len(atomtypes)*2], dtype=numpy.float64)

print(i_vectors.size, o_vectors.size)


#i_vectors = numpy.reshape(i_vectors,(len(optypes),1))
#o_vectors = numpy.reshape(o_vectors,(len(atomtypes),1))

i=0
for r, d, f in os.walk(path):
    for file in f:
        if file.endswith(".txt"):
            files.append(os.path.join(r, file))
    for fff in sorted(files):
        if ((os.path.exists(fff)) and (os.path.getsize(fff) == 0)):
            print ("Warning type 1: File exists but is empty " , fff)
            continue
        elif (not (os.path.exists(fff))):
            print ("Warning type 2: txt file does not exists" , fff)
            continue
        else:
            txt_filepath = fff
            
        itp_filename = "lipid_" + os.path.splitext(fff)[0].split('_')[-2] + "_" + os.path.splitext(fff)[0].split('_')[-1] + ".itp"
        itp_filepath = os.path.join(os.path.dirname(fff), itp_filename)
        if (os.path.exists(itp_filepath) and (os.path.getsize(itp_filepath)) == 0):
            print ("Warning type 1: File exists but is empty " , itp_filepath)
            continue
        elif (not (os.path.exists(itp_filepath))):
            print ("Warning type 2: itp file does not exists" , itp_filepath)
            continue
        else:
            print (txt_filepath, itp_filepath)
            i_vector = numpy.array([len(optypes)], dtype=numpy.float64)
            o_vector = numpy.array([len(atomtypes)*2], dtype=numpy.float64)
            instance = File_Parser(txt_filepath, itp_filepath, atomtypes, optypes)
            (i_vector, o_vector) = zip(instance.file_parser(txt_filepath, itp_filepath, atomtypes, optypes))
            i_vectors = numpy.append(i_vectors, i_vector, axis =0)
            o_vectors = numpy.append(o_vectors, o_vector, axis =0)
            print(i_vectors, o_vectors)
            print(len(i_vectors), len(o_vectors))
            i= i+1
            
        