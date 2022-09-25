height, width = input().split()
matrix = []
square_count = 0

for _ in range(int(height)):
    user_input = list(input().split())
    matrix.append(user_input)

for i in range(len(matrix) - 1):
    for j in range(len(matrix[i]) - 1):
        first = matrix[i][j]
        second = matrix[i][j + 1]
        third = matrix[i + 1][j]
        forth = matrix[i + 1][j + 1]
        if matrix[i][j] == matrix[i][j + 1] and matrix[i][j] == matrix[i + 1][j] and matrix[i][j] == matrix[i + 1][j + 1]:
            square_count += 1
        else:
            continue

print(square_count)
