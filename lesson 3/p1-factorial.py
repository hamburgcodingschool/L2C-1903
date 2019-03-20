
print("Give me a number")
userNumber = int(input("> "))

counter = 0
fact = 1

while counter < userNumber:
    counter += 1 # counter = counter + 1
    fact *= counter # fact = fact * counter

print("{}! = {}".format(userNumber, fact))

