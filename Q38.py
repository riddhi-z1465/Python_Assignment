# Write a function to find the transpose of a given matrix (list of lists).
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
print("Enter the matrix:")
matrix = []
for i in range(rows):
    row = list(map(int, input(f"Enter row {i + 1} (space-separated values): ").split()))
    if len(row) != cols:
        print(f"Error: You must enter exactly {cols} values.")
        exit()  
    matrix.append(row)
transposed_matrix = []
for i in range(cols):
    transposed_row = []
    for j in range(rows):
        transposed_row.append(matrix[j][i])
    transposed_matrix.append(transposed_row)
print("Transposed matrix:")
for row in transposed_matrix:
    print(row)