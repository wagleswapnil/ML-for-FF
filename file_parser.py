import numpy
numpy.set_printoptions(suppress=True)

class File_Parser(object):    

    global o_vector
    global i_vector
    global atomnames
    o_vector = numpy.empty((82,2))
    i_vector = numpy.empty(82)
    atomnames = ['' for atomnames in range(82)]
    
    
    def __init__(self, path, id):
        self.id = id
        self.path= path
        
    def txt_parser(self, path):
        File_Parser.parse_txt(path)

    def itp_parser(self):
        File_Parser.parse_itp(self.path)
        
    def parse_txt(path):
        f = open (path, "r")
        print (path)
        for x in f.readlines():
            data=x.split()
            if (len(data)==5):
                for temp in data:
                    print (temp)
        f.close()
    
    def parse_itp(path):
        f = open (path, "r")
        flag = 0
        content = []
        print (path)
        for x in f.readlines():
            data=x.split()
            if (len(data) < 3):
                continue
            elif ((data[0]=="[") and (data[1]=="atomtypes") and (data[2]=="]")):
                flag=1
                sign="atomtypes"
                continue
            elif ((data[0]=="[") and (data[1]=="atoms") and (data[2]=="]")):
                flag=1
                sign="atoms"
                continue
            elif ((data[0]=="[") and (data[2]=="]")):
                flag = 0
            if ((flag==1) and data[0] != ";" and len(data)):
                x = x + sign
                content.append(x)
        File_Parser.create_vectors(content)
        f.close()
        
    def parse_txt(path):
        f = open (path, "r")
        print (path)
        i=0
        content=[]
        for x in f.readlines():
            data=x.split()
            if ((data[0]=="fitness") or (data[0]=="final")):
                continue
            else:
                sign = "out"
                x = x + sign
                content.append(x)
        File_Parser.create_vectors(content)
        print ("i=" + str(i))
        f.close()        
        
    def create_vectors(info):
        j=0
        for line in info:
            y = line.split()
            if (y[-1] == "atoms" or y[-1] == "atomtypes"):
                if (y[-1] == "atomtypes"):
                    if (y[0] in atomnames):
                        print ("double entry" + y[0])
                    else:
                        atomnames[j] = y[0]
                        o_vector[j][0] = round(float(y[5]),6)
                        j = j+1
                elif (y[-1] == "atoms"):
                    if (y[1] in atomnames):
                        index = atomnames.index(y[1])
                        o_vector[index][1] = round(float(y[6]),3)
                    else:
                        print ("atomname not found in 'atoms' section")
                        print (y[1])
            elif (y[-1] == "out"):
                i_vector[j] = round(float(y[3]),3)
        print (atomnames)
        print (i_vector)
        print (o_vector)
        
    
