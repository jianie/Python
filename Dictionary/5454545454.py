import pickle
def main():
    justices=getDictionary("JusticesDict.dat")
    countstates=createStatesDict(justices)
    displaycount(countstates)
def getDictionary(fileName):
    infile=open(fileName,'rb')
    dictName=pickle.load(infile)
    infile.close()
    return dictName
def createStatesDict(justices):
    states=[]
    for justice in justices:
        states.append(justices[justice]['state'])
    countstates = {}
    for state in states:
        countstates[state] = 0
    for state in states:
        countstates[state] = countstates[state] + 1
    return countstates

def displaycount(countstates):
    Count=sorted(countstates.items(),key=lambda k:k[0])
    print(len(countstates),"states have produced jutices.")
    for item in Count:
        print(" ",item[0],":",item[1])
main()