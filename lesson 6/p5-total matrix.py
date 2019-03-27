import random

def newRandomMatrix():
    matrix = []

    for i in range(0, 4):
        matrix.append([])
        for j in range(0, 4):
            number = random.randrange(1, 4)
            matrix[i].append(number)

    return matrix


def printMatrix(matrix):

    for i in range(0, len(matrix)): # this outer loop, is responsible for the line (inner array)
        total = 0
        line = ""
        for j in range(0, len(matrix[i])): # this inner loop, is responsible for the actual values
            if j > 0:
                line += " + "
            line += str(matrix[i][j])
            total += matrix[i][j]
        # print(line + " = " + str(10))
        print("{} = {}".format(line, total))


    for i in range(0, len(matrix)):
        total = 0
        for j in range(0, len(matrix[i])):
            total += matrix[j][i]
        print(total)


newMatrix = newRandomMatrix()
printMatrix(newMatrix)
