def main():
    winnerslist=getlistfromfile("Rosebowl.txt")
    wins=creatfreqdict(winnerslist)
    displaywinners(wins)

def getlistfromfile(filename):
    infile=open(filename)
    winnerslist=[line.rstrip() for line in infile]
    return winnerslist
def creatfreqdict(winnerslist):
    wins={}
    for winner in winnerslist:
        wins[winner]=0
    for winner in winnerslist:
        wins[winner]+=1
    return wins
def displaywinners(wins):
    print("Teams with four or more\n Rose Bowl wins as of 2014:")
    winnersslist=[(winner,wins[winner]) for winner in wins if wins[winner]>=4]
    winnersslist.sort(key= lambda x: x[1],reverse=True)
    print (winnersslist)
    for item in winnersslist:
        print(" ",item[0],":",item[1])
main()