first_sequence = set(int(x) for x in input().split())
second_sequence = set(int(x) for x in input().split())
n = int(input())

for _ in range(n):
    user_input = input().split()
    command_first = user_input[0]
    command_second = user_input[1]
    command_tuple = set(int(num) for num in user_input[2:])

    if command_first == "Check" and command_second == "Subset":
        if first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence):
            print("True")
        else:
            print("False")

    elif command_first == "Add" and command_second == "First":
        first_sequence.update(command_tuple)

    elif command_first == "Add" and command_second == "Second":
        second_sequence.update(command_tuple)

    elif command_first == "Remove" and command_second == "First":
        first_sequence.difference_update(command_tuple)

    elif command_first == "Remove" and command_second == "Second":
        second_sequence.difference_update(command_tuple)

print(*(sorted(first_sequence)), sep=", ")
print(*(sorted(second_sequence)), sep=", ")
