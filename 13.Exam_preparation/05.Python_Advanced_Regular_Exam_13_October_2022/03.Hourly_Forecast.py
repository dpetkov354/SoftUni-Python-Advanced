def forecast(*args):
    output, result = "", {"Sunny": [], "Cloudy": [], "Rainy": []}
    for info in args:
        location, weather = info
        if weather in result:
            result[weather].append(str(location))
    for p_weather, p_location in sorted(result.items(), key=lambda x: (-len(x[1]))):
        for city in sorted(p_location):
            output += f"{city} - {p_weather}\n"
    return output


print(forecast(
    ("Rainy", "Rainy")))


print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))

print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))
