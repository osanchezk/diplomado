# This program prints Hello, world!
import time
import os

infolder = r"/home/oksm/sites/python/mppdata/"
keep_phrases = [""]
g = 'GET'
sector = ['energy', 'oilandgas', 'mining', 'health', 'automotive', 'aerospace', 'infrastructure', 'tech', 'entrepreneurs', 'professional-services', 'finance', 'logistics', 'ecommerce', 'digital-transformation', 'agribusiness', 'talent', 'mobility', 'trade-and-investment', 'policyandeconomy']
my_list = []

##Functions
def formatDate(y):
    year = y[0].replace("/", "-")
    return year

with os.scandir(infolder) as filePath:
    for fileName in filePath:
        with open(infolder+fileName.name) as f:
            f = f.readlines()
            print("**********************************************")
            print(infolder+fileName.name)
            print("**********************************************")
            cont = 0;
            ##Creamos el archivo
            #createFile = open ('data.csv','w')
            for line in f:
                for phrase in keep_phrases:
                    if phrase in line:
                        time.sleep(.01)
                        cont = cont + 1;
                        print(fileName.name)
                        print(cont)
                        getDate = line.split("[")[1].split(":")[0]
                        getData = line.split("\"")[1].split("\"")[0]
                        if getData[0:3] == 'GET':
                            r = getData.split(" ")[1].split(" ")[0]
                            if r[0:1] == "/":
                                print(r)
                                s = r.split("/")[1].split("/")[0]
                                if s != "":
                                    if s in sector:
                                        fic = open("data.csv", "a")
                                        print(fileName.name+","+getDate +","+s)
                                        fic.write(getDate +","+s+"\n")
                                        fic.close()
        #createFile.close()
        print("Fin")
