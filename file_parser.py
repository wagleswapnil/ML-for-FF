#################################################################################################
# The class contains the methods used for parsing text from the txt and itp files and generate  #
# input and output vectors (numpy arrays) from the read text.                                   #
#                                                                                               #
# The author of this program is:                                                                #
# Swapnil Wagle                                                                                 #
# Max Planck Institute of Colloids and Interfaces, Potsdam, Germany                             #
# E-mail id: swapnil.wagle@mpikg.mpg.de                                                         #
#################################################################################################

import numpy
numpy.set_printoptions(suppress=True)

# Initialization of the class
class File_Parser(object):    

    def __init__(self, i_path, o_path, atomtypes, optypes):
        self.i_path = i_path
        self.o_path = o_path
        self.atomtypes = atomtypes
        self.optypes = optypes
    
    
    def file_parser(self, i_path, o_path, atomtypes, optypes):
        i_list = (self.parse_txt(i_path))
        o_list = (self.parse_itp(o_path))
        return(self.create_vectors(i_list, o_list, atomtypes, optypes))
    
    def parse_itp(self, path):
        f = open (path, "r")
        flag = 0
        content = []
        for x in f.readlines():
            data=x.split()
            if (len(data) < 3):
                continue
            elif ((data[0]=="[") and (data[1]=="atomtypes") and (data[2]=="]")):
                flag = 1
                sign = "atomtype"
                continue
            elif ((data[0]=="[") and (data[1]=="atoms") and (data[2]=="]")):
                flag = 1
                sign = "atom"
                continue
            elif ((data[0]=="[") and (data[2]=="]")):
                flag = 0
                
            if ((flag==1) and data[0] != ";" and len(data)):
                x = x + sign
                content.append(x)
        f.close()
        return(content)
        
    def parse_txt(self, path):
        f = open (path, "r")
        i=0
        content=[]
        for x in f.readlines():
            data=x.split()
            if ((data[0]=="fitness") or (data[0]=="final")):
                continue
            else:
                content.append(x)
        f.close()        
        return(content)
        
    def create_vectors(self, i_list, o_list, atomtypes, optypes):
        i_vector = numpy.empty(len(self.optypes))
        o_vector = numpy.empty((len(self.atomtypes)*2))
        for line in i_list:
            y = line.split()
            if y[0] in self.optypes:
                i_vector[self.optypes.index(y[0])] = round(float(y[2]), 10)
            else: 
                i_vector[self.optypes.index(y[0])] = numpy.NaN
                print(y[0] + "does not exist in the list of optypes")

        for line in o_list:
            y = line.split()
            if (y[-1] == "atomtype"):
                if y[0] in self.atomtypes:
                    o_vector[self.atomtypes.index(y[0])] = round(float(y[5]),10)
                else:
                    print(y[0] + "does not exist in the list of atomtypes: ATOMTYPE secion")
            elif (y[-1] == "atom"):
                if y[1] in self.atomtypes:
                    o_vector[self.atomtypes.index(y[1]) + len(self.atomtypes)] = round(float(y[6]),5)
                else:
                    print(y[1] + "does not exist in the list of atomtypes: ATOM secion")
            else:
#                print("Check the entry " + line)
                o_vector[self.atomtypes.index(y[0])] = numpy.NaN
                o_vector[self.atomtypes.index(y[0]) + len(self.atomtypes)] = numpy.NaN
        return (i_vector, o_vector)
        
    
