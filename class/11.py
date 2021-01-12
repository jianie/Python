import random
def main():
    nameOfHuman=input("Enter name of human: ")
    h=Human(nameOfHuman)
    nameOfComputer=input("Enter name of computer: ")
    c=Computer(nameOfComputer)
    print()
    for i in range(3):
        humanChoice=h.makeChoice()
        computerChoice=c.makeChoice()
        print("{0} chooses {1}".format(c.getName(),computerChoice))
        if humanChoice=='rock':
            if computerChoice=="scissors":
                h.incrementScore()
            elif computerChoice=="paper":
                c.incrementScore()
        elif humanChoice=="paper":
            if computerChoice=="rock":
                h.incrementScore()
            elif computerChoice=="scissors":
                c.incrementScore()
        else:
            if computerChoice=="rock":
                h.incrementScore()
            elif computerChoice=="paper":
                c.incrementScore()
        print(h,end="  ")
        print(c)
        print()
    if h.getScore()>c.getScore():
        print(h.getName().upper(),"WINS")
    elif c.getScore()>h.getScore():
        print(c.getName().upper(),"WINS")
    else:
        print("TIE")
class Constant():
    def __init__(self,name="",score=0):
        self._name=name
        self._score=score
    def getName(self):
        return self._name
    def getScore(self):
        return self._score
    def incrementScore(self):
        self._score+=1
    def __str__(self):
        return "{0}: {1}".format(self._name,self._score)
class Human(Constant):
    def makeChoice(self):
        choices=["rock","paper","scissors"]
        while True:
            choice=input(self._name+",enter your choice: ")
            if choice.lower() in choices:
                break
        return choice.lower()
class Computer(Constant):
    def makeChoice(self):
        choices = ["rock", "paper", "scissors"]
        selection=random.choice(choices)
        return selection
main()