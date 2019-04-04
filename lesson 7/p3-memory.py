#
# def someFunction(number):
#     number = 21
#
# a = 10
# someFunction(a)
# print(a)


person = {
    "name": "Joe",
    "age": 10
}

listOfPpl = []
listOfPpl.append(person)

person["name"] = "Mary"
person["age"] = 21

listOfPpl.append(person)

print(listOfPpl)