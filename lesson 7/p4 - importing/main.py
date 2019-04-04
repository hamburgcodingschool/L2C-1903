import matrix_functions as mf

nm = mf.newRandomMatrix(3, 1, 2)
totalR = mf.calculateSumMatrixRows(nm)
totalC = mf.calculateSumMatrixCols(nm)

mf.printMatrix(nm, totalR, totalC)

import random

# from matrix_functions
#
# nm = newRandomMatrix(3, 1, 2)
# totalR = calculateSumMatrixRows(nm)
# totalC = calculateSumMatrixCols(nm)
#
# printMatrix(nm, totalR, totalC)