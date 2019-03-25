import random

def lotto(size, maxNumber):
    if maxNumber < size:
        return []

    myArray = []

    for i in range(0, size):
        x = random.randrange(1, maxNumber + 1)
        while x in myArray:
            x = random.randrange(1, maxNumber + 1)

        myArray.append(x)

    return sorted(myArray)





firstKey = lotto(6, 49)
nextKey = []

counter = 0
while firstKey != nextKey:
    counter += 1
    nextKey = lotto(6, 49)
    if counter % 100000 == 0:
        print(counter)

