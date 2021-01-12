import pickle
def main():
    presidents=getDictionary("USpresStatesDict.dat")
    Pres=createPresList(presidents)
    displatPtes(Pres)
def getDictionary(fileName):
    infile=open(fileName,'rb')
    dictName=pickle.load(infile)
    infile.close()
    return dictName
def createPresList(presidents):
    Pres=[]
    Name=input("Enter a first name: ")
    for president in presidents:
        if Name in president[1]:
            Pres.append((president[0],president[1]))
    return Pres
def displatPtes(Pres):
    Pres.sort(key=lambda x: x[1])
    Pres.sort(key=lambda x: x[0])
    if len(Pres)!=0:
        for item in Pres:
            print(" ",item[1],item[0])
    else:
        print("There is no president with that name.")
main()

