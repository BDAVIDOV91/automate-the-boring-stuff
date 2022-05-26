print('How many cats do you have?')
numCats = input()
try:
    if int(numCats) >= 4:
        print('Thats a lot of cats.')
    else:
        print('Thats not that many cats.')
except ValueError:
    print('You did not enter a number.')