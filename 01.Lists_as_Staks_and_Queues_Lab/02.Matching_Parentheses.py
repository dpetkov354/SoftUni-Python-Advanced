string = [*input()]
stack = []

for index, item in enumerate(string):
    if item == "(":
        stack.append(index)
    elif item == ")":
        result = []
        sequence = ""
        opening_index = stack.pop()
        closing_index = index
        for letter in range(opening_index, closing_index + 1):
            result.append(string[letter])
        print(sequence.join(result))
