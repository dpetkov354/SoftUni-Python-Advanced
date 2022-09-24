def area(length, width):
    return f"Rectangle area: {length * width}"


def perimeter(length, width):
    return f"Rectangle perimeter: {(length+ width) * 2}"


def rectangle(length, width):
    if type(length) is not int:
        return "Enter valid values!"
    if type(width) is not int:
        return "Enter valid values!"

    return f"{area(length, width)}\n{perimeter(length, width)}"


print(rectangle(2, 10))
print(rectangle('2', 10))
