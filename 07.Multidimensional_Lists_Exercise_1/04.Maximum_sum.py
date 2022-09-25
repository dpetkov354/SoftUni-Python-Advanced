height, width = input().split()
matrix = []
max_sum = -99999999999999999999999999999999999999999999999999999999999999999999
winner_matrix = []

for _ in range(int(height)):
    user_input = list(map(int, input().split()))
    matrix.append(user_input)

for i in range(len(matrix) - 2):
    for j in range(len(matrix[i]) - 2):
        current_sum = matrix[i][j] + matrix[i][j + 1] + matrix[i][j + 2] + matrix[i + 1][j] + matrix[i + 1][j + 1] + \
                      matrix[i + 1][j + 2] + matrix[i + 2][j] + matrix[i + 2][j + 1] + matrix[i + 2][j + 2]
        if current_sum > max_sum:
            max_sum = current_sum
            winner_matrix.clear()
            winner_matrix = [[matrix[i][j], matrix[i][j + 1], matrix[i][j + 2]], [matrix[i + 1][j], matrix[i + 1][j + 1], matrix[i + 1][j + 2]], [matrix[i + 2][j], matrix[i + 2][j + 1], matrix[i + 2][j + 2]]]

        else:
            continue


print(f"Sum = {max_sum}")
print('\n'.join([' '.join([str(j) for j in n]) for n in winner_matrix]))
