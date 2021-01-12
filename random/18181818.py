import random
rockPaperscissors=['rock','paper','scissors']
game=[]
game.append(random.choice(rockPaperscissors))
game.append(random.choice(rockPaperscissors))
print('player1:',game[0])
print('player2:',game[1])
if game[0]==game[1]:
    print("The two players tied")
elif 'rock' in game and 'scissors' in game:
    if game[0]=='rock':
        print("player1 wins.")
    else:
        print("player2 wins.")
elif 'paper' in game and 'scissors'in game:
    if game[0]=='scissors':
        print("player1 wins.")
    else:
        print("player2 wins")
elif 'rock' in game and 'paper' in game:
    if game[0]=='paper':
        print("player1 wins.")
    else:
        print("player 2 wins.")