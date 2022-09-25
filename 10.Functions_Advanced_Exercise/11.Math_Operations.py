def math_operations(*args, **kwargs):
    numbers = args
    dictionary = kwargs
    rounded = 0
    for index in range(len(numbers)):
        current_index = index-rounded*4
        if current_index == 0:
            dictionary['a'] += numbers[index]
        elif current_index == 1:
            dictionary['s'] -= numbers[index]
        elif current_index == 2 and not numbers[index] == 0:
            dictionary['d'] /= numbers[index]
        elif current_index == 3:
            dictionary['m'] *= numbers[index]
            rounded += 1
    result = ''
    for key, value in sorted(dictionary.items(), key=lambda kvp: (-kvp[1], kvp[0])):
        result += f"{key}: {value:.1f}\n"
    return result


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
