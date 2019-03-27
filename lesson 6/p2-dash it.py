
def myAwesomeReverseFunction(word):

    reverseWord = ""

    for i in range(0, len(word)):
        mirrorPos = len(word) -i -1
        mirrorLetter = word[mirrorPos]

        reverseWord += mirrorLetter

    return reverseWord

def dashItUp(word):

    dashedWord = ""

    for i in range(0, len(word)):
        if i > 0:
            dashedWord += "-"
        dashedWord += word[i]

    return dashedWord

word = "maximilian"
rev = myAwesomeReverseFunction(word)
dashedRev = dashItUp(rev)

print(dashedRev)