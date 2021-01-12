import pickle
def main():
    justices=getDictionary("USpresStatesDict.dat")
    states=createStatesDict(justices)
    sortedStates=[state for state in states if states[state]>2]
    sortedStates.sort(key=lambda state:states[state],reverse=True)
    print("States that produced three or\nmore presidents as of 2016:")
    for state in sortedStates:
        print(" ",state+":",states[state])
def getDictionary(fileName):
    infile=open(fileName,'rb')
    dictName=pickle.load(infile)
    infile.close()
    return dictName
def createStatesDict(justices):
    states={}
    for state in justices.values():
        if not states.get(state,False):
            states[state]=1
        else:
            states[state]+=1
    return states
main()