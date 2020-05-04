# RockPaperScissors
'''
1. one game or 3 games - inputMenu 
2. choose from: rock, paper, scissors - inputMenu
3. player == rock:
    rock loose with paper
    rock win with scissors
4. player == paper
    paper loose with scissors
    paper win with rock
5. player == scissors
    scissors loose with rock 
    scissors win with paper
6. playerWins, aIwins --> variables 
7. if 3 games and 2 games the same winner end game
8. again?
'''

# Import modules
import random
import pyinputplus as pyip

# List of possible choices
choices = ['rock', 'paper', 'scissors']

# Welcome screen
print('------------------------------------------------------')
print('--------------Rock--Paper--And--Scissors--------------')
print('------------------------------------------------------')
print('Welcome!')

# Value to main loop, when it will be False, then game is over
game = True

# This function check who is the winner
def checkWin(player, aI):
    winner = ''
    if player == 'rock':
        if aI == 'rock':
            winner = 'tie'
        elif aI == 'paper':
            winner = 'aI'
        else:
            winner = 'player'
    elif player == 'paper':
        if aI == 'paper':
            winner = 'tie'
        elif aI == 'scissors':
            winner = 'aI'
        else:
            winner = 'player'
    else:
        if aI == 'scissors':
            winner = 'tie'
        elif aI == 'rock':
            winner = 'aI'
        else:
            winner = 'player'
    return winner

# This function is one game, return the winner
def game():

        print('--------------------------------------------')
        player = pyip.inputMenu(['rock', 'paper', 'scissors'])
        aI = choices[random.randint(0,2)]
        winner = checkWin(player, aI)
        print('----------------------------------------------')
        print('Your choice: %s   vs   My choice: %s' % (player, aI))
        if winner == 'player':
            print('You win!')
        elif winner == 'aI':
            print('I win!')
        else:
            print('Tie!')
        return winner

# Main Loop
while game:
# Choose how many times player wants to play
    howManyGames = pyip.inputChoice(['one', 'three', '1', '3'], '\nHow many times would you like to play? (one or three): ')
    if howManyGames == 'one' or howManyGames == '1':
        game()
    else:
        playersWin = 0
        aIwin = 0
        for i in range(3):
            winner = game()
            if winner == 'player':
                playersWin += 1
            elif winner == 'aI':
                aIwin += 1
            if playersWin == 2 or aIwin == 2:
                break
        print('-----------------------------------------')
        if playersWin > aIwin:
            print('You win the game!')
        elif playersWin < aIwin:
            print('I win the game!')
        else:
            print('Tie!')
        print('\n-----------------------------------------')
            
    again = pyip.inputYesNo('Play again?')
    if again == 'no':
        game = False
