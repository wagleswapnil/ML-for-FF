#################################################################################################
# The program is the main 'processing unit' of the project in a way                             #
# that it calls all the other programs and is the place where global variables                  #
# are defined. The program can be devided into two major parts: 1. the file parser section      #
# and 2. the neural network section.                                                            #
#                                                                                               #
# The author of this program is:                                                                #
# Swapnil Wagle                                                                                 #
# Max Planck Institute of Colloids and Interfaces, Potsdam, Germany                             #
# E-mail id: swapnil.wagle@mpikg.mpg.de                                                         #
#################################################################################################

#! /usr/env/python

import os
import numpy
from os import path
from file_parser import File_Parser
import network
from network import Network1

# The path for the directory, where all the data is located
path = '/Users/swapnil/Documents/FF_for_swapnil/test'    

# Initialization of the variables
files =[]
atomtypes = []
optypes = []
global i_vectors
global o_vectors

# Reading the atomtypes.txt files, which creates the the index list for the output vectors
f = open('./atomtypes.txt', "r")
i=0
for x in f.readlines():
    data = x.split()
    atomtypes.append(data[0])
    i = i+1
f.close()

# Reading the optypes.txt files, which creates the the index list for the input vectors
i=0
f = open('./optypes.txt', "r")
for x in f.readlines():
    data = x.split()
    optypes.append(data[0])
    i = i+1
f.close()

# The input and output arrays are redeclared as 2-dimensional numpy arrays, 
# where the second dimension (the coloumn index) is the length of the input/output index, 
# i.e. the optypes and atomtypes
i_vectors = numpy.empty([0, len(optypes)], dtype = numpy.float64)
o_vectors = numpy.empty([0, len(atomtypes)*2], dtype = numpy.float64)


# This is the first part of the processing unit, i.e. the files parser, 
# it is an abstract part of the pasring process, in which the files are listed. The path is then 
# sent to another program in the Class 'File_Parser', where it is transformed into numpy arrays 
# based on the indexing of the optyeps and atomtypes lists. The numpy arrays (i_vectors and o_vectors) 
# are utilized further by the neural network, which is introduced in the second part of this program.
i=0
for r, d, f in os.walk(path):
    for file in f:
        if file.endswith(".txt"):
            files.append(os.path.join(r, file))
    for fff in sorted(files):
        if ((os.path.exists(fff)) and (os.path.getsize(fff) == 0)):
#            print ("Warning type 1: File exists but is empty " , fff)
            continue
        elif (not (os.path.exists(fff))):
#            print ("Warning type 2: txt file does not exists" , fff)
            continue
        else:
            txt_filepath = fff
            
        itp_filename = "lipid_" + os.path.splitext(fff)[0].split('_')[-2] + "_" + os.path.splitext(fff)[0].split('_')[-1] + ".itp"
        itp_filepath = os.path.join(os.path.dirname(fff), itp_filename)
        if (os.path.exists(itp_filepath) and (os.path.getsize(itp_filepath)) == 0):
#            print ("Warning type 1: File exists but is empty " , itp_filepath)
            continue
        elif (not (os.path.exists(itp_filepath))):
#            print ("Warning type 2: itp file does not exists" , itp_filepath)
            continue
        else:
            i_vector = numpy.array([len(optypes)], dtype=numpy.float64)
            o_vector = numpy.array([len(atomtypes) * 2], dtype=numpy.float64)            
            instance = File_Parser(txt_filepath, itp_filepath, atomtypes, optypes)
            (i_vector, o_vector) = zip(instance.file_parser(txt_filepath, itp_filepath, atomtypes, optypes))
            i_vectors = numpy.append(i_vectors, i_vector, axis = 0)
            o_vectors = numpy.append(o_vectors, o_vector, axis = 0)
            i= i+1

# This is the second part of the processing unit, i.e. the neural network section.
# The i_vectors and o_vectors obtained from the file_parser section are combined together
# to generate the training data set for the neural network. The training data set is a three-
# dimensional numpy array, which has a structure like:
# [[[input array 1] [output array 1]]
#  [[input array 2] [output array 2]]
#  [[input array 3] [output array 3]]
#  ...]
training_data = numpy.empty([int(len(i_vectors)-1), 2], dtype = numpy.ndarray)
i = 0
for i_vector, o_vector in zip(i_vectors, o_vectors):
    i_vector = i_vector[numpy.newaxis]
    i_vector = i_vector.transpose()
    o_vector = o_vector[numpy.newaxis]
    o_vector = o_vector.transpose()
    if i < len(training_data):
        training_data[i,0] = i_vector
        training_data[i,1] = o_vector
    else:
        test_data = i_vector
    i = i + 1

# This section deals with instancing the Neural Network class (named Network) and calling its methods
# eta is the learning rate, layers_sizes is a list containg the number of neurons in each of the layers with 
# first and last layer being the input and output vectors, respectively.
eta = 1             # Learning Rate
layers_sizes = [len(optypes), 200, len(atomtypes) *2]   # Layer structure: Input Layer, Hidden Layer, Output Layer
network = Network1(layers_sizes)
network.SGD(training_data, 10, 8, eta, test_data)
            
        