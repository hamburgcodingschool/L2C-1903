import random

def printMatrix(matrix):


    for i in range(0, len(matrix)):
        line = ""
        for j in range(0, len(matrix[i])):
            if j > 0:
                line += ", "
            line += str(matrix[i][j])
        print(line)


def newRandomMatrix():
    matrix = []

    for i in range(0, 4):
        matrix.append([])
        for j in range(0, 4):
            number = random.randrange(0, 10)
            matrix[i].append(number)

    return matrix


newMatrix = newRandomMatrix()
printMatrix(newMatrix)