import math
import random

def circlePerimeter(radius):
    return radius * 2 * math.pi

def circleArea(radius):
    return math.pow(radius, 2) * math.pi


def somethingSilly():

    x = random.randrange(0, 2)
    if x == 0:
        return

    print("I WILL MAYBE BE... 50% chance")


print("What is the radius?")
r = int(input("> "))

area = circleArea(r)
perimeter = circlePerimeter(r)

print("The perimeter is {}".format(perimeter))
print("The area is {}".format(area))