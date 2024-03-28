# Find the product of two square matrix

print("\n\t\tMatrix Multiplication\n\nSquare Matrix only")

n = int(input("Enter the number of rows and columns: "))

print("Matrix 1")

matrix1 = [[int(input("Enter the number: "))
            for i in range(n)] for j in range(n)]

print("\nMatrix 2")

matrix2 = [[int(input("Enter the number: "))
            for i in range(n)] for j in range(n)]

result_matrix = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(n):
        result_matrix[i][j] = matrix1[i][j]*matrix2[i][j]

for i in range(n):
    for j in range(n):
        print(result_matrix[i][j], end=" ")
    print()
