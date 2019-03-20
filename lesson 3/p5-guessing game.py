import random

secretNumber = random.randrange(1, 101)
print(secretNumber) # cheat to win 😝

print("What's your guess?")
userNumber = int(input("> "))

while userNumber != secretNumber:
    if userNumber > secretNumber:
        print("That too high!")

    if userNumber < secretNumber:
        print("That too low!")

    print("Try again")
    userNumber = int(input("> "))

print("YOU WON! (but you had no other option really...)")