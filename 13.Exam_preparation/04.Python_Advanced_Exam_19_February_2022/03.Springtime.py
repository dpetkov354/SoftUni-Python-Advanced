def start_spring(**kwargs):
    objects = {}
    result = ""

    for value, key in kwargs.items():
        if key in objects:
            objects[key].append(value)
        else:
            objects[key] = []
            objects[key].append(value)

    ordered_dict = dict(sorted(objects.items(), key=lambda x: x[1], reverse=True))

    for types, objects in sorted(ordered_dict.items(), key=lambda x: (-len(x[1]), x[0])):
        result += f"{types}:\n"
        for item in sorted(objects):
            result += f"-{item}\n"

    return result


example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))
