def even_odd(*args):
    command = args[-1]
    nums = args[0:-1]
    result = []
    if command == 'even':
        for i in nums:
            if i % 2 == 0:
                result.append(i)
        return result
    elif command == 'odd':
        for i in nums:
            if i % 2 != 0:
                result.append(i)
        return result


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
