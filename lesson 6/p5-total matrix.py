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



# newMatrix = newRandomMatrix(3, 1, 3)
# calcRows = calculateSumMatrixRows(newMatrix)
# calcCols = calculateSumMatrixCols(newMatrix)
# printMatrix(newMatrix, calcRows, calcCols)



nm = newRandomMatrix(3, 1, 2)
totalR = calculateSumMatrixRows(nm)
totalC = calculateSumMatrixCols(nm)

printMatrix(nm, totalR, totalC)

# def printMatrix(matrix):
#
#     for i in range(0, len(matrix)): # this outer loop, is responsible for the line (inner array)
#         total = 0
#         line = ""
#         for j in range(0, len(matrix[i])): # this inner loop, is responsible for the actual values
#             if j > 0:
#                 line += " + "
#             line += str(matrix[i][j])
#             total += matrix[i][j]
#         # print(line + " = " + str(10))
#         print("{} = {}".format(line, total))
#
#
#     for i in range(0, len(matrix)):
#         total = 0
#         for j in range(0, len(matrix[i])):
#             total += matrix[j][i]
#         print(total)
#
#
# newMatrix = newRandomMatrix()
# printMatrix(newMatrix)
