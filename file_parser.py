class File_Parser(object):
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
        i=0
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
                i=i+1
                File_Parser.create_vectors(sign,data)
        f.close()
        
    def parse_txt(path):
        f = open (path, "r")
        print (path)
        i=0
        
        for x in f.readlines():
            data=x.split()
            if ((data[0]=="fitness") or (data[0]=="final")):
                continue
            else:
                sign = "out"
                File_Parser.create_vectors(sign, data)
        print ("i=" + str(i))
        f.close()        
        
    def create_vectors(case, info):
        i_vector = []
        o_vector = []
        if (case == "atoms" or case == "atomtypes"):
            if (case == "atoms"):
                for i in len(i_vector):
                    if info[1] == items:
                        info[6]=i_vector[1]
                    else:
                        i_vector[:][0].append(info[1])
                        i_vector[:][1].append(info[6])
            if (case == "atomtypes"):
                for i in len(i_vector):
                    if info[0] == items:
                        i_vector[:][2].append(info[5])
                    else:
                        i_vector[:][0].append(info[0])
                        i_vector[:][2].append(info[5])
            elif (case == "atomtypes"):
                i_vector [:][1] = info [5]
        else:
            print (case, len(info))
            print (info)