ages = [40, 25, 34, 48, 18]

counter = 0
total = 0

while counter < len(ages):
    total += ages[counter]  #total = total + ages[counter]

    counter += 1

print(total)

average = total / len(ages)

print(average)

# Homework
# find out the highest value in the array and print it
# find out the lowest value in the array and print it

highest = ages[0]
lowest = ages[0]

counter = 0
while counter < len(ages):

    if ages[counter] > highest:
        highest = ages[counter]

    if ages[counter] < lowest:
        lowest = ages[counter]

    counter += 1

print("H: " + str(highest))
print("L: " + str(lowest))