import math

# ask the user for a number
# tell the user if that number is prime or not

number = 10

# print(number % 2)
# print(number % 3)
# print(number % 4)
# print(number % 5)
# print(number % 6)
# print(number % 7)
# print(number % 8)
# print(number % 9)

# zeroModulusCounter = 0
# for i in range(2, number):
#     if number % i == 0:
#         zeroModulusCounter += 1
#         break
#
# if zeroModulusCounter == 0:
#     print("MY FRIEND YOU HAVE A PRIME NUMBER")
# else:
#     print("not a prime")

isPrime = True
# for i in range(2, int(math.sqrt(number)) + 1): #checking until the square root is enough
for i in range(2, number):
    if number % i == 0:
        isPrime = False
        break

if isPrime:
    print("MY FRIEND YOU HAVE A PRIME NUMBER")
else:
    print("not a prime")

