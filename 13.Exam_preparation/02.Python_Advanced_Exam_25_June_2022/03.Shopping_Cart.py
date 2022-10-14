def shopping_cart(*args):
    output, result = "", {"Dessert": [], "Pizza": [], "Soup": []}
    for info in args:
        if "Stop" in info:
            break
        meal, product, = info
        for meal_type, number_product in (("Soup", 3), ("Pizza", 4), ("Dessert", 2)):
            if meal == meal_type and len(result[meal]) != number_product and product not in result[meal]:
                result[meal].append(product)
                break

    for p_meal, p_product in sorted(result.items(), key=lambda x: (-len(x[1]), x[0])):
        output += f"{p_meal}:\n"
        for item in sorted(p_product):
            output += f" - {item}\n"
    if len(output) == 22:
        output = "No products in the cart!"
    return output


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    "Stop"
))

print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))

print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
