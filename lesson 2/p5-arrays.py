
people = ["Markus", "Julia", "Max", "Helder"]

# print(people[0])
# print(people[1])
# print(people[2])
# print(people[3])

people[1] = "Julez"

counter = 0
while counter < len(people):
    # print(str(counter + 1) + ": " + people[counter])
    print("{}: {}".format(counter + 1, people[counter]))
    counter += 1