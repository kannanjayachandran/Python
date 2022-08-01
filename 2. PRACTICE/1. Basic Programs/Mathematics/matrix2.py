# WAP to multiply two matrices.

import numpy as np

row1 = int(input("Enter the number of rows: "))
col1 = int(input("Enter the number of columns: "))

matrix1 = [[int(input("Enter Number: ")) for i in range(col1)]
           for j in range(row1)]

row2 = int(input("Enter the number of rows: "))
col2 = int(input("Enter the number of columns: "))

matrix2 = [[int(input("Enter Number: ")) for i in range(col2)]
           for j in range(row2)]

np_matrix1 = np.matrix(matrix1)
np_matrix2 = np.matrix(matrix2)
print("\nMatrix 1: ", np_matrix1, "\n\nMatrix 2: ", np_matrix2)

if col1 == row2:
    result_matrix = np.matmul(np_matrix1, np_matrix2)
    print("Resultant matrix is : ", result_matrix)
else:
    print("Incompatible Matirces.")
