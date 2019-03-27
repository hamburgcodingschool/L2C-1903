
someData = [
    [7, 8, 5],
    [2, 1, 0],
    [7, 8, 8]
]

def printMatrix(matrix):


    for i in range(0, len(matrix)):
        line = ""
        for j in range(0, len(matrix[i])):
            if j > 0:
                line += ", "
            line += str(matrix[i][j])
        print(line)

printMatrix(someData)