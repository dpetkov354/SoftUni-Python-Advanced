players = list(input().split(", "))
player_one = players[0]
player_two = players[1]
current_round = 1

matrix = list(list(input().split(sep=" ")) for i in range(6))
winner = ""

player_one_pause = 0
player_two_pause = 0

while winner == "":
    if current_round % 2 != 0:
        current_player = player_one
        opponent = player_two
        coordinates = list(map(int, ((input().strip("()")).split(", "))))
        cell = str(matrix[coordinates[0]][coordinates[1]])
        if player_one_pause > 0:
            player_one_pause -= 1
            current_round += 1
            continue
    else:
        current_player = player_two
        opponent = player_one
        coordinates = list(map(int, ((input().strip("()")).split(", "))))
        cell = str(matrix[coordinates[0]][coordinates[1]])
        if player_two_pause > 0:
            player_two_pause -= 1
            current_round += 1
            continue

    if cell == "E":
        winner = str(current_player)
        print(f"{winner} found the Exit and wins the game!")
        break
    elif cell == "T":
        print(f"{current_player} is out of the game! The winner is {opponent}.")
        break
    elif cell == "W":
        print(f"{current_player} hits a wall and needs to rest.")
        if current_player == player_one:
            player_one_pause = 1
        else:
            player_two_pause = 1
    else:
        current_round += 1
        continue

    current_round += 1
