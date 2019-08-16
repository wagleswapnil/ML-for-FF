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
                continue
            elif ((data[0]=="[") and (data[1]=="atoms") and (data[2]=="]")):
                flag=1
                continue
            elif ((data[0]=="[") and (data[2]=="]")):
                flag = 0
            if ((flag==1) and data[0] != ";" and len(data)):
                i=i+1
                for temp in data:
                    print (temp)
        print ("i=" + str(i))
        f.close()
        
    def parse_txt(path):
        f = open (path, "r")
        print (path)
        for x in f.readlines():
            data=x.split()
            if (len(data) < 3):
                continue
            elif ((data[0]=="[") and (data[1]=="atomtypes") and (data[2]=="]")):
                flag=1
                continue
            elif ((data[0]=="[") and (data[1]=="atoms") and (data[2]=="]")):
                flag=1
                continue
            elif ((data[0]=="[") and (data[2]=="]")):
                flag = 0
            if ((flag==1) and data[0] != ";" and len(data)):
                i=i+1
                for temp in data:
                    print (temp)
        print ("i=" + str(i))
        f.close()        
        
#        def create_dictionary(case, info):         Search for "Python Dictionary" and work on this method to fetch the data and create input and output vectors
            