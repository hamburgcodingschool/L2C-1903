


def myAwesomeReverseFunction(word):

    reverseWord = ""

    for i in range(0, len(word)):
        mirrorPos = len(word) -i -1
        mirrorLetter = word[mirrorPos]

        reverseWord += mirrorLetter

    return reverseWord



rev = myAwesomeReverseFunction("pokemon")
print(rev)


name = "i dunno"

if name == myAwesomeReverseFunction(name):
    print("It is a palindrome!")
else:
    print("try again")
