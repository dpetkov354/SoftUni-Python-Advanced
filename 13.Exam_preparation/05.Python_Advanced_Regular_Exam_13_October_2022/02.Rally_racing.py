n = int(input())
car_number = str(input())
matrix = list(list(input().split(sep=" ")) for i in range(n))
km_passed = 0
car_place = [0, 0]
finish_place = []
tunnel_one = []
tunnel_two = []
finish = False
tunnel_pass = False
command = input()

for row in range(0, len(matrix)):
    for col in range(0, len(matrix[row])):
        if matrix[row][col] == 'T':
            if len(tunnel_one) == 0:
                tunnel_one.append(int(row))
                tunnel_one.append(int(col))
            else:
                tunnel_two.append(int(row))
                tunnel_two.append(int(col))
        elif matrix[row][col] == 'F':
            finish_place.append(int(row))
            finish_place.append(int(col))


while command != "End":
    if command == "up":
        car_place[0] -= 1
        km_passed += 10
    elif command == "down":
        car_place[0] += 1
        km_passed += 10
    elif command == "left":
        car_place[1] -= 1
        km_passed += 10
    elif command == "right":
        car_place[1] += 1
        km_passed += 10

    if car_place == finish_place:
        finish = True
        break

    if car_place == tunnel_one and tunnel_pass == False:
        matrix[tunnel_one[0]][tunnel_one[1]] = "."
        matrix[tunnel_two[0]][tunnel_two[1]] = "."
        car_place = tunnel_two
        km_passed += 20
        tunnel_pass = True

    elif car_place == tunnel_two and tunnel_pass == False:
        matrix[tunnel_one[0]][tunnel_one[1]] = "."
        matrix[tunnel_two[0]][tunnel_two[1]] = "."
        car_place = tunnel_one
        km_passed += 20
        tunnel_pass = True

    command = input()

matrix[car_place[0]][car_place[1]] = "C"

if finish is False:
    print(f"Racing car {car_number} DNF.")
elif finish is True:
    print(f"Racing car {car_number} finished the stage!")

print(f"Distance covered {km_passed} km.")

for i in matrix:
    print(''.join(map(str, i)))
