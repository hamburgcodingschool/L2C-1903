import random

def newRandomMatrix(size, min, max):
    matrix = []

    for i in range(0, size):
        matrix.append([])
        for j in range(0, size):
            number = random.randrange(min, max+1)
            matrix[i].append(number)

    return matrix


def calculateSumMatrixRows(matrix):
    total = []
    for i in range(0, len(matrix)):
        total.append(0)
        for j in range(0, len(matrix[i])):
            total[i] += matrix[i][j]
    return total


def calculateSumMatrixCols(matrix):
    total = []
    for i in range(0, len(matrix)):
        total.append(0)
        for j in range(0, len(matrix[i])):
            total[i] += matrix[j][i]
    return total


def printMatrix(matrix, totalRows, totalCols):

    for i in range(0, len(matrix)):
        line = ""
        for j in range(0, len(matrix[i])):
            if j > 0:
                line += " + "
            line += str(matrix[i][j])
        print("{} = {}".format(line, totalRows[i]))

    line = ""
    for i in range(0, len(matrix)):
        line += "=   "
    print(line)

    line = ""
    for i in range(0, len(matrix)):
        line += "{}   ".format(totalCols[i])
    print(line)