import math

def sayHi(name):
    if name == "Max":
        print("HEEEYYYY MAX!!!!!!!!")
    else:
        print("Hello {}!".format(name))


sayHi("Markus")
sayHi("Julia")
sayHi("Max")


def theSum(a, b):
    result = a + b
    print(result)

theSum(6, 12)



def circlePerimeter(radius):
    per = radius * 2 * math.pi
    print(per)

def circleArea(radius):
    # area = radius * radius * math.pi
    area = math.pow(radius, 2) * math.pi
    print(area)

circlePerimeter(3)
circleArea(3)