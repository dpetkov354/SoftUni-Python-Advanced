from collections import deque

seats = list(input().split(', '))
matches = []
rotations_count = 0
removed_count = 0
first_seq = deque(map(int, input().split(', ')))
second_seq = deque(map(int, input().split(', ')))

while True:
    rotations_count += 1
    current_ascii = chr(first_seq[0] + second_seq[-1])
    first_guess = str(first_seq[0]) + current_ascii
    second_guess = str(second_seq[-1]) + current_ascii

    if first_guess in seats:
        first_seq.popleft()
        second_seq.pop()
        matches.append(first_guess)
        seats.remove(first_guess)
        removed_count += 1

    elif second_guess in seats:
        first_seq.popleft()
        second_seq.pop()
        matches.append(second_guess)
        seats.remove(second_guess)
        removed_count += 1
    else:
        move_first = first_seq.popleft()
        move_second = second_seq.pop()
        first_seq.append(move_first)
        second_seq.appendleft(move_second)

    if rotations_count == 10:
        break

    elif removed_count == 3:
        break

    else:
        continue

print(f"Seat matches: {', '.join(matches)}")
print(f"Rotations count: {rotations_count}")



