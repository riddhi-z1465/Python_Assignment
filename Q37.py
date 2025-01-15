# Prompt the user for two 2D matrices (lists of lists) of the same dimensions. Perform matrix addition and print the result.
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
print("Enter the first matrix:")
matrix1 = []
for i in range(rows):
    row = list(map(int, input(f"Enter row {i + 1} (space-separated values): ").split()))
    if len(row) != cols:
        print(f"Error: You must enter exactly {cols} values.")
        exit()  
    matrix1.append(row)

print("Enter the second matrix:")
matrix2 = []
for i in range(rows):
    row = list(map(int, input(f"Enter row {i + 1} (space-separated values): ").split()))
    if len(row) != cols:
        print(f"Error: You must enter exactly {cols} values.")
        exit() 
    matrix2.append(row)
result_matrix = []
for i in range(rows):
    result_row = []
    for j in range(cols):
        result_row.append(matrix1[i][j] + matrix2[i][j])
    result_matrix.append(result_row)
print("Result of matrix addition:")
for row in result_matrix:
    print(row)