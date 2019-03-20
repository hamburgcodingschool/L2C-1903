import random

secretNumber = random.randrange(1, 101)
#print(secretNumber) # cheat to win 😝

print("What's your guess?")
userNumber = int(input("> "))

tries = 6
hasWon = True

while userNumber != secretNumber:

    if userNumber > secretNumber:
        print("That's too high!")
    else:
        print("That's too low!")

    tries -= 1

    if tries <= 0:
        hasWon = False
        break

    print("Try again. You have {} try(ies) left".format(tries))
    userNumber = int(input("> "))


if hasWon:
    print("YOU ARE AWESOME YOU WON!")
else:
    print("YOU SUCK!")