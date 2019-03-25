import math

def isPrime(number):

    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False

    return True

def listOfPrimes(size):
    list = []

    number = 1

    while len(list) < size:
        if isPrime(number):
            list.append(number)
        number += 1

    return list

def listOf100Primes():
    return listOfPrimes(100)

print(listOf100Primes())