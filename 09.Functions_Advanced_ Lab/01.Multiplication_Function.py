def multiply(result=1, *args):
    if not args:
        return result

    return multiply(result * args[0], *args[1:])


print(multiply(1, 4, 5))
print(multiply(4, 5, 6, 1, 3))
print(multiply(2, 0, 1000, 5000))
