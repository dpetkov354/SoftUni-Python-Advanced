clothes_stack = [int(x) for x in input().split()]
cap = int(input())
rack_cap = cap
count_racks = 1

while clothes_stack:
    last_cloth = clothes_stack[-1]
    if last_cloth <= rack_cap:
        rack_cap -= last_cloth
        clothes_stack.pop()
    else:
        rack_cap = cap
        count_racks += 1

print(count_racks)
