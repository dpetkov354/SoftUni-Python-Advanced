from collections import deque

total_food = int(input())
all_orders = deque([int(x) for x in input().split()])

biggest_order = max(all_orders)
print(biggest_order)

while all_orders:
    completed = False
    for order in all_orders:
        if total_food >= order:
            all_orders.popleft()
            total_food -= order
            break
        else:
            completed = True
            break

    if completed:
        break

if not all_orders:
    print('Orders complete')
else:
    print(f'Orders left: {" ".join([str(x) for x in all_orders])}')
