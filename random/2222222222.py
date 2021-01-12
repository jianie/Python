import random
import pickle
infile=open("DeckOfCardsList.dat",'rb')
deckOfCards=pickle.load(infile)
infile.close()
count = 0
for i in range(1000000):
    random.shuffle(deckOfCards)
    findflag = False
    turn = 0
    for card in deckOfCards:
        turn+=1
        if 'A' in card:
            findflag=True
        if findflag:
            count += turn
            break
abs=count/1000000
print("The average number of cards\nturned up was {0:.2f}.".format(abs))

