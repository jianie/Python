def main():
    listOfwinners=formlistOfwinners("Rosebowl.txt")
    wins=createFreqDict(listOfwinners)
    displayWinners(wins)
def formlistOfwinners(fileName):
    infile=open(fileName)
    winnerslist=[line.rstrip() for line in infile]
    return winnerslist
def createFreqDict(listOfwinners):
    wins={}
    for winner in listOfwinners:
        wins[winner]=0
    for winner in listOfwinners:
        wins[winner]=wins[winner]+1
    return wins
def displayWinners(wins):
    print("Teams with four or more\nRose Bowl wins as of 2014:")
    winnerslist=[]
    for winner in wins.keys():
        if wins[winner]>=4:
            winnerslist.append((winner,wins[winner]))
    winnerslist.sort(key=lambda x:x[1],reverse=True)
    for item in winnerslist:
        print("  ",item[0],':',item[1])
main()