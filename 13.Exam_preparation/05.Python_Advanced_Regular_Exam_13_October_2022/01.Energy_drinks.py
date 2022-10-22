from collections import deque

caffeine = deque(map(int, input().split(', ')))
energy_drinks = deque(map(int, input().split(', ')))

max_caffeine = 300
personal_caffeine = 0

while len(caffeine) > 0 and len(energy_drinks) > 0:
    current_drink = energy_drinks.popleft()
    current_caffeine = caffeine.pop()
    total_caffeine = current_drink * current_caffeine

    if total_caffeine <= (max_caffeine - personal_caffeine):
        personal_caffeine += total_caffeine
        continue

    elif total_caffeine > (max_caffeine - personal_caffeine):
        energy_drinks.append(current_drink)
        if personal_caffeine >= 30:
            personal_caffeine -= 30
        else:
            personal_caffeine = 0


if len(energy_drinks) > 0:
    print(f"Drinks left: {', '.join(map(str, energy_drinks))}")
else:
    print(f"At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {personal_caffeine} mg caffeine.")
