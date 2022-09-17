from collections import deque

n = int(input())
pumps = deque()

for _ in range(n):
    pump_details = [int(x) for x in input().split()]
    pumps.append(pump_details)

for starts in range(n):
    tank = 0
    failed = False

    for details in pumps:
        fuel = details[0]
        kms = details[1]
        tank += fuel
        if kms > tank:
            failed = True
            break
        else:
            tank -= kms

    if failed:
        removed = pumps.popleft()
        pumps.append(removed)
    else:
        print(starts)
        break
