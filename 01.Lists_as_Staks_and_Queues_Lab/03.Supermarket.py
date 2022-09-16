from collections import deque

clients = deque()


while True:
    user_input = input()
    if user_input == "End":
        break
    if user_input == "Paid":
        for person in range(len(clients)):
            current_client = clients.popleft()
            print(current_client)
    else:
        clients.append(user_input)

print(f"{len(clients)} people remaining.")
