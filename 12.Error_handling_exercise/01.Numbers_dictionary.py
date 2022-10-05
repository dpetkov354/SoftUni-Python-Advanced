def value_must_be_integer():
    return f"The variable number must be an integer"


def number_does_not_exist():
    return f"Number does not exist in dictionary"


nums_dictionary = {}

while True:
    line = input()
    if line == "Search":
        break
    try:
        number_as_string = line
        number = int(input())
        nums_dictionary[number_as_string] = number
    except ValueError:
        print(value_must_be_integer())

while True:
    line = input()
    if line == "Remove":
        break
    searched = line
    try:
        print(nums_dictionary[searched])
    except ValueError:
        print(number_does_not_exist())

while True:
    line = input()
    if line == "End":
        break
    searched = line
    try:
        del nums_dictionary[searched]
    except KeyError:
        print(number_does_not_exist())

print(nums_dictionary)
