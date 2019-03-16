
people = []

# people.append("Joe")
# people.append("Max")
# people.append("Martha")
# people.insert(2, "Gloria")
# people.pop(1)
#
# print(people)

counter = 0
while counter < 4:
    counter += 1

    print("Give me a name:")
    name = input("> ")

    people.append(name)

print(people)