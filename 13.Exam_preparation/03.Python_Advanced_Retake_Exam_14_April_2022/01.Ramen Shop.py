from collections import deque

ramen_dishes = deque(map(int, input().split(', ')))
customers = deque(map(int, input().split(', ')))

while len(ramen_dishes) > 0 and len(customers) > 0:
    ramen = ramen_dishes.pop()
    customer = customers.popleft()

    if ramen == customer:
        continue

    elif ramen > customer:
        ramen -= customer
        ramen_dishes.append(ramen)
        continue

    elif ramen < customer:
        customer -= ramen
        customers.appendleft(customer)
        continue

if len(customers) == 0:
    print("Great job! You served all the customers.")
    if len(ramen_dishes) > 0:
        print(f"Bowls of ramen left: {(', '.join(list(map(str, ramen_dishes))))}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {(', '.join(list(map(str, customers))))}")
