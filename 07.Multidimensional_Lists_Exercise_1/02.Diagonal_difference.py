n = int(input())
matrix = []
primary = []
secondary = []

for _ in range(n):
    user_input = list(input().split())
    matrix.append(user_input)

for i in range(0, len(matrix)):
    primary.append(int(matrix[i][i]))
    secondary.append(int(matrix[i][-i - 1]))

print(f"{abs(sum(primary) - sum(secondary))}")
