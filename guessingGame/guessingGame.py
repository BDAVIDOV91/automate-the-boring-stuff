import random
print('Hello.Whats is your name?')
name = input()

print('Well, ' + name + ', I am thinking of a number between 1 and 30.')  
secretNumber = random.randint(1, 30)

for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())
    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Your gues is too high')
    else:
        break


if guess == secretNumber:
    print('Good job, ' + name + '! You guesed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope.The number I was thinking of was ' + str(secretNumber))
