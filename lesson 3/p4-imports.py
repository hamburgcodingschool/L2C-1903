import random

counter = 0

myArray = []

while counter < 10:
    counter += 1
    x = random.randrange(1, 11)
    myArray.append(x)


print(myArray)
