def createNewPersonFromInput():
    print("What is the name for the person?")
    name = input("> ")

    print("What is the city for the person?")
    city = input("> ")

    print("What is the age for the person?")
    age = int(input("> "))

    person = {
        "name": name,
        "city": city,
        "age": age
    }

    return person

#POPULATE THE ARRAY
ppl = []
for i in range(0, 3):
    p = createNewPersonFromInput()
    ppl.append(p)


#CALCULATE SOME STUFF
oldest = ppl[0]
totalAges = 0
for i in range(0, len(ppl)):
    totalAges += ppl[i]["age"]

    if ppl[i]["age"] > oldest["age"]:
        oldest = ppl[i]

averageAges = totalAges / len(ppl)

print("The average age is {} and the oldest is {}".format(averageAges, oldest["name"]))
