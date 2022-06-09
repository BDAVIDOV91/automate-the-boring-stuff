import random

# clean up for the code
from enum import IntEnum

# user use numbers instead of whole words
class Action(IntEnum):
    rock = 0
    paper = 1
    scissors = 2
    lizard = 3
    spock = 4

victories = {
    Action.scissors: [Action.lizard, Action.paper], # scissors wins
    Action.paper: [Action.spock, Action.rock], # paper wins
    Action.rock: [Action.lizard, Action.scissors], # rock wins
    Action.lizard: [Action.spock, Action.paper], # lizard wins
    Action.spock: [Action.scissors, Action.rock] # spock wins
}
# player selection 
def playerSelection():  
    choices = [f'{action.name}[{action.value}]' for action in Action]  # action ???
    choices_str = ', '.join(choices)  # ???
    selection = int(input(f'Enter a choice ({choices_str}): ')) 
    action = Action(selection)
    return action

# computer selection
def computerSelection():
    selection = random.randint(0, len(Action) - 1)
    action = Action(selection)
    return action


# determine the winner
def determineWinner(playerAction, computerAction):
    defeat = victories[playerAction]
    if playerAction == computerAction:
        print(f"Both players selected {playerAction.name}. It's a tie! ")
    
    elif computerAction in defeat:
        print(f"{playerAction.name} beats {computerAction.name}! Get shit on! ")
    else:
        print(f"{computerAction.name} beats {playerAction.name}! Get shit on! LOSER. ")

#loop for newgame + "except ValueErrror"
while True:
    try:
        playerAction = playerSelection()
    except ValueError as e:
        range_str = f"[0, {len(Action) - 1}]"
        print(f"Invalid selection.Enter a value in range {range_str}")
        continue
    computerAction = computerSelection()
    determineWinner(playerAction, computerAction)

    playAgain = input('Play again? (y/n): ')
    if playAgain.lower() != 'y':
        break