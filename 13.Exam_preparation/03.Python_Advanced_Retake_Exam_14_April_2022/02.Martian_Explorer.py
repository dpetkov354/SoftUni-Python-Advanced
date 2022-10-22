matrix = list(list(input().split(sep=" ")) for i in range(6))
commands = list(map(str, input().split(sep=", ")))

rover_position = []
water = 0
concrete = 0
metal = 0

for row in range(0, len(matrix)):
    for col in range(0, len(matrix[row])):
        if matrix[row][col] == 'E':
            rover_position.append(int(row))
            rover_position.append(int(col))

for command in commands:
    if command == 'up':
        if rover_position[0] > 0:
            rover_position[0] -= 1
        elif rover_position[0] == 0:
            rover_position[0] = 5

    elif command == 'down':
        if rover_position[0] < 5:
            rover_position[0] += 1
        elif rover_position[0] == 5:
            rover_position[0] = 0

    elif command == 'left':
        if rover_position[1] > 0:
            rover_position[1] -= 1
        elif rover_position[1] == 0:
            rover_position[1] = 5

    elif command == 'right':
        if rover_position[1] < 5:
            rover_position[1] += 1
        elif rover_position[1] == 5:
            rover_position[1] = 0

    if matrix[rover_position[0]][rover_position[1]] == "R":
        print(f"Rover got broken at ({rover_position[0]}, {rover_position[1]})")
        break

    elif matrix[rover_position[0]][rover_position[1]] == "-":
        continue

    elif matrix[rover_position[0]][rover_position[1]] == "W":
        water += 1
        print(f"Water deposit found at ({rover_position[0]}, {rover_position[1]})")
        continue

    elif matrix[rover_position[0]][rover_position[1]] == "M":
        metal += 1
        print(f"Metal deposit found at ({rover_position[0]}, {rover_position[1]})")
        continue

    elif matrix[rover_position[0]][rover_position[1]] == "C":
        concrete += 1
        print(f"Concrete deposit found at ({rover_position[0]}, {rover_position[1]})")
        continue

if water >= 1 and metal >= 1 and concrete >= 1:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
