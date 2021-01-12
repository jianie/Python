import pickle
def main():
    dictname=getdictionary("USpresStatesDict.dat")
    pres=createpreslist(dictname)
    displaypres(pres)
def getdictionary(filename):
    infile=open(filename,'rb')
    dictname=pickle.load(infile)
    infile.close()
    return dictname
def createpreslist(dictname):
    name=input("Enter a first name: ")
    pres=[(president[0],president[1])for president in dictname if name in president[1]]
    return pres
def displaypres(pres):
    pres.sort(key=lambda x:x[1])
    pres.sort(key=lambda x:x[0])
    if len(pres)!=0:
        for item in pres:
            print(" ",item[1],item[0])
    else:
        print("There is no president with that name.")
main()
