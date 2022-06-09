import random


# user (actions) input
player = input('Enter a choice (rock, paper, scissors): ')

# computer actions  input
possibleActions = ('rock', 'paper', 'scissors')
computerAction = random.choice(possibleActions)
print(f'\nYou chose {player}, computer chose {computerAction}. \n')

# determine the Winner  if/elif/else functions
# tie
# player pick "rock" ... computer pick "scissors" .. else "paper"

if player == computerAction:
    print(f"Both players selected {player}. It's a tie! ")
elif player == 'rock':
    if computerAction == 'scissors':
        print('Rock smashes scissors! Get shit on! ')
    else:
        print('Paper covers rock! Get shit on LOSER! ')

# player pick "paper" ...computer pick "Rock" ...else "scissors"       

elif player == 'paper':
    if computerAction == 'rock':
        print('Paper covers rock! Get shit on! ')
    else:
        print('Scissors cut paper! Get shit on LOSER! ')

# player pick "scissors"... computer pick "paper"... else "rock"

elif player == 'scissors':
    if computerAction == 'paper':
        print('Scissors cut paper! Get shit on!')
    else:
        print('Rock smashes scissors! Get shit on LOSER!')