numbers = list(map(int, input().split()))

for _ in range(len(numbers)):
    removed_element = numbers.pop()
    print(removed_element, end=" ")
