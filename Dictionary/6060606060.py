import pickle
def main():
    state = input("Enter the name of a state: ")
    states=getDictionary("LargeCitiesDict.dat")
    Cities=createCitiesList(states,state)
    displatCities(Cities,state)
def getDictionary(fileName):
    infile=open(fileName,'rb')
    dictName=pickle.load(infile)
    infile.close()
    return dictName
def createCitiesList(states,state):
    Cities=[]
    for x in states:
        if state==x:
            Cities=states[x]
    return Cities
def displatCities(Cities,state):
    if len(Cities)!=0:
        print("Large cities: ", " ".join(Cities))
    else:
        print("There are no large cities in {0:s}".format(state))
main()

