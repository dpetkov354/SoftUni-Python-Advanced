from collections import deque

people = deque()
water = int(input())
end_point = True

while end_point is True:
    user_input = input()

    if user_input == "Start":
        while True:
            command = list(input().split())

            if len(command) == 1 and command[0] == "End":
                end_point = False
                break

            elif len(command) == 1 and command[0] != "End":
                request = int(command[0])

                if request <= water:
                    water -= request
                    current_person = people.popleft()
                    print(f"{current_person} got water")
                else:
                    current_person = people.popleft()
                    print(f"{current_person} must wait")

            elif command[0] == "refill":
                refill = int(command[1])
                water += refill

    people.append(user_input)

print(f"{water} liters left")
