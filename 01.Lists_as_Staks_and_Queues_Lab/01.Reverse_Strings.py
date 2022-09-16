string = [*input()]

for letter in range(len(string)):
    removed_element = string.pop()
    print(removed_element, end="")
