import math

def isPrime(number):

    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False

    return True

# prime numbers from 1 to 100

for i in range(1, 101):
    if isPrime(i):
        print(i)


print("--------")

# 1st 100 prime numbers

primeCounter = 0
number = 1

while primeCounter < 100:
    if isPrime(number):
        primeCounter += 1
        print("{}: {}".format(primeCounter, number))
    number += 1