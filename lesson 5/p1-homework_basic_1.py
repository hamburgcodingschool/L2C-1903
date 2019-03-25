# Write a program that asks the user for a number n and prints the sum of the numbers 1 to n

def addUpTo(number):
    # for i in range(1, number):
    #     number += i
    # return number

    total = 0

    for i in range(1, number + 1):
        total += i

    # total is calculated
    return total

def addUpToMult3_5(number):

    total = 0

    for i in range(1, number + 1):
        if i % 5 == 0 or i % 3 == 0:
            total += i

    return total


print("Hello Mr. user please give me a number")
n = int(input("> "))

t = addUpTo(n)
print(t)