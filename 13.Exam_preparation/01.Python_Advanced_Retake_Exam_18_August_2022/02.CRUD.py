matrix = list(list(input().split(sep=" ")) for i in range(6))
starting_position = list(map(int, ((input().replace(", ", "")).replace("(", "")).replace(")", "")))

user_input = list(input().split(", "))

while user_input[0] != "Stop":
    command = user_input

    if command[0] == "Create":
        direction = command[1]
        value = command[2]
        if direction == "up":
            starting_position[0] -= 1
        elif direction == "down":
            starting_position[0] += 1
        elif direction == "left":
            starting_position[1] -= 1
        elif direction == "right":
            starting_position[1] += 1

        if matrix[starting_position[0]][starting_position[1]] == ".":
            matrix[starting_position[0]][starting_position[1]] = str(value)
        else:
            pass

    elif command[0] == "Update":
        direction = command[1]
        value = command[2]
        if direction == "up":
            starting_position[0] -= 1
        elif direction == "down":
            starting_position[0] += 1
        elif direction == "left":
            starting_position[1] -= 1
        elif direction == "right":
            starting_position[1] += 1

        if matrix[starting_position[0]][starting_position[1]] != ".":
            matrix[starting_position[0]][starting_position[1]] = str(value)
        else:
            pass

    elif command[0] == "Delete":
        direction = command[1]
        if direction == "up":
            starting_position[0] -= 1
        elif direction == "down":
            starting_position[0] += 1
        elif direction == "left":
            starting_position[1] -= 1
        elif direction == "right":
            starting_position[1] += 1

        if matrix[starting_position[0]][starting_position[1]] != ".":
            matrix[starting_position[0]][starting_position[1]] = "."
        else:
            pass

    elif command[0] == "Read":
        direction = command[1]
        if direction == "up":
            starting_position[0] -= 1
        elif direction == "down":
            starting_position[0] += 1
        elif direction == "left":
            starting_position[1] -= 1
        elif direction == "right":
            starting_position[1] += 1

        if matrix[starting_position[0]][starting_position[1]] != ".":
            print(matrix[starting_position[0]][starting_position[1]])
        else:
            pass

    user_input = list(input().split(", "))

for line in matrix:
    print(' '.join(map(str, line)))
